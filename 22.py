G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_5300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to DG
# G["loadStreet"]('phase_8/dna/daisys_garden_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to DG Playground
LoadingZone.define(-90, -65, -80, -55, 3, entryPos=(-60, -94, 0.025), entryHpr=(0, 0, 0))
# Forward to Sellbot HQ
LoadingZone.define(-315.947, 310.883, -305.947, 320.883, 5, entryPos=(10, -241, 100.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-400, 100, -100, 400)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_sz.ogg')
G["music"].setLoop(True)
G["music"].play()
