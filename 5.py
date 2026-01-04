base.localAvatar.setPos(67.5842,-340.653,100.819)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# Sellbot HQ Tunnel to Daisy's Garden
LoadingZone.define(5, 0, -5, 10, 3)

from direct.actor.Actor import Actor
from panda3d.core import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import Sequence

currentLand.currentLandModels[zones[zID]] = loader.loadModel("phase_9/models/cogHQ/SellbotHQExterior.bam")
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(69,-61,100)
currentLand.currentLandModels[zones[zID]].setHpr(360,0,0)
currentLand.currentLandModels[zones[zID]].setScale(1)

G["music"].stop()
G["music"] = loader.loadSfx('phase_9/audio/bgm/PLEASEDONTMAKEMEGOSADAGAIN.ogg')
G["music"].setLoop(True)
G["music"].play()

# Cogs removed from Sellbot HQ area (treated as playground here)

wall = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wall.reparentTo(currentLand.currentLandModels[zones[zID]])
wall.setPos(76.670,-126.234,110.096)
wall.setHpr(360,0,0)
wall.setScale(3)

wall2 = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wall2.reparentTo(currentLand.currentLandModels[zones[zID]])
wall2.setPos(53.670,-126.234,110.096)
wall2.setHpr(360,0,0)
wall2.setScale(3)

wall3 = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wall3.reparentTo(currentLand.currentLandModels[zones[zID]])
wall3.setPos(39.670,-126.234,110.096)
wall3.setHpr(360,0,0)
wall3.setScale(3)

wall4 = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wall4.reparentTo(currentLand.currentLandModels[zones[zID]])
wall4.setPos(27.670,-126.234,110.096)
wall4.setHpr(360,0,0)
wall4.setScale(3)

wall5 = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wall5.reparentTo(currentLand.currentLandModels[zones[zID]])
wall5.setPos(16.670,-126.234,110.096)
wall5.setHpr(360,0,0)
wall5.setScale(3)

wall6 = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wall6.reparentTo(currentLand.currentLandModels[zones[zID]])
wall6.setPos(3.670,-126.234,110.096)
wall6.setHpr(360,0,0)
wall6.setScale(3)

wall99 = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wall99.reparentTo(currentLand.currentLandModels[zones[zID]])
wall99.setPos(104.657,-102.151,110.096)
wall99.setHpr(360,0,0)
wall99.setScale(2)

lobby = loader.loadModel("phase_9/models/cogHQ/SellbotHQLobby.bam")
lobby.reparentTo(currentLand.currentLandModels[zones[zID]])
lobby.setPos(78,80,86.5)
lobby.setHpr(177.706,0,0)
lobby.setScale(1)

arrow = loader.loadModel('phase_4/models/minigames/toonblitz_game_arrow.bam') 
arrow.reparentTo(currentLand.currentLandModels[zones[zID]]) 
arrow.setPos(62,-83,110) 
arrow.setHpr(380,0,0) 
arrow.setScale(2) 

wallin = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wallin.reparentTo(currentLand.currentLandModels[zones[zID]])
wallin.setPos(49,-77,110)
wallin.setHpr(989.538,0,0)
wallin.setScale(1.4)

wallin2 = loader.loadModel("phase_11/models/lawbotHQ/LB_wall_panel.bam")
wallin2.reparentTo(currentLand.currentLandModels[zones[zID]])
wallin2.setPos(97,-98,110)
wallin2.setHpr(1172.597,0,0)
wallin2.setScale(1.7)


train = loader.loadModel("phase_5/models/props/train.bam")
train.reparentTo(currentLand.currentLandModels[zones[zID]])
train.setPos(51,-171,100)
train.setHpr(55,0,0)
train.setScale(1.2)
train.setColor(0.70,0.70,0.70)

train.findAllMatches('**/').setColorScale(25)
shorts=loader.loadTexture("phase_11/maps/LB_WoodPanel2.jpg")
train.findAllMatches('**/').setTexture(shorts, 1)
train.findAllMatches('**/').setTexture(shorts, 1)
train.setColor(0.70,0.70,0.70)



