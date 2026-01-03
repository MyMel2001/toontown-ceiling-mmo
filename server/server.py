from panda3d.core import *
from direct.task import Task
import sys

class ToontownServer():
    def __init__(self):
        self.cManager = QueuedConnectionManager()
        self.cListener = QueuedConnectionListener(self.cManager, 0)
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager, 0)

        self.activeConnections = []
        self.clients = {} # conn: {dna, pos, zone, name}

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
                'anim': 'neutral'
            }
            print(f"Player {name} logged in at zone {zone}")
            
            # Send current players to new player
            for other_conn, data in self.clients.items():
                if other_conn != conn and data['zone'] == zone:
                    self.sendSpawn(conn, other_conn, data)
            
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
                
                # Spawn in new zone
                for other_conn, data in self.clients.items():
                    if other_conn != conn and data['zone'] == new_zone:
                        self.sendSpawn(conn, other_conn, data)
                        self.sendSpawn(other_conn, conn, self.clients[conn])

        elif msgID == 4: # CHAT
            if conn in self.clients:
                text = it.getString()
                self.broadcastChat(conn, text)

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

server = ToontownServer()
server.run()
