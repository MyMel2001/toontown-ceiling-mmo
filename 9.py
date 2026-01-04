G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# Walrus Way (3126 -> 23)
LoadingZone.define(160.26, -80.77, 150.26, -70.77, 23)
# Sleet Street (3233 -> 24)
LoadingZone.define(-22.77, -253.67, -12.77, -243.67, 24)
# Polar Place (3301 -> 25)
LoadingZone.define(100.11, 152.01, 110.11, 142.01, 25)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Walrus Way
# loadStreet('phase_8/dna/the_burrrgh_3100.xml', pos=(0,0,0))

# Cogs removed from playground
