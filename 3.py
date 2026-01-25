G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
tunnelA = loader.loadModel('phase_6/models/cogHQ/Cog_Tunnel.bam')
tunnelA.reparentTo(currentLand.currentLandModels[zones[zID]])
tunnelA.setPos(0, 0, 0.025)
base.localAvatar.setPos(22.9513,60.1588,0.025)

LoadingZone = G["LoadingZone"]

# Elm Street (zone 14) - Tunnel at (187.08, 191.78, 3.3) facing 126
# Zone placed 5 units in front of tunnel entrance
LoadingZone.define(182, 186, 192, 196, 14, entryPos=(182, 197, 0.025), entryHpr=(306, 0, 0))

# Labyrinth Lane (zone 21) - Tunnel at (-109.48, 292.95, 3.36) facing -130
# Zone placed 5 units in front of tunnel entrance
LoadingZone.define(-114, 287, -104, 297, 21, entryPos=(-104, 292, 0.025), entryHpr=(50, 0, 0))

# Oak Street (zone 22) - Tunnel at (-60.12, -94.82, -6.63) facing 0
# Zone placed 5 units in front of tunnel entrance
LoadingZone.define(-65, -99, -55, -89, 22, entryPos=(-55, -94, 0.025), entryHpr=(180, 0, 0))

# To Sellbot HQ (zone 5)
LoadingZone.define(-20, -20, 20, 20, 5, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively
# Elm Street
# loadStreet('phase_8/dna/daisys_garden_5100.xml', pos=(0,0,0))

# Cogs removed from playground
