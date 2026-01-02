currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_4/models/modules/street_full_silly.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_sz.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
base.cogMgr = CogManager()
base.cogMgr.spawnCog('A', 'phase_3.5/models/char/suitA-heads.bam', (0, 40, 0))
