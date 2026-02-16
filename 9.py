G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# Walrus Way (zone 23) - Tunnel at (160.26, -80.77, -0.62) facing 90 HPR
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(150, -95, 170, -65, 23, entryPos=(175, -80, 0.025), entryHpr=(90, 0, 0))
# Sleet Street (zone 24) - Tunnel at (-22.77, -253.67, -0.85) facing 23 HPR
# Loading zone in front of tunnel
LoadingZone.define(-35, -265, -10, -242, 24, entryPos=(120, 150, 0.025), entryHpr=(-180, 0, 0))
# Polar Place (zone 25) - Tunnel at (100.11, 152.01, -0.54) facing 150 HPR
# Loading zone in front of tunnel
LoadingZone.define(90, 142, 110, 162, 25, entryPos=(80, 200, 0.025), entryHpr=(-180, 0, 0))

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()