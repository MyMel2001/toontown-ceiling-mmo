G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_9200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to DL
# G["loadStreet"]('phase_8/dna/donalds_dreamland_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to DL Playground
LoadingZone.define(75, 125, 85, 135, 10, entryPos=(55, 195, 0.025), entryHpr=(180, 0, 0))
# Forward to Cashbot HQ
LoadingZone.define(-151.735, -81.4866, -141.735, -71.4866, 8, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-200, 100, -100, 200)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_sz.ogg')
G["music"].setLoop(True)
G["music"].play()