eagle = loader.loadModel("phase_5/models/cogdominium/tt_m_ara_crg_paintingLegalEagle.bam")
eagle.reparentTo(currentLand.currentLandModels[zones[zID]])
eagle.setPos(75.824,22.146,96)
eagle.setHpr(531.669,0,0)
eagle.setScale(1)

mover = loader.loadModel("phase_5/models/cogdominium/tt_m_ara_crg_paintingMoverShaker.bam")
mover.reparentTo(currentLand.currentLandModels[zones[zID]])
mover.setPos(81,158,164)
mover.setHpr(-1.128,0,0)
mover.setScale(2)

table = loader.loadModel("phase_12/models/bossbotHQ/BanquetTableChairs.bam")
table.reparentTo(currentLand.currentLandModels[zones[zID]])
table.setPos(92,54,86)
table.setHpr(0,0,0)
table.setScale(1.1)

shakeroffice = loader.loadModel("phase_5/models/cogdominium/tt_m_ara_crg_penthouse_sell.bam")
shakeroffice.reparentTo(currentLand.currentLandModels[zones[zID]])
shakeroffice.setPos(86,208,114)
shakeroffice.setHpr(-3.636,0,0)
shakeroffice.setScale(1)

magnet = loader.loadModel("phase_5/models/props/magnet.bam")
magnet.reparentTo(currentLand.currentLandModels[zones[zID]])
magnet.setPos(41,105,94)
magnet.setHpr(275,0,0)
magnet.setScale(4.5)

table2 = loader.loadModel("phase_12/models/bossbotHQ/BanquetTableChairs.bam")
table2.reparentTo(currentLand.currentLandModels[zones[zID]])
table2.setPos(61,54,86)
table2.setHpr(0,0,0)
table2.setScale(1.1)

magnet = loader.loadModel("phase_5/models/props/magnet.bam")
magnet.reparentTo(currentLand.currentLandModels[zones[zID]])
magnet.setPos(41,105,94)
magnet.setHpr(275,0,0)
magnet.setScale(4.5)



paint = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint.setPos(74,-299,100)  
paint.setHpr(0,0,0) 
paint.setScale(1.3) 

paint1 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint1.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint1.setPos(74,-290,100)  
paint1.setHpr(0,0,0) 
paint1.setScale(1) 

paint2 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint2.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint2.setPos(74,-284,100)  
paint2.setHpr(0,0,0) 
paint2.setScale(1) 

paint3 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint3.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint3.setPos(74,-269,100)  
paint3.setHpr(0,0,0) 
paint3.setScale(1) 

paint4 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint4.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint4.setPos(74,-263,100)  
paint4.setHpr(0,0,0) 
paint4.setScale(1) 

paint5 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint5.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint5.setPos(74,-258,100)  
paint5.setHpr(0,0,0) 
paint5.setScale(1) 

paint6 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint6.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint6.setPos(74,-253,100)  
paint6.setHpr(0,0,0) 
paint6.setScale(1) 

paint7 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint7.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint7.setPos(74,-247,100)  
paint7.setHpr(0,0,0) 
paint7.setScale(1) 

paint8 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint8.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint8.setPos(74,-242,100)  
paint8.setHpr(0,0,0) 
paint8.setScale(1) 

paint9 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint9.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint9.setPos(74,-237,100)  
paint9.setHpr(0,0,0) 
paint9.setScale(1) 

paint10 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint10.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint10.setPos(74,-232,100)  
paint10.setHpr(0,0,0) 
paint10.setScale(1.3) 

paint11 = loader.loadModel('phase_9/models/cogHQ/PaintMixer.bam') 
paint11.reparentTo(currentLand.currentLandModels[zones[zID]]) 
paint11.setPos(74,-216,100)  
paint11.setHpr(0,0,0) 
paint11.setScale(1.4) 


rexp3 = loader.loadModel('phase_3.5/models/props/explosion.bam')  
rexp3.reparentTo(currentLand.currentLandModels[zones[zID]]) 
rexp3.setPos(69,-246,80)
rexp3.setHpr(50,0,0) 
rexp3.setScale(3)
rexp3.setColor(0.70,0.70,0.70)

