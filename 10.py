G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

breakAllChecks = False
G = get_builtins()
LoadingZone = G["LoadingZone"]
# To TTC
LoadingZone.define(-60, -200, -70, -190, 1)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels

# Cogs removed from playground
