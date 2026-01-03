G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_5/dna/toontown_central_2100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

# Tunnels in Silly Street
LoadingZone = G["LoadingZone"]
# Back to TTC Playground
LoadingZone.define(10, 10, -10, -10, 1)
# Forward to Melodyland Playground
LoadingZone.define(-20, 100, -40, 120, 0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_sz.ogg')
G["music"].setLoop(True)
G["music"].play()

from cog import CogManager
base.cogMgr = CogManager()
base.cogMgr.spawnCog('A', 'phase_4/models/char/suitA-heads.bam', (0, 40, 0), name="Flunky")
