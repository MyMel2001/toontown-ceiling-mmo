currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_6/models/neighborhoods/donalds_dock.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DOCKS.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
base.cogMgr = CogManager()
base.cogMgr.spawnCog('C', 'phase_3.5/models/char/suitC-heads.bam', (40, 0, 0))
