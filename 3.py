G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

LoadingZone = G["LoadingZone"]

# Elm Street (zone 14) - Tunnel at (187.08, 191.78, 3.3) facing 126
# Loading zone in front of tunnel (player approaches from opposite direction)
LoadingZone.define(177, 182, 197, 202, 14, entryPos=(-61, 8, 0.025), entryHpr=(90, 0, 0))

# Labyrinth Lane (zone 21) - Tunnel at (-109.48, 292.95, 3.36) facing -130
# Loading zone in front of tunnel
LoadingZone.define(-120, 283, -99, 303, 21, entryPos=(-35, 5, 0.025), entryHpr=(90, 0, 0))

# Oak Street (zone 22) - Tunnel at (-60.12, -94.82, -6.63) facing 0
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(-70, -105, -50, -85, 22, entryPos=(-85, -60, 0.025), entryHpr=(90, 0, 0))

# To Sellbot HQ (zone 5) - Not in DNA tunnel list, using approximate position
# Zone placed at Sellbot HQ entrance area
LoadingZone.define(5, -241, 15, -231, 5, entryPos=(10, -241, 100.025), entryHpr=(0, 0, 0))

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()