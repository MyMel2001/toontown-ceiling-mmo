from panda3d.core import *
from pandac.PandaModules import *
ConfigVariableString("window-type","none").setValue("none")
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import sys
import random
import math

class ToontownServer(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.cManager = QueuedConnectionManager()
        self.cListener = QueuedConnectionListener(self.cManager, 0)
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager, 0)

        self.activeConnections = []
        self.clients = {} # conn: {dna, pos, zone, name}
        self.cogs = {} # zoneId: {cogId: data}
        self.nextCogId = 1

        # Zone bounds for COG spawning (minX, maxX, minY, maxY)
        # Based on actual street/playground sizes from DNA files and tunnel positions
        # Bounds are set to encompass the playable street area between tunnel entrances
        self.zoneBounds = {
            # Playgrounds - no COGs spawn in safe zones
            0: (-60, 60, -60, 60),      # Melodyland
            1: (-100, 100, -100, 100),  # TTC (no COGs in safe zone)
            2: (-150, 150, -150, 150),  # DD
            3: (-80, 80, -80, 80),      # DG
            4: (-200, 200, -200, 200),  # Goofy Speedway
            9: (-80, 80, -80, 80),      # Brrrgh
            10: (-60, 60, -60, 60),     # Dreamland
            # TTC Streets (zone IDs match file numbers)
            11: (-350, -60, -400, 0),   # Loopy Lane: TTC(-90,-80) to DG(-360,-400)
            12: (-560, -60, -80, 130),  # Punchline Place: TTC(-75,115) to MML(-580,-30)
            13: (-20, 780, -20, 120),   # Silly Street: TTC(0,0) to DD(780,90)
            # DD Streets
            14: (-80, 700, -20, 130),   # Elm Street: DG(-61,8) to TTC(678,98)
            18: (140, 400, -80, 10),    # Barnacle Blvd: DD(160,-50) to TTC(370,-30)
            19: (-310, -170, -440, -110), # Seaweed St: DD(-185,-125) to DG(-295,-430)
            20: (-20, 650, -80, 10),    # Lighthouse Lane: DD(0,0) to BR(630,-50)
            # MM Streets
            15: (-480, -150, 20, 230),  # Tenor Terrace: MML(-165,40) to TTC(-460,210)
            16: (60, 170, 140, 420),    # Alto Ave: MML(80,165) to BR(140,400)
            17: (30, 720, 180, 240),    # Baritone Blvd: DL(60,0) to MML(695,215)
            # DG Streets
            21: (-60, 720, -30, 110),   # Labyrinth Lane: DG(-35,5) to DD(695,85)
            22: (-330, -70, -80, 340),  # Oak St: DG(-85,-60) to Sellbot(-311,316)
            # BR Streets
            23: (160, 460, -100, 230),  # Walrus Way: BR(175,-80) to DD(440,210)
            24: (100, 175, 130, 390),   # Sleet St: BR(120,150) to MML(155,370)
            25: (60, 220, 180, 390),    # Polar Place: BR(80,200) to Lawbot(205,370)
            # DL Streets
            26: (-120, 30, -520, 60),   # Lullaby Lane: DL(5,40) to MML(-99,-509)
            27: (-170, 100, -100, 150), # Pajama Place: DL(80,130) to Cashbot(-147,-76)
        }

        port = 1913
        self.tcpSocket = self.cManager.openTCPServerRendezvous(port, 5)
        if self.tcpSocket:
            self.cListener.addConnection(self.tcpSocket)
            print(f"Server started on port {port}")
            self.connIds = {} # mapping connection object to a small stable integer ID
            self.nextId = 1
        else:
            print(f"Failed to open port {port}")
            sys.exit()

        self.taskMgr.add(self.listenTask, "ListenTask")
        self.taskMgr.add(self.readTask, "ReadTask")
        self.taskMgr.add(self.cogUpdateTask, "CogUpdateTask")

    def cogUpdateTask(self, task):
        dt = globalClock.getDt()
        for zoneId, cogs in self.cogs.items():
            # If no players in zone, maybe skip?
            playersInZone = [c for c in self.clients if self.clients[c]['zone'] == zoneId]
            if not playersInZone:
                continue

            # Get zone bounds for this zone
            bounds = self.zoneBounds.get(zoneId, (-100, 100, -100, 100))
            minX, maxX, minY, maxY = bounds
            margin = 10  # Keep COGs away from edges

            for cogId, cog in cogs.items():
                if cog.get('inBattle'): continue

                # Simple random walk
                dist = (Vec3(cog['pos']) - Vec3(cog['target_pos'])).length()
                if dist > 1:
                    dir = Vec3(cog['target_pos']) - Vec3(cog['pos'])
                    dir.normalize()
                    newPos = Vec3(cog['pos']) + dir * 5 * dt
                    cog['pos'] = (newPos.getX(), newPos.getY(), newPos.getZ())
                    # Calculate H
                    cog['h'] = math.atan2(-dir.getX(), dir.getY()) * 180 / math.pi

                    # Enforce bounds - clamp position to stay within zone
                    x, y, z = cog['pos']
                    x = max(minX + margin, min(maxX - margin, x))
                    y = max(minY + margin, min(maxY - margin, y))
                    cog['pos'] = (x, y, z)

                    # Broadcast update periodically or if moved enough
                    # For now just broadcast every tick to keep it simple, but maybe too much traffic
                else:
                    # Pick a new target within bounds
                    new_x = random.uniform(minX + margin, maxX - margin)
                    new_y = random.uniform(minY + margin, maxY - margin)
                    cog['target_pos'] = (new_x, new_y, cog['pos'][2])

            self.broadcastCogPos(zoneId)

        return Task.cont

    def spawnCogsForZone(self, zoneId):
        if zoneId not in self.cogs:
            self.cogs[zoneId] = {}
        
        # Only spawn cogs if the zone is empty and not a safe zone
        if not self.cogs[zoneId]:
            # Playgrounds/Safe Zones: 0-4, 9-10; Misc: 6-7
            if zoneId in [0, 1, 2, 3, 4, 6, 7, 9, 10]:
                return

            # Spawn 5-8 cogs per zone
            numCogs = random.randint(5, 8)
            for _ in range(numCogs):
                self.spawnCog(zoneId)

    def spawnCog(self, zoneId):
        if zoneId not in self.cogs:
            self.cogs[zoneId] = {}

        cogId = self.nextCogId
        self.nextCogId += 1

        cogData = random.choice([
            ("Flunky", "C"), ("Pencil Pusher", "B"), ("Yesman", "A"), ("Micromanager", "C"),
            ("Downsizer", "B"), ("Head Hunter", "A"), ("Corporate Raider", "C"), ("The Big Cheese", "A"),
            ("Bottom Feeder", "C"), ("Bloodsucker", "B"), ("Double Talker", "A"), ("Ambulance Chaser", "C"),
            ("Backstabber", "B"), ("Spin Doctor", "A"), ("Legal Eagle", "C"), ("Big Wig", "A"),
            ("Short Change", "C"), ("Penny Pincher", "B"), ("Tightwad", "A"), ("Bean Counter", "C"),
            ("Number Cruncher", "B"), ("Money Bags", "A"), ("Loan Shark", "C"), ("Robber Baron", "A"),
            ("Cold Caller", "C"), ("Telemarketer", "B"), ("Name Dropper", "A"), ("Glad Hander", "C"),
            ("Mover & Shaker", "B"), ("Two-Face", "A"), ("The Mingler", "C"), ("Mr. Hollywood", "A")
        ])

        name, type = cogData
        level = random.randint(1, 12)

        # Use zone-specific bounds for spawning
        if zoneId in self.zoneBounds:
            minX, maxX, minY, maxY = self.zoneBounds[zoneId]
            # Spawn within the bounds, with some margin from edges
            margin = 20
            x = random.uniform(minX + margin, maxX - margin)
            y = random.uniform(minY + margin, maxY - margin)
        else:
            # Default spawn area
            x = random.uniform(-100, 100)
            y = random.uniform(-100, 100)
        pos = (x, y, 0)

        self.cogs[zoneId][cogId] = {
            'name': name,
            'type': type,
            'level': level,
            'pos': pos,
            'orig_pos': pos,
            'target_pos': pos,
            'h': 0,
            'hp': (level + 1) * (level + 2),
            'maxHp': (level + 1) * (level + 2),
            'inBattle': False
        }

        # Broadcast to all players in zone
        self.broadcastCogSpawn(zoneId, cogId)

    def sendCogSpawn(self, conn, zoneId, cogId):
        if zoneId not in self.cogs or cogId not in self.cogs[zoneId]:
            return
            
        cog = self.cogs[zoneId][cogId]
        dg = NetDatagram()
        dg.addUint8(7) # COG SPAWN
        dg.addUint32(cogId)
        dg.addString(cog['type'])
        dg.addString(cog['name'])
        dg.addUint8(cog['level'])
        dg.addFloat32(cog['pos'][0])
        dg.addFloat32(cog['pos'][1])
        dg.addFloat32(cog['pos'][2])
        dg.addFloat32(cog['h'])
        self.cWriter.send(dg, conn)

    def broadcastCogSpawn(self, zoneId, cogId):
        for conn, data in self.clients.items():
            if data['zone'] == zoneId:
                self.sendCogSpawn(conn, zoneId, cogId)

    def broadcastCogPos(self, zoneId):
        if zoneId not in self.cogs: return
        
        dg = NetDatagram()
        dg.addUint8(8) # COG POS
        dg.addUint16(len(self.cogs[zoneId]))
        for cogId, cog in self.cogs[zoneId].items():
            dg.addUint32(cogId)
            dg.addFloat32(cog['pos'][0])
            dg.addFloat32(cog['pos'][1])
            dg.addFloat32(cog['pos'][2])
            dg.addFloat32(cog['h'])
            dg.addString("Walk" if (Vec3(cog['pos']) - Vec3(cog['target_pos'])).length() > 1 else "Neutral")

        for conn, data in self.clients.items():
            if data['zone'] == zoneId:
                self.cWriter.send(dg, conn)

    def listenTask(self, task):
        if self.cListener.newConnectionAvailable():
            rendezvous = PointerToConnection()
            netAddress = NetAddress()
            newConnection = PointerToConnection()

            if self.cListener.getNewConnection(rendezvous, netAddress, newConnection):
                newConnection = newConnection.p()
                self.activeConnections.append(newConnection)
                self.cReader.addConnection(newConnection)
                self.connIds[newConnection] = self.nextId
                self.nextId += 1
                print(f"New connection from {netAddress} (ID: {self.connIds[newConnection]})")
        return Task.cont

    def readTask(self, task):
        while self.cManager.resetConnectionAvailable():
            conn = PointerToConnection()
            if self.cManager.getResetConnection(conn):
                conn = conn.p()
                self.handleDisconnect(conn)
                self.cReader.removeConnection(conn)

        while self.cReader.dataAvailable():
            datagram = NetDatagram()
            if self.cReader.getData(datagram):
                self.processDatagram(datagram)
        return Task.cont

    def handleDisconnect(self, conn):
        if conn in self.clients:
            name = self.clients[conn]['name']
            zone = self.clients[conn]['zone']
            print(f"Player {name} disconnected")
            self.broadcastDespawn(conn, zone)
            self.releaseCogsOwnedBy(conn)
            del self.clients[conn]
        if conn in self.activeConnections:
            self.activeConnections.remove(conn)
        if conn in self.connIds:
            del self.connIds[conn]

    def processDatagram(self, datagram):
        conn = datagram.getConnection()
        it = DatagramIterator(datagram)
        msgID = it.getUint8()

        if msgID == 1: # LOGIN
            name = it.getString()
            dna = []
            dna_len = it.getUint8()
            for i in range(dna_len):
                type = it.getUint8()
                if type == 0: dna.append(it.getString())
                elif type == 1: dna.append(it.getBool())
                elif type == 2: dna.append(it.getUint8())
                elif type == 3: dna.append(None)
            
            zone = it.getUint16()
            x, y, z = it.getFloat32(), it.getFloat32(), it.getFloat32()
            h, p, r = it.getFloat32(), it.getFloat32(), it.getFloat32()

            self.clients[conn] = {
                'name': name,
                'dna': dna,
                'zone': zone,
                'pos': (x, y, z),
                'hpr': (h, p, r),
                'anim': 'Neutral'
            }
            print(f"Player {name} logged in at zone {zone}")
            
            # Spawn cogs for this zone if not already spawned
            self.spawnCogsForZone(zone)

            # Send current players to new player
            for other_conn, data in self.clients.items():
                if other_conn != conn and data['zone'] == zone:
                    self.sendSpawn(conn, other_conn, data)
            
            # Send current cogs to new player
            if zone in self.cogs:
                for cogId in self.cogs[zone]:
                    self.sendCogSpawn(conn, zone, cogId)

            # Broadcast new player to others
            for other_conn in self.clients:
                if other_conn != conn and self.clients[other_conn]['zone'] == zone:
                    self.sendSpawn(other_conn, conn, self.clients[conn])

        elif msgID == 2: # POS UPDATE
            if conn in self.clients:
                x, y, z = it.getFloat32(), it.getFloat32(), it.getFloat32()
                h, p, r = it.getFloat32(), it.getFloat32(), it.getFloat32()
                anim = it.getString()
                self.clients[conn]['pos'] = (x, y, z)
                self.clients[conn]['hpr'] = (h, p, r)
                self.clients[conn]['anim'] = anim
                
                # Broadcast to others in zone
                self.broadcastPos(conn)

        elif msgID == 3: # ZONE CHANGE
            if conn in self.clients:
                old_zone = self.clients[conn]['zone']
                new_zone = it.getUint16()
                self.clients[conn]['zone'] = new_zone
                
                # Despawn from old zone
                self.broadcastDespawn(conn, old_zone)
                self.releaseCogsOwnedBy(conn)
                
                # Spawn cogs for new zone if not already spawned
                self.spawnCogsForZone(new_zone)

                # Spawn in new zone
                for other_conn, data in self.clients.items():
                    if other_conn != conn and data['zone'] == new_zone:
                        self.sendSpawn(conn, other_conn, data)
                        self.sendSpawn(other_conn, conn, self.clients[conn])
                
                # Send current cogs to player
                if new_zone in self.cogs:
                    for cogId in self.cogs[new_zone]:
                        self.sendCogSpawn(conn, new_zone, cogId)

        elif msgID == 4: # CHAT
            if conn in self.clients:
                text = it.getString()
                self.broadcastChat(conn, text)

        elif msgID == 9: # BATTLE REQUEST
            if conn in self.clients:
                cogId = it.getUint32()
                zoneId = self.clients[conn]['zone']
                if zoneId in self.cogs and cogId in self.cogs[zoneId]:
                    cog = self.cogs[zoneId][cogId]
                    if not cog['inBattle']:
                        cog['inBattle'] = True
                        cog['toonId'] = self.connIds[conn]
                        # Broadcast battle start
                        self.broadcastBattleStart(zoneId, cogId, self.connIds[conn])

        elif msgID == 10: # BATTLE ACTION
            if conn in self.clients:
                cogId = it.getUint32()
                damage = it.getUint8()
                zoneId = self.clients[conn]['zone']
                if zoneId in self.cogs and cogId in self.cogs[zoneId]:
                    cog = self.cogs[zoneId][cogId]
                    cog['hp'] -= damage
                    if cog['hp'] <= 0:
                        cog['hp'] = 0
                        # Cog defeated
                        self.broadcastBattleUpdate(zoneId, cogId, damage, cog['hp'])
                        # Remove cog after delay?
                        self.taskMgr.doMethodLater(2.0, self.despawnCog, f"despawnCog-{cogId}", extraArgs=[zoneId, cogId])
                    else:
                        self.broadcastBattleUpdate(zoneId, cogId, damage, cog['hp'])

    def broadcastBattleStart(self, zoneId, cogId, toonId):
        dg = NetDatagram()
        dg.addUint8(9)
        dg.addUint32(cogId)
        dg.addUint32(toonId)
        for conn, data in self.clients.items():
            if data['zone'] == zoneId:
                self.cWriter.send(dg, conn)

    def broadcastBattleUpdate(self, zoneId, cogId, damage, hp):
        dg = NetDatagram()
        dg.addUint8(12) # BATTLE UPDATE
        dg.addUint32(cogId)
        dg.addUint8(damage)
        dg.addUint16(hp)
        for conn, data in self.clients.items():
            if data['zone'] == zoneId:
                self.cWriter.send(dg, conn)

    def despawnCog(self, zoneId, cogId):
        if zoneId in self.cogs and cogId in self.cogs[zoneId]:
            del self.cogs[zoneId][cogId]
            dg = NetDatagram()
            dg.addUint8(11) # COG DESPAWN
            dg.addUint32(cogId)
            for conn, data in self.clients.items():
                if data['zone'] == zoneId:
                    self.cWriter.send(dg, conn)
            
            # Spawn a new cog to replace it after a while
            self.taskMgr.doMethodLater(10.0, lambda task: self.spawnCog(zoneId), f"respawnCog-{zoneId}")

    def sendSpawn(self, target_conn, player_conn, data):
        dg = NetDatagram()
        dg.addUint8(5) # SPAWN MSG
        dg.addUint32(self.connIds.get(player_conn, 0))
        dg.addString(data['name'])
        dg.addUint8(len(data['dna']))
        for item in data['dna']:
            if isinstance(item, str):
                dg.addUint8(0)
                dg.addString(item)
            elif isinstance(item, bool):
                dg.addUint8(1)
                dg.addBool(item)
            elif item is None:
                dg.addUint8(3)
            else:
                dg.addUint8(2)
                dg.addUint8(item)
        dg.addFloat32(data['pos'][0])
        dg.addFloat32(data['pos'][1])
        dg.addFloat32(data['pos'][2])
        dg.addFloat32(data['hpr'][0])
        dg.addFloat32(data['hpr'][1])
        dg.addFloat32(data['hpr'][2])
        dg.addString(data['anim'])
        self.cWriter.send(dg, target_conn)

    def broadcastPos(self, conn):
        data = self.clients[conn]
        dg = NetDatagram()
        dg.addUint8(2) # POS UPDATE
        dg.addUint32(self.connIds.get(conn, 0))
        dg.addFloat32(data['pos'][0])
        dg.addFloat32(data['pos'][1])
        dg.addFloat32(data['pos'][2])
        dg.addFloat32(data['hpr'][0])
        dg.addFloat32(data['hpr'][1])
        dg.addFloat32(data['hpr'][2])
        dg.addString(data['anim'])
        
        for other_conn in self.clients:
            if other_conn != conn and self.clients[other_conn]['zone'] == data['zone']:
                self.cWriter.send(dg, other_conn)

    def broadcastDespawn(self, conn, zone):
        dg = NetDatagram()
        dg.addUint8(6) # DESPAWN
        dg.addUint32(self.connIds.get(conn, 0))
        for other_conn in self.clients:
            if other_conn != conn and self.clients[other_conn]['zone'] == zone:
                self.cWriter.send(dg, other_conn)

    def broadcastChat(self, conn, text):
        dg = NetDatagram()
        dg.addUint8(4)
        dg.addUint32(self.connIds.get(conn, 0))
        dg.addString(text)
        zone = self.clients[conn]['zone']
        for other_conn in self.clients:
            if self.clients[other_conn]['zone'] == zone:
                self.cWriter.send(dg, other_conn)

    def releaseCogsOwnedBy(self, conn):
        if conn not in self.connIds: return
        toonId = self.connIds[conn]
        for zoneId in self.cogs:
            for cogId, cog in self.cogs[zoneId].items():
                if cog.get('inBattle') and cog.get('toonId') == toonId:
                    print(f"Releasing cog {cogId} from battle with toon {toonId}")
                    cog['inBattle'] = False
                    cog['toonId'] = None

server = ToontownServer()
server.run()
