G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_5100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Setup tunnel collision to go back to DG
base.localAvatar.setPos(0, 20, 0)

# Tunnels in Elm Street
LoadingZone = G["LoadingZone"]
# Back to DG Playground
LoadingZone.define(-5, -5, 5, 5, 3)
# Forward to TTC (Punchline Place)
LoadingZone.define(-5, 595, 5, 605, 1)

# Load tunnel back to DG
# G["loadStreet"]('phase_8/dna/daisys_garden_sz.xml', pos=(0,0,0))
# Setup tunnel at end of street to TTC
# G["loadStreet"]('phase_4/dna/toontown_central_sz.xml', pos=(0, 600, 0), zone_key="next_sz")

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
if not hasattr(base, "cogMgr"):
    base.cogMgr = CogManager()
base.cogMgr.spawnCog('A', 'phase_3.5/models/char/suitA-heads.bam', (0, 40, 0), name="Corporate Raider")
base.cogMgr.spawnCog('B', 'phase_3.5/models/char/suitB-heads.bam', (20, 60, 0), name="Head Hunter")
base.cogMgr.spawnCog('C', 'phase_3.5/models/char/suitC-heads.bam', (-20, 80, 0), name="Backstabber")
