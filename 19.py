G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_1200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to DD
# G["loadStreet"]('phase_6/dna/donalds_dock_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to DD Playground
LoadingZone.define(-5, -5, 5, 5, 2)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DD_sz.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
if not hasattr(base, "cogMgr"):
    base.cogMgr = CogManager()
base.cogMgr.spawnCog('B', 'phase_3.5/models/char/suitB-heads.bam', (0, 40, 0), name="Backstabber")
