G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Tunnel back to TTC now through Loopy Lane (12)
LoadingZone.define(-188, -118, -208, -98, 12)

# Seaweed Street (1100)
LoadingZone.define(-38.3287, 91.7318, -53.18, 101.799, 18)
# Barnacle Boulevard (1200)
LoadingZone.define(34.5333, -163.679, 24.6789, -148.533, 19)
# Lighthouse Lane (1300)
LoadingZone.define(-127.328, -80.7726, -140.133, -56.2604, 20)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DOCKS.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Seaweed Street
# loadStreet('phase_6/dna/donalds_dock_1100.xml', pos=(0,0,0))

# Cogs removed from playground
