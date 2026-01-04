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
LoadingZone.define(-65.8, 3.2, -55.8, 13.2, 3)
# Forward to TTC (Punchline Place)
LoadingZone.define(673.14, 93.25, 683.14, 103.25, 1)

# Load tunnel back to DG
# G["loadStreet"]('phase_8/dna/daisys_garden_sz.xml', pos=(0,0,0))
# Setup tunnel at end of street to TTC
# G["loadStreet"]('phase_4/dna/toontown_central_sz.xml', pos=(0, 600, 0), zone_key="next_sz")

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()