rexp34 = loader.loadModel('phase_3.5/models/props/explosion.bam')  
rexp34.reparentTo(currentLand.currentLandModels[zones[zID]]) 
rexp34.setPos(69,-246,80)
rexp34.setHpr(250,0,0) 
rexp34.setScale(3)
rexp34.setColor(0.70,0.70,0.70)

rexp345 = loader.loadModel('phase_3.5/models/props/explosion.bam')  
rexp345.reparentTo(currentLand.currentLandModels[zones[zID]]) 
rexp345.setPos(69,-246,80)
rexp345.setHpr(200,0,0) 
rexp345.setScale(3)
rexp345.setColor(0.70,0.70,0.70)

rexp3456 = loader.loadModel('phase_3.5/models/props/explosion.bam')  
rexp3456.reparentTo(currentLand.currentLandModels[zones[zID]]) 
rexp3456.setPos(69,-246,80)
rexp3456.setHpr(100,0,0) 
rexp3456.setScale(3)
rexp3456.setColor(0.70,0.70,0.70)

piano = loader.loadModel('phase_6/models/props/piano.bam') 
piano.reparentTo(currentLand.currentLandModels[zones[zID]]) 
piano.setPos(123,-176,100)  
piano.setHpr(-391,0,0) 
piano.setScale(3) 

X = loader.loadModel("phase_9/models/cogHQ/Elevator.bam")
X.reparentTo(currentLand.currentLandModels[zones[zID]])
X.setHpr(0,0,0)
X.setPos(-22,-70,310)
X.setColor(0,0,0)

pandaPosInterval22 = X.posInterval(13,Point3(89,260,114),
startPos=Point3(89,260,114))
pandaPosInterval33 = X.posInterval(13,Point3(89,260,150),


startPos=Point3(89,260,114))
pandaHprInterval11 = X.hprInterval(3,Point3(0,0,0),


startHpr=Point3(0, 0, 0))
pandaHprInterval22 = X.hprInterval(3,Point3(0, 0, 0),

startHpr=Point3(0, 0, 0))
pandaPace = Sequence(pandaPosInterval22,
pandaHprInterval11,
pandaPosInterval33,
pandaHprInterval22,
name="pandaPace")
pandaPace.loop()

boss = loader.loadModel("phase_9/models/cogHQ/BossRoomHQ.bam")
boss.reparentTo(currentLand.currentLandModels[zones[zID]])
boss.setPos(114,542,150)
boss.setHpr(-5.548,0,0)
boss.setScale(1)

a = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
a.reparentTo(currentLand.currentLandModels[zones[zID]])
a.setPos(91,267,150)
a.setHpr(-5.548,0,0)
a.setScale(1)

b = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
b.reparentTo(currentLand.currentLandModels[zones[zID]])
b.setPos(91,276,150)
b.setHpr(-5.548,0,0)
b.setScale(1)

c = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
c.reparentTo(currentLand.currentLandModels[zones[zID]])
c.setPos(91,285,150)
c.setHpr(-5.548,0,0)
c.setScale(1)

d = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
d.reparentTo(currentLand.currentLandModels[zones[zID]])
d.setPos(91,296,150)
d.setHpr(-5.548,0,0)
d.setScale(1)


e = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
e.reparentTo(currentLand.currentLandModels[zones[zID]])
e.setPos(91,305,150)
e.setHpr(-5.548,0,0)
e.setScale(1)

f = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
f.reparentTo(currentLand.currentLandModels[zones[zID]])
f.setPos(91,316,150)
f.setHpr(-5.548,0,0)
f.setScale(1)

g = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
g.reparentTo(currentLand.currentLandModels[zones[zID]])
g.setPos(91,325,150)
g.setHpr(-5.548,0,0)
g.setScale(1)

h = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
h.reparentTo(currentLand.currentLandModels[zones[zID]])
h.setPos(91,345,150)
h.setHpr(-5.548,0,0)
h.setScale(3)

i = loader.loadModel("phase_9/models/cogHQ/PaintMixer.bam")
i.reparentTo(currentLand.currentLandModels[zones[zID]])
i.setPos(91,360,146.5)
i.setHpr(-5.548,0,0)
i.setScale(1.5)
