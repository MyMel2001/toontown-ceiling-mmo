import random
from sys import argv
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
import threading
from thirdparty.nametag.toonNametag import createNametag
from pickAToon import defineToon, destroyNPCS, get_builtins, toonDnaArray, toonNameArray, pickAToon
from thirdparty.createToon.src.toon.ToonDNA import colorsList
import datetime
import asyncio
from networking import Networking
from pick_a_toon_menu import PickAToonMenu
from DNALoader import DNALoader
import os
import math

base = ShowBase()
base.disableMouse()

# Setup Cull Bins
cbm = CullBinManager.getGlobalPtr()
if cbm.findBin('shadow') == -1:
    cbm.addBin('shadow', CullBinManager.BTFixed, 40)
if cbm.findBin('ground') == -1:
    cbm.addBin('ground', CullBinManager.BTFixed, 10)

G = get_builtins()
G["music"] = loader.loadSfx('phase_3/audio/bgm/c_theme.ogg')
G["music"].setLoop(True)
G["music"].play()

# Initialize DNA Loader
dna_loader = DNALoader()
dna_loader.loadStorage('phase_4/dna/storage.xml')
dna_loader.loadStorage('phase_4/dna/storage_TT.xml')
dna_loader.loadStorage('phase_4/dna/storage_TT_sz.xml')
dna_loader.loadStorage('phase_5/dna/storage_town.xml')
dna_loader.loadStorage('phase_5/dna/storage_TT_town.xml')
dna_loader.loadStorage('phase_6/dna/storage_DD.xml')
dna_loader.loadStorage('phase_6/dna/storage_DD_sz.xml')
dna_loader.loadStorage('phase_6/dna/storage_DD_town.xml')
dna_loader.loadStorage('phase_6/dna/storage_MM.xml')
dna_loader.loadStorage('phase_6/dna/storage_MM_sz.xml')
dna_loader.loadStorage('phase_6/dna/storage_MM_town.xml')
dna_loader.loadStorage('phase_6/dna/storage_GS.xml')
dna_loader.loadStorage('phase_6/dna/storage_GS_sz.xml')
dna_loader.loadStorage('phase_8/dna/storage_DG.xml')
dna_loader.loadStorage('phase_8/dna/storage_DG_sz.xml')
dna_loader.loadStorage('phase_8/dna/storage_DG_town.xml')
dna_loader.loadStorage('phase_8/dna/storage_BR.xml')
dna_loader.loadStorage('phase_8/dna/storage_BR_sz.xml')
dna_loader.loadStorage('phase_8/dna/storage_BR_town.xml')
dna_loader.loadStorage('phase_8/dna/storage_DL.xml')
dna_loader.loadStorage('phase_8/dna/storage_DL_sz.xml')
dna_loader.loadStorage('phase_8/dna/storage_DL_town.xml')
dna_loader.loadStorage('phase_12/dna/storage_CC_sz.xml')
G["dna_loader"] = dna_loader

zones = ["Melodyland", "The Central", "Docks", "Garden", "Speedway", "Sellbot HQ Past 2021", "Test Trolley Game", "Toon Hall", "Cashbot HQ", "The Brrrgh", "Dreamland", "Silly Street", "Loopy Lane", "Punchline Place", "Elm Street", "Tenor Terrace", "Alto Avenue", "Baritone Boulevard", "Seaweed Street", "Barnacle Boulevard", "Lighthouse Lane", "Labyrinth Lane", "Maple Street", "Walrus Way", "Sleet Street", "Polar Place", "Lullaby Lane", "Pajama Place"]

def getZoneName(zoneId):
    if zoneId < len(zones):
        return zones[zoneId]
    return f"Zone {zoneId}"

