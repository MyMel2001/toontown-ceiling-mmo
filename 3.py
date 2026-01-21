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
# Elm Street (5102 -> 14) - Tunnel at (187.08, 191.78, 3.3) facing 126 HPR
# Zone placed in front of tunnel (extending toward -X and +Y)
LoadingZone.define(200, 205, 220, 230, 14)
# Labyrinth Lane (5201 -> 21) - Tunnel at (-109.48, 292.95, 3.36) facing -130 HPR
# Zone placed in front of tunnel (extending toward +X and -Y)
LoadingZone.define(-120, 305, -100, 285, 21)
# Oak Street (5301 -> 22) - Tunnel at (-60.12, -94.82, -6.63) facing 0 HPR
# Zone placed in front of tunnel (extending toward -Y)
LoadingZone.define(-70, -105, -50, -85, 22)
# To Sellbot HQ - Leave this one alone as requested
# LoadingZone.define(-15, -15, 15, 15, 5)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively
# Elm Street
# loadStreet('phase_8/dna/daisys_garden_5100.xml', pos=(0,0,0))

# Cogs removed from playground
