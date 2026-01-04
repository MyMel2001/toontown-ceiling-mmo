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
LoadingZone.define(177.08, 181.78, 187.08, 191.78, 14)
# Labyrinth Lane (5201 -> 21)
LoadingZone.define(-109.48, 282.95, -99.48, 292.95, 21)
# Oak Street (5301 -> 22)
LoadingZone.define(-65.12, -94.82, -55.12, -84.82, 22)
# To Sellbot HQ (Based on neighborhood sign or tunnel in DG)
LoadingZone.define(-15, -15, 15, 15, 5)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively
# Elm Street
# loadStreet('phase_8/dna/daisys_garden_5100.xml', pos=(0,0,0))

# Cogs removed from playground
