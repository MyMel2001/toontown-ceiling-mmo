from direct.actor.Actor import Actor
from panda3d.core import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import Sequence
import threading

currentLand.currentLandModels[zones[zID]] = loader.loadModel("phase_4/models/minigames/maze_4player.bam")
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setHpr(180,0,0)
currentLand.currentLandModels[zones[zID]].setPos(0,0,0)
base.localAvatar.setPos(0,0,0)
currentLand.currentLandModels[zones[zID]].setScale(12)

G["music"].stop()
G["music"] = loader.loadSfx('phase_4/audio/bgm/EE_DiesandPies.ogg')
G["music"].setLoop(True)
G["music"].play()

def sleepThenBackToPlayground():
    import time
    time.sleep(43)
    #loadZone(G["pZID"])
    loadZone(1)

pgthr = threading.Thread(target=sleepThenBackToPlayground, args=(), kwargs={})
pgthr.start()
