G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_5200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to DG
# G["loadStreet"]('phase_8/dna/daisys_garden_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to DG Playground
LoadingZone.define(-5, -5, 5, 5, 3)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_sz.ogg')
G["music"].setLoop(True)
G["music"].play()

