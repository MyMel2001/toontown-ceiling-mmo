G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Loopy Lane (To TTC) (Calculated Sign/Tunnel approx)
LoadingZone.define(30.79, 63.75, 40.79, 73.75, 11)

# Tenor Terrace (4340 -> 15)
LoadingZone.define(-30, -199.95, -20, -189.95, 15)
# Alto Avenue (4127 -> 16)
LoadingZone.define(75, 169.99, 85, 179.99, 16)
# Baritone Boulevard (4222 -> 17)
LoadingZone.define(-160.012, 39.58, -150.012, 49.58, 17)

global isCurrentZone
isCurrentZone = True

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Tenor Terrace
# loadStreet('phase_6/dna/minnies_melody_land_4100.xml', pos=(0,0,0))

# Cogs removed from playground