def getPlaygroundForZone(zoneId):
    # Mapping streets and special zones to their respective playgrounds
    street_to_playground = {
        11: 1, 12: 1, 13: 1, # TTC Streets
        14: 2, 18: 2, 19: 2, 20: 2, # DD Streets
        15: 0, 16: 0, 17: 0, # MM Streets
        21: 3, 22: 3, # DG Streets
        23: 9, 24: 9, 25: 9, # BR Streets
        26: 10, 27: 10, # DL Streets
        5: 3, # Sellbot HQ -> DG
        8: 10, # Cashbot HQ -> DL
    }
    # If it's already a playground (0-4, 9, 10), return it.
    if zoneId in [0, 1, 2, 3, 4, 9, 10]:
        return zoneId
    return street_to_playground.get(zoneId, 1)

base.getPlaygroundForZone = getPlaygroundForZone

global duckBody, localAvatar, zID, battleMgr, pickedToonArray
duckBody = None
localAvatar = None
zID = 1
G["pZID"] = zID

class currentLand:
    currentLandModels = {}

def execfile(path):
    with open(str(path)) as f:
        exec(f.read(), globals())

class LoadingZoneManager:
    def __init__(self):
        self.zones = []
        base.taskMgr.add(self.update, "loadingZoneManagerUpdate")

    def addZone(self, x1, y1, x2, y2, zoneId):
        minX = min(x1, x2)
        maxX = max(x1, x2)
        minY = min(y1, y2)
        maxY = max(y1, y2)
        self.zones.append((minX, minY, maxX, maxY, zoneId))

    def clear(self):
        self.zones = []

    def update(self, task):
        if localAvatar:
            x, y = localAvatar.getX(), localAvatar.getY()
            for z in list(self.zones):
                minX, minY, maxX, maxY, zoneId = z
                if minX <= x <= maxX and minY <= y <= maxY:
                    self.clear()
                    loadZone(zoneId)
                    break
        return Task.cont

loadingZoneMgr = LoadingZoneManager()
G["loadingZoneMgr"] = loadingZoneMgr

def loadZone(zoneId):
    global breakAllChecks, zID
    breakAllChecks = True
    
    # Clear ice creams
    if hasattr(base, "iceCreams"):
        for ic in base.iceCreams:
            ic.removeNode()
    base.iceCreams = []
    
    # Clear loading queue
    loading_queue.clear()
    
    # Clean up managed entities
    destroyNPCS()
    if hasattr(base, "battleMgr") and base.battleMgr.currentBattle:
        base.battleMgr.currentBattle.cleanup()
    if hasattr(base, "cogMgr"):
        base.cogMgr.cleanup()
    
    if hasattr(base, "net"):
        base.net.changeZone(zoneId)
        
    # Aggressively cleanup everything else in render EXCEPT the local avatar
    if duckBody:
        duckBody.detachNode()
    
    for child in list(render.getChildren()):
        child.removeNode()
    
    if duckBody:
        duckBody.reparentTo(render)
    
    currentLand.currentLandModels.clear()
    
    old_zID = zID
    zID = zoneId
    base.zID = zID
    G["pZID"] = old_zID
    
    try:
        execfile(f"{zID}.py")
        spawnIceCreams()
    except Exception as e:
        print(f"Error loading zone {zID}: {e}")
G["loadZone"] = loadZone
base.loadZone = loadZone

def spawnOneIceCream(task=None):
    if not hasattr(base, "iceCreams"):
        base.iceCreams = []
        
    playground_zones = [0, 1, 2, 3, 4, 9, 10]
    if zID in playground_zones and len(base.iceCreams) < 10:
        # Spawn ice creams further away from the center to avoid immediate pickup on teleport
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(20, 100)
        x = math.cos(angle) * dist
        y = math.sin(angle) * dist
        ic = loader.loadModel("phase_4/models/props/icecream.bam")
        ic.reparentTo(render)
        ic.setPos(x, y, 0.5)
        ic.setScale(1.5)
        base.iceCreams.append(ic)
    
    return Task.again if task else None

def spawnIceCreams():
    if not hasattr(base, "iceCreams"):
        base.iceCreams = []
    
    # Randomly spawn ice cream cones in playgrounds
    playground_zones = [0, 1, 2, 3, 4, 9, 10]
    if zID in playground_zones:
        for i in range(10):
            spawnOneIceCream()

