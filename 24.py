G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_3200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to BR
# G["loadStreet"]('phase_8/dna/the_burrrgh_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to BR Playground
LoadingZone.define(115, 145, 125, 155, 9)
# Forward to Minnie's Melody Land (Alto Avenue)
LoadingZone.define(150, 365, 160, 375, 0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_sz.ogg')
G["music"].setLoop(True)
G["music"].play()
