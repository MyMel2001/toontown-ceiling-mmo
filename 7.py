from pickAToon import createNPC
from launch import G
currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setHpr(0,0,0)
base.localAvatar.setPos(-29.0326,-6.00595,0.025)
createNPC(['mi', 'ss', False, 'ss', 'l', 'Blue', 'Red', 'Green', 'Red', '2019 Winter Laff-o-lympics Gold Medal', 'Beta Bug Hunter Shorts', 'Beta Bug Hunter Skirt', 'Amber', 'Aqua', None, None, 4, None, None, None, 'Neutral', True, False],-79.1836,31.7583,0.025,630.764,0,0, "Poodletooth")

# Exit back to TTC Playground (near the entrance)
LoadingZone = G["LoadingZone"]
LoadingZone.define(-40, -20, -20, 0, 1)

G["music"].stop()
G["music"] = loader.loadSfx('phase_4/audio/bgm/DrSurleePlsDont.ogg')
G["music"].setLoop(True)
G["music"].play()