def iceCreamTask(task):
    if localAvatar and localAvatar.hp > 0:
        for ic in list(base.iceCreams):
            if ic.isEmpty():
                continue
            if (localAvatar.getPos() - ic.getPos()).length() < 5.0:
                print("Picked up Ice Cream!")
                ic.removeNode()
                base.iceCreams.remove(ic)
                localAvatar.hp = min(localAvatar.maxHp, localAvatar.hp + random.randint(1, 6))
                if hasattr(base, "laffMeter"):
                    base.laffMeter.updateLaff()
    return Task.cont

class LaffMeter(DirectFrame):
    def __init__(self, dna):
        DirectFrame.__init__(self, relief=None, scale=0.15, pos=(-1.1, 0, -0.8))
        self.dna = dna
        self.container = loader.loadModel("phase_3/models/gui/laff_o_meter.bam")
        self.container.reparentTo(self)
        
        # Hide all heads
        for head in self.container.find("**/heads").getChildren():
            head.hide()
            
        species = dna[0]
        mapping = {
            'b': 'bearhead', 'ca': 'cathead', 'd': 'doghead', 'du': 'duckhead',
            'h': 'horsehead', 'mo': 'monkeyhead', 'mi': 'mousehead', 'p': 'pighead',
            'r': 'bunnyhead', 'ri': 'bunnyhead', 'cr': 'bearhead', 'de': 'bearhead'
        }
        headName = mapping.get(species, 'doghead')
        self.head = self.container.find(f"**/heads/{headName}")
        if not self.head.isEmpty():
            self.head.show()
            self.head.setColor(colorsList.get(dna[5], (1,1,1,1)))
            
        self.eyes = self.container.find("**/eyes")
        self.smile = self.container.find("**/smile")
        self.open_smile = self.container.find("**/open_smile")
        self.frown = self.container.find("**/frown")
        self.teeth = self.container.find("**/teeth")
        
        self.hpLabel = DirectLabel(parent=self, text="", scale=0.6, pos=(0, 0, 0.1), 
                                   text_fg=(0,1,0,1), frameColor=(0,0,0,0))
        self.isSad = False
        self.lastHp = -1
        self.lastMaxHp = -1
        base.taskMgr.add(self.updateTask, "updateLaffTask")
        self.updateLaff()

    def updateTask(self, task):
        if localAvatar:
            if localAvatar.hp != self.lastHp or localAvatar.maxHp != self.lastMaxHp:
                self.updateLaff()
        return Task.cont

    def updateLaff(self):
        if not localAvatar: return
        if localAvatar.hp < 0:
            localAvatar.hp = 0
        hp = localAvatar.hp
        maxHp = localAvatar.maxHp
        self.lastHp = hp
        self.lastMaxHp = maxHp
        self.hpLabel['text'] = f"{int(hp)} {int(maxHp)}"
        
        if hp <= 0:
            self.hpLabel['text_fg'] = (1, 0, 0, 1) # Red
            if not self.isSad:
                self.isSad = True
                # Set HP to 0 explicitly to ensure it stays 0 during teleport
                localAvatar.hp = 0
                Sequence(
                    Wait(0.5),
                    Func(base.loadZone, getPlaygroundForZone(zID)),
                    Wait(0.1),
                    Func(self.healAfterSad)
                ).start()
        else:
            self.hpLabel['text_fg'] = (0, 1, 0, 1) # Green
            self.isSad = False
        
        self.updateLaffMeter()

    def healAfterSad(self):
        # In Toontown, you are healed to 1 HP after going sad and reaching playground
        if localAvatar.hp <= 0:
            localAvatar.hp = 1
            self.updateLaff()

    def updateLaffMeter(self):
        if not localAvatar: return
        hp = localAvatar.hp
        maxHp = localAvatar.maxHp
        ratio = float(hp) / maxHp if maxHp > 0 else 0
        
        self.eyes.show()
        self.smile.hide()
        self.open_smile.hide()
        self.frown.hide()
        self.teeth.hide()
        
        if ratio > 0.7:
            self.open_smile.show()
            self.teeth.show()
        elif ratio > 0.3:
            self.smile.show()
        else:
            self.frown.show()

