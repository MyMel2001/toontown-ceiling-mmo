G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

breakAllChecks = False
G = get_builtins()
LoadingZone = G["LoadingZone"]
# Tunnel back to TTC
# Tunnel back to TTC now goes through Silly Street (11)
LoadingZone.define(12, 107, -8, 112, 11)

global isCurrentZone
isCurrentZone = True

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Cogs removed from playground
