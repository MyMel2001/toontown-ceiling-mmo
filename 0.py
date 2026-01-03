G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Silly Street (11) - Tunnel back to TTC
LoadingZone.define(32, 73.75, 22, 83.75, 11)

# Tenor Terrace (4340 -> 15)
LoadingZone.define(-20, -204.95, -30, -214.95, 15)
# Alto Avenue (4127 -> 16)
LoadingZone.define(85, 164.99, 75, 174.99, 16)
# Baritone Boulevard (4222 -> 17)
LoadingZone.define(-165.01, 49.58, -175.01, 39.58, 17)

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