class LoadingZone:
    @staticmethod
    def define(x1, y1, x2, y2, zoneId):
        loadingZoneMgr.addZone(x1, y1, x2, y2, zoneId)

G["LoadingZone"] = LoadingZone

loading_queue = []
is_loading = False

def process_loading_queue(task):
    global is_loading
    if not loading_queue:
        is_loading = False
        return Task.done
    
    is_loading = True
    load_func, args = loading_queue.pop(0)
    load_func(*args)
    
    # Schedule next load with a small delay for "progressive" feel
    base.taskMgr.doMethodLater(0.5, process_loading_queue, "process_loading_queue")
    return Task.done

def queue_load(func, *args):
    loading_queue.append((func, args))
    if not is_loading:
        base.taskMgr.add(process_loading_queue, "process_loading_queue")

def actual_load_street(path, pos, hpr, zone_key=None):
    print("Unloading previous place....")
    # Aggressively cleanup everything else in render EXCEPT the local avatar
    if duckBody:
        duckBody.detachNode()
    
    for child in list(render.getChildren()):
        child.removeNode()
    
    if duckBody:
        duckBody.reparentTo(render)
        duckBody.setScale(1,1,1)
    
    currentLand.currentLandModels.clear()
    print(f"Progressive loading: {path}")
    if path.endswith('.xml'):
        street = dna_loader.loadDNA(path)
    else:
        street = loader.loadModel(path)
    if street:
        if zone_key:
            currentLand.currentLandModels[zone_key] = street
        else:
            # If no key, we should still track it to remove it later
            # Using path as a fallback key
            currentLand.currentLandModels[path] = street
        street.reparentTo(render)
        street.setPos(pos)
        street.setHpr(hpr)

def loadStreet(path, pos=(0, 0, 0), hpr=(0, 0, 0), zone_key=None):
    queue_load(actual_load_street, path, pos, hpr, zone_key)
    return None # Return None because it's async now

G["loadStreet"] = loadStreet
G["queue_load"] = queue_load

def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        inputState.set(input, active)
        keyMap[keyMapName] = 1 if active else 0
    base.accept(key, watchKey, [True])
    base.accept(key+'-up', watchKey, [False])

keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')

movingNeutral, movingForward = False, False
movingRotation, movingBackward = False, False
movingJumping = False

def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral, movingForward, movingRotation, movingBackward, movingJumping
    if not duckBody: return
    
    movingJumping = 'Jump' in loopName
    movingForward = loopName == 'Run'
    movingNeutral = loopName == 'Neutral'
    if loopName == 'Walk':
        if playRate == -1.0:
            movingBackward, movingRotation = True, False
        else:
            movingBackward, movingRotation = False, True
    else:
        movingBackward = movingRotation = False
        
    duckBody.loop(loopName)
    if playRate != 1.0:
        duckBody.setPlayRate(playRate, loopName)

def handleMovement(task):
    if not duckBody or not duckBody.physControls: return Task.cont
    
    isAirborne = duckBody.physControls.isAirborne
    
    if keyMap['control'] == 1:
        if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
            if not movingJumping:
                if isAirborne: setMovementAnimation('Running Jump')
                else:
                    if keyMap['forward'] and not movingForward: setMovementAnimation('Run')
                    elif keyMap['backward'] and not movingBackward: setMovementAnimation('Walk', -1.0)
                    elif (keyMap['left'] or keyMap['right']) and not movingRotation: setMovementAnimation('Walk')
        else:
            if not movingJumping:
                if isAirborne: setMovementAnimation('Jump')
                elif not movingNeutral: setMovementAnimation('Neutral')
    elif keyMap['forward'] == 1:
        if not movingForward and not isAirborne: setMovementAnimation('Run')
    elif keyMap['backward'] == 1:
        if not movingBackward and not isAirborne: setMovementAnimation('Walk', -1.0)
    elif keyMap['left'] or keyMap['right']:
        if not movingRotation and not isAirborne: setMovementAnimation('Walk')
    else:
        if not isAirborne and not movingNeutral: setMovementAnimation('Neutral')
    return Task.cont

