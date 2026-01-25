G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_5/dna/toontown_central_2300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to TTC
# G["loadStreet"]('phase_4/dna/toontown_central_sz.xml', pos=(0,0,0))
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Setup tunnel collision to go back to TTC
base.localAvatar.setPos(0, 20, 0)

# Tunnels in Silly Street
LoadingZone = G["LoadingZone"]
# Back to TTC Playground - Tunnel at (0, 0, 0) facing 180
LoadingZone.define(-10, -10, 10, 10, 1, entryPos=(30, -146, 0.025), entryHpr=(180, 0, 0))
# Forward to Donald's Dock (end of street)
LoadingZone.define(775, 85, 785, 95, 2, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

# Setup tunnel at end of street to Daisy's Garden
# G["loadStreet"]('phase_8/dna/daisys_garden_sz.xml', pos=(0, 600, 0), zone_key="next_sz")

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_SZ.ogg')
G["music"].setLoop(True)
G["music"].play()
