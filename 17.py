G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_4300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to MML
# G["loadStreet"]('phase_6/dna/minnies_melody_land_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to MML Playground
LoadingZone.define(689.9, 210, 699.9, 220, 0, entryPos=(-170, 44, 0.025), entryHpr=(-90, 0, 0))
# Forward to Donald's Dreamland (Lullaby Lane)
LoadingZone.define(55, -5, 65, 5, 10, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-50, 800, -100, 300)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_sz.ogg')
G["music"].setLoop(True)
G["music"].play()
