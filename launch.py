from sys import argv
from direct.directbase import DirectStart
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
import datetime
import asyncio
from networking import Networking
from pick_a_toon_menu import PickAToonMenu

base.disableMouse()

G = get_builtins()
G["music"] = loader.loadSfx('phase_3/audio/bgm/c_theme.ogg')
G["music"].setLoop(True)
G["music"].play()

zones = ["Melodyland", "The Central", "Docks", "Garden", "Speedway", "Sellbot HQ Past 2021", "Test Trolley Game", "Toon Hall", "Cashbot HQ", "The Brrrgh", "Dreamland", "Silly Street"]

global duckBody, localAvatar, zID, battleMgr
duckBody = None
localAvatar = None
zID = 1
G["pZID"] = zID

class currentLand:
    currentLandModels = {}

def execfile(path):
    exec(open(str(path)).read())

global breakAllChecks
breakAllChecks = False

def loadZone(zoneId):
    global breakAllChecks, zID
    breakAllChecks = True
    try:
        if zones[zID] in currentLand.currentLandModels:
            currentLand.currentLandModels[zones[zID]].removeNode()
    except:
        pass
    
    old_zID = zID
    zID = zoneId
    G["pZID"] = old_zID
    
    try:
        destroyNPCS()
        if hasattr(base, "cogMgr"):
            for cog in base.cogMgr.cogs:
                cog.cleanup()
            base.cogMgr.cogs = []
        execfile(f"{zID}.py")
        if hasattr(base, "net"):
            base.net.changeZone(zID)
    except Exception as e:
        print(f"Error loading zone {zID}: {e}")

class LoadingZone:
    @staticmethod
    def check(x1, z1, x2, z2, zoneId):
        global breakAllChecks
        while not breakAllChecks:
            if localAvatar:
                x, y = localAvatar.getX(), localAvatar.getY()
                if x2 <= x <= x1 and z1 <= y <= z2:
                    loadZone(zoneId)
                    break
            threading.Event().wait(0.5)

    @staticmethod
    def define(x1, z1, x2, z2, zoneId):
        threading.Thread(target=LoadingZone.check, args=(x1, z1, x2, z2, zoneId), daemon=True).start()

G["LoadingZone"] = LoadingZone

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
    
    movingJumping = 'jump' in loopName
    movingForward = loopName == 'run'
    movingNeutral = loopName == 'neutral'
    if loopName == 'walk':
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
                if isAirborne: setMovementAnimation('running-jump-idle')
                else:
                    if keyMap['forward'] and not movingForward: setMovementAnimation('run')
                    elif keyMap['backward'] and not movingBackward: setMovementAnimation('walk', -1.0)
                    elif (keyMap['left'] or keyMap['right']) and not movingRotation: setMovementAnimation('walk')
        else:
            if not movingJumping:
                if isAirborne: setMovementAnimation('jump-idle')
                elif not movingNeutral: setMovementAnimation('neutral')
    elif keyMap['forward'] == 1:
        if not movingForward and not isAirborne: setMovementAnimation('run')
    elif keyMap['backward'] == 1:
        if not movingBackward and not isAirborne: setMovementAnimation('walk', -1.0)
    elif keyMap['left'] or keyMap['right']:
        if not movingRotation and not isAirborne: setMovementAnimation('walk')
    else:
        if not isAirborne and not movingNeutral: setMovementAnimation('neutral')
    return Task.cont

def start_game(toon_index):
    global duckBody, localAvatar, walkControls
    base.taskMgr.add(battleTriggerTask, "BattleTriggerTask")
    toon = pickAToon(toon_index)
    duckBody = toon.toonActor
    localAvatar = duckBody
    base.localAvatar = localAvatar
    
    head = duckBody.findAllMatches('**/head*')
    nametag = createNametag(toonNameArray[toon_index], (1,1,1,.5), (0,0,1,1))
    nametag.setPos(0,0,2)
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
    
    loadZone(1)
    onScreenDebug.enabled = True
    base.taskMgr.add(handleMovement, 'controlManager')
    base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')
    DirectButton(text=("Back to TTC", "Click", "...", "disabled"), scale=.08, pos=(0, -.5, .5), command=lambda: loadZone(1))

def battleTriggerTask(task):
    if not localAvatar or not hasattr(base, "cogMgr") or not hasattr(base, "battleMgr"):
        return Task.cont
    
    if base.battleMgr.currentBattle:
        return Task.cont

    for cog in base.cogMgr.cogs:
        if (localAvatar.getPos() - cog.node.getPos()).length() < 5:
            base.battleMgr.startBattle(localAvatar, cog)
            break
    return Task.cont

def updateOnScreenDebug(task):
    if localAvatar:
        onScreenDebug.add('Avatar Position', localAvatar.getPos())
        onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
        onScreenDebug.add('Zone', zones[zID])
    return Task.cont

PickAToonMenu(start_game)
base.run()
