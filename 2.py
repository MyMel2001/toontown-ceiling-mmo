G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Barnacle Boulevard (1101 -> 19)
LoadingZone.define(-193, -103, -203, -113, 19)
# Seaweed Street (1225 -> 18)
LoadingZone.define(-210, 80, -220, 70, 18)
# Lighthouse Lane (1301 -> 20)
LoadingZone.define(169.82, -46.14, 159.82, -56.14, 20)
# Outdoor Zone (6000)
LoadingZone.define(-48, 177, -58, 167, 6)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DOCKS.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Seaweed Street
# loadStreet('phase_6/dna/donalds_dock_1100.xml', pos=(0,0,0))

# Cogs removed from playground