def start_game(toon_index):
    global duckBody, localAvatar, walkControls
    base.taskMgr.add(battleTriggerTask, "BattleTriggerTask")
    base.taskMgr.add(iceCreamTask, "IceCreamTask")
    base.taskMgr.doMethodLater(15, spawnOneIceCream, "respawnIceCreamTask")
    toon = pickAToon(toon_index)
    duckBody = toon.toonActor
    localAvatar = duckBody
    base.localAvatar = localAvatar
    
    localAvatar.maxHp = 64
    localAvatar.hp = 64
    
    base.laffMeter = LaffMeter(toonDnaArray[toon_index])
    
    head_joint = duckBody.find('**/def_head')
    if head_joint.isEmpty():
        head_joint = duckBody.find('**/joint_head')
    
    nametag = createNametag(toonNameArray[toon_index], (1,1,1,.5), (0,0,1,1))
    nametag.setPos(0,0,3.2)
    nametag.setScale(.5, 0, .5)
    if not head_joint.isEmpty():
        nametag.reparentTo(head_joint)
    else:
        head = duckBody.findAllMatches('**/head*')
        if head:
            nametag.reparentTo(head[0])

    duckBody.reparentTo(render)
    offset = 3.2375
    base.camera.reparentTo(duckBody)
    base.camera.setPos(0, -10.0 - offset, offset)
    
    base.cTrav = CollisionTraverser()
    walkControls = GravityWalker(legacyLifter=True)
    walkControls.setWallBitMask(BitMask32(1))
    walkControls.setFloorBitMask(BitMask32(2))
    walkControls.setWalkSpeed(16.0, 24.0, 8.0, 80.0)
    walkControls.initializeCollisions(base.cTrav, duckBody, floorOffset=0.025, reach=4.0)
    walkControls.setAirborneHeightFunc(lambda: offset + 0.025)
    walkControls.enableAvatarControls()
    duckBody.physControls = walkControls
    
    base.net = Networking()
    base.net.login(toonNameArray[toon_index], toonDnaArray[toon_index], zID, duckBody.getPos(), duckBody.getHpr())
    
    from chat import ChatManager
    base.chatMgr = ChatManager()

    from battle import BattleManager
    base.battleMgr = BattleManager()

    from cog import CogManager
    base.cogMgr = CogManager()
    
    loadZone(1)
    onScreenDebug.enabled = True
    base.taskMgr.add(handleMovement, 'controlManager')
    base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')
    DirectButton(text=("Back to previous safezone", "Click", "...", "disabled"), scale=.08, pos=(0, -.5, .5), command=lambda: loadZone(1))

def battleTriggerTask(task):
    if not localAvatar or localAvatar.hp <= 0 or not hasattr(base, "cogMgr") or not hasattr(base, "battleMgr"):
        return Task.cont
    
    if base.battleMgr.currentBattle:
        return Task.cont

    for cog in base.cogMgr.cogs.values():
        if cog.node.isEmpty():
            continue
        if (localAvatar.getPos() - cog.node.getPos()).length() < 5:
            base.battleMgr.startBattle(localAvatar, cog)
            break
    return Task.cont

def updateOnScreenDebug(task):
    if localAvatar and os.getenv("DEBUG") == "True":
        onScreenDebug.add('Avatar Position', localAvatar.getPos())
        onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
        onScreenDebug.add('Zone', zones[zID])
    return Task.cont

PickAToonMenu(start_game)
base.run()
