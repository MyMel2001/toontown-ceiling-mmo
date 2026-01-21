G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Barnacle Boulevard (1101 -> 19) - Tunnel at (-198.22, -108.72, -0.975) facing -34 HPR
# Zone placed in front of tunnel (extending toward +X and -Y)
LoadingZone.define(-215, -120, -185, -98, 19)
# Seaweed Street (1225 -> 18) - Tunnel at (-214.99, 74.98, -0.975) facing -90 HPR
# Zone placed in front of tunnel (extending toward +Y)
LoadingZone.define(-225, 65, -205, 85, 18)
# Lighthouse Lane (1301 -> 20) - Tunnel at (164.82, -51.14, -0.975) facing 90 HPR
# Zone placed in front of tunnel (extending toward -Y)
LoadingZone.define(155, -60, 175, -42, 20)
# Outdoor Zone (6000) - Tunnel at (-53.1974, 172.046, 3.27967) facing 52 HPR
# Zone placed in front of tunnel (extending toward +X and +Y)
LoadingZone.define(-60, 165, -45, 180, 6)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DOCKS.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Seaweed Street
# loadStreet('phase_6/dna/donalds_dock_1100.xml', pos=(0,0,0))

# Cogs removed from playground
