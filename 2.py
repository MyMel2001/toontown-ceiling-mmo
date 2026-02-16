G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

LoadingZone = G["LoadingZone"]
# Barnacle Boulevard (zone 19) - Tunnel at (-198.22, -108.72, -0.975) facing -34 HPR
# Loading zone in front of tunnel (player approaches from heading 146 direction)
LoadingZone.define(-210, -120, -185, -95, 19, entryPos=(160, -50, 0.025), entryHpr=(90, 0, 0))
# Seaweed Street (zone 18) - Tunnel at (-214.99, 74.98, -0.975) facing -90 HPR
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(-230, 65, -200, 85, 18, entryPos=(-185, -125, 0.025), entryHpr=(0, 0, 0))
# Lighthouse Lane (zone 20) - Tunnel at (164.82, -51.14, -0.975) facing 90 HPR
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(150, -65, 180, -40, 20, entryPos=(5, -5, 0.025), entryHpr=(90, 0, 0))
# Outdoor Zone / Trolley (zone 6) - Tunnel at (-53.20, 172.05, 3.28) facing 52 HPR
# Loading zone in front of tunnel
LoadingZone.define(-65, 160, -40, 185, 6, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DOCKS.ogg')
G["music"].setLoop(True)
G["music"].play()