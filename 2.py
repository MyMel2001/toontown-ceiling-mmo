G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

breakAllChecks = False
LoadingZone = G["LoadingZone"]
# Tunnel back to TTC
LoadingZone.define(-188, -118, -208, -98, 1)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DOCKS.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels

# Cogs removed from playground
