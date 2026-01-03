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
# To Punchline Place/TTC (through Elm Street 14)
LoadingZone.define(192, 187, 182, 197, 14)

# Labyrinth Lane (5200)
LoadingZone.define(34.5333, -163.679, 24.6789, -148.533, 21)
# Maple Street (5300)
LoadingZone.define(-38.3287, 91.7318, -53.18, 101.799, 22)
# To Sellbot HQ
LoadingZone.define(3.6083, -1.4502, -14.5347, 9.84779, 5)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively
# Elm Street
# loadStreet('phase_8/dna/daisys_garden_5100.xml', pos=(0,0,0))

# Cogs removed from playground
