G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

breakAllChecks = False
G = get_builtins()
LoadingZone = G["LoadingZone"]
# To Walrus Way (Coordinates for TTC tunnel in Brrrgh DNA)
LoadingZone.define(165, -75, 155, -85, 1)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()
