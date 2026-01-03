from panda3d.core import QueuedConnectionManager, QueuedConnectionReader, ConnectionWriter
from panda3d.core import NetDatagram, DatagramIterator, PointerToConnection
from direct.task import Task
from pickAToon import get_builtins
from thirdparty.createToon.src.toon.CeilingToon import Toon
from thirdparty.nametag.toonNametag import createNametag
import os

class Networking:
    def __init__(self, host=os.getenv("IP"), port=1913):
        self.cManager = QueuedConnectionManager()
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager, 0)
        
        self.connection = self.cManager.openTCPClientConnection(host, port, 1000)
        if self.connection:
            self.cReader.addConnection(self.connection)
            print("Connected to server")
        else:
            print("Failed to connect to server")

        self.remotePlayers = {} # id: Toon object
        self.playerNames = {} # id: string name

        base.taskMgr.add(self.readTask, "ClientReadTask")
        base.taskMgr.add(self.sendPosTask, "ClientSendPosTask")

    def readTask(self, task):
        while self.cReader.dataAvailable():
            datagram = NetDatagram()
            if self.cReader.getData(datagram):
                self.processDatagram(datagram)
        return Task.cont

    def processDatagram(self, datagram):
        it = DatagramIterator(datagram)
        msgID = it.getUint8()

        if msgID == 2: # POS UPDATE
            player_id = it.getUint32()
            if player_id in self.remotePlayers:
                x, y, z = it.getFloat32(), it.getFloat32(), it.getFloat32()
                h, p, r = it.getFloat32(), it.getFloat32(), it.getFloat32()
                anim = it.getString()
                toon = self.remotePlayers[player_id]
                toon.toonActor.setPos(x, y, z)
                toon.toonActor.setHpr(h, p, r)
                if toon.animationType != anim:
                    toon.animationType = anim
                    toon.toonActor.loop(anim)

        elif msgID == 5: # SPAWN
            player_id = it.getUint32()
            name = it.getString()
            dna = []
            dna_len = it.getUint8()
            for i in range(dna_len):
                type = it.getUint8()
                if type == 0: dna.append(it.getString())
                elif type == 1: dna.append(it.getBool())
                elif type == 2: dna.append(it.getUint8())
                elif type == 3: dna.append(None)
            
            x, y, z = it.getFloat32(), it.getFloat32(), it.getFloat32()
            h, p, r = it.getFloat32(), it.getFloat32(), it.getFloat32()
            anim = it.getString()

            if player_id not in self.remotePlayers:
                print(f"Spawning player {name}")
                self.playerNames[player_id] = name
                newToon = Toon(*dna)
                newToon.animationType = anim
                newToon.toonActor.setPos(x, y, z)
                newToon.toonActor.setHpr(h, p, r)
                newToon.toonActor.reparentTo(render)
                
                # Create nametag
                head = newToon.toonActor.findAllMatches('**/head*')
                nametag = createNametag(name, (1,1,1,.5), (0,0,1,1))
                nametag.setPos(0,0,2)
                nametag.reparentTo(head[0])
                
                self.remotePlayers[player_id] = newToon

        elif msgID == 6: # DESPAWN
            player_id = it.getUint32()
            if player_id in self.remotePlayers:
                print(f"Despawning player {player_id}")
                self.remotePlayers[player_id].toonActor.cleanup()
                self.remotePlayers[player_id].toonActor.removeNode()
                del self.remotePlayers[player_id]

        elif msgID == 4: # CHAT
            player_id = it.getUint32()
            text = it.getString()
            if hasattr(base, "chatMgr"):
                base.chatMgr.displayMessage(player_id, text)

    def login(self, name, dna, zone, pos, hpr):
        self.playerNames[id(self.connection)] = name
        dg = NetDatagram()
        dg.addUint8(1)
        dg.addString(name)
        dg.addUint8(len(dna))
        for item in dna:
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
        dg.addUint16(zone)
        dg.addFloat32(pos[0])
        dg.addFloat32(pos[1])
        dg.addFloat32(pos[2])
        dg.addFloat32(hpr[0])
        dg.addFloat32(hpr[1])
        dg.addFloat32(hpr[2])
        self.cWriter.send(dg, self.connection)

    def sendPosTask(self, task):
        if not hasattr(base, "localAvatar"): return Task.cont
        
        dg = NetDatagram()
        dg.addUint8(2)
        pos = base.localAvatar.getPos()
        hpr = base.localAvatar.getHpr()
        dg.addFloat32(pos[0])
        dg.addFloat32(pos[1])
        dg.addFloat32(pos[2])
        dg.addFloat32(hpr[0])
        dg.addFloat32(hpr[1])
        dg.addFloat32(hpr[2])
        
        # Get current animation
        anim = "neutral"
        G = get_builtins()
        # This is a bit hacky, but we can check the moving flags in launch.py
        # Or just use the actor's current anim
        # For now, let's assume we can get it from G or base.localAvatar
        if hasattr(base.localAvatar, "getCurrentAnim"):
             anim = base.localAvatar.getCurrentAnim()
             if anim is None: anim = "neutral"
        
        dg.addString(anim)
        self.cWriter.send(dg, self.connection)
        
        task.delayTime = 0.1 # Send 10 times per second
        return Task.again

    def changeZone(self, newZone):
        # Clear remote players when changing zones
        for player_id in list(self.remotePlayers.keys()):
            self.remotePlayers[player_id].toonActor.cleanup()
            self.remotePlayers[player_id].toonActor.removeNode()
            del self.remotePlayers[player_id]
        
        dg = NetDatagram()
        dg.addUint8(3)
        dg.addUint16(newZone)
        self.cWriter.send(dg, self.connection)

    def sendChat(self, text):
        dg = NetDatagram()
        dg.addUint8(4)
        dg.addString(text)
        self.cWriter.send(dg, self.connection)
