G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# To Walrus Way (3100)
LoadingZone.define(167, -74, 153, -88, 23)
# To Sleet Street (3200)
LoadingZone.define(-16, -247, -30, -261, 24)
# To Polar Place (3300)
LoadingZone.define(107, 159, 93, 145, 25)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Walrus Way
# loadStreet('phase_8/dna/the_burrrgh_3100.xml', pos=(0,0,0))

# Cogs removed from playground
