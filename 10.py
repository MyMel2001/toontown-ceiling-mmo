G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# Lullaby Lane (9101 -> 26)
LoadingZone.define(-60.2, -190.2, -70.2, -200.2, 26)
# Pajama Place (9201 -> 27)
LoadingZone.define(60, 190, 50, 200, 27)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Lullaby Lane
# loadStreet('phase_8/dna/donalds_dreamland_9100.xml', pos=(0,0,0))

# Cogs removed from playground
