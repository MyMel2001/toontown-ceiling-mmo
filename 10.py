G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# To Lullaby Lane (9100)
LoadingZone.define(-60, -200, -70, -190, 26)
# To Pajama Place (9200)
LoadingZone.define(-38.3287, 91.7318, -53.18, 101.799, 27)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Lullaby Lane
# loadStreet('phase_8/dna/donalds_dreamland_9100.xml', pos=(0,0,0))

# Cogs removed from playground
