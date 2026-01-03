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
# Elm Street (5102 -> 14)
LoadingZone.define(182.08, 186.78, 192.08, 196.78, 14)
# Labyrinth Lane (5201 -> 21)
LoadingZone.define(-104.48, 287.95, -114.48, 297.95, 21)
# Oak Street (5301 -> 22)
LoadingZone.define(-55.12, -89.82, -65.12, -99.82, 22)
# To Sellbot HQ
LoadingZone.define(5, -5, -5, 5, 5)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively
# Elm Street
# loadStreet('phase_8/dna/daisys_garden_5100.xml', pos=(0,0,0))

# Cogs removed from playground
