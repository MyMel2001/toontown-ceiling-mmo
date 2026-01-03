G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Tunnel back to TTC
# Tunnel back to TTC now goes through Silly Street (11)
LoadingZone.define(27, 81, 13, 67, 11)

# Tenor Terrace (4100)
LoadingZone.define(-18, -203, -32, -217, 15)
# Alto Avenue (4200)
LoadingZone.define(87, 177, 73, 163, 16)
# Baritone Boulevard (4300)
LoadingZone.define(-163, 52, -177, 38, 17)

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
