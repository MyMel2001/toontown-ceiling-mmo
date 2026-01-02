currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_8/models/neighborhoods/the_burrrgh.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
base.cogMgr = CogManager()
base.cogMgr.spawnCog('B', 'phase_3.5/models/char/suitB-heads.bam', (10, 10, 0))
