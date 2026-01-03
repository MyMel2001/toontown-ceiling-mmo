G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_3300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to BR
# G["loadStreet"]('phase_8/dna/the_burrrgh_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to BR Playground
LoadingZone.define(-20, -10, 20, 10, 9)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_sz.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
if not hasattr(base, "cogMgr"):
    base.cogMgr = CogManager()
base.cogMgr.spawnCog('C', 'phase_3.5/models/char/suitC-heads.bam', (0, 40, 0), name="Big Wig")
