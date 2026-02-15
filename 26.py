G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_9100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to DL
# G["loadStreet"]('phase_8/dna/donalds_dreamland_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to DL Playground
LoadingZone.define(-5, 30, 15, 50, 10, entryPos=(-65, -195, 0.025), entryHpr=(0, 0, 0))
# Forward to Minnie's Melody Land (Baritone Boulevard)
LoadingZone.define(-104.28, -513.92, -94.28, -503.92, 0, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-150, 100, -550, 100)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_sz.ogg')
G["music"].setLoop(True)
G["music"].play()
