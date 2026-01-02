G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
tunnelA = loader.loadModel('phase_6/models/cogHQ/Cog_Tunnel.bam')
tunnelA.reparentTo(currentLand.currentLandModels[zones[zID]])
tunnelA.setPos(0, 0, 0.025)
base.localAvatar.setPos(22.9513,60.1588,0.025)

breakAllChecks = False
G = get_builtins()
LoadingZone = G["LoadingZone"]
# To TTC
LoadingZone.define(192, 187, 182, 197, 1)
# To Sellbot HQ
LoadingZone.define(3.6083, -1.4502, -14.5347, 9.84779, 5)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()
