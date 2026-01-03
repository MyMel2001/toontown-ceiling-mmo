G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_4300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to MML
# G["loadStreet"]('phase_6/dna/minnies_melody_land_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to MML Playground
LoadingZone.define(-5, -5, 5, 5, 0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_sz.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
if not hasattr(base, "cogMgr"):
    base.cogMgr = CogManager()
base.cogMgr.spawnCog('C', 'phase_3.5/models/char/suitC-heads.bam', (0, 40, 0), name="Legal Eagle")
