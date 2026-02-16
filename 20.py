G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_1300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DD
base.localAvatar.setPos(-5, -5, 0)

LoadingZone = G["LoadingZone"]
# Back to DD Playground - Tunnel at (0, 0, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(-10, -10, 10, 10, 2, entryPos=(165, -51, 0.025), entryHpr=(90, 0, 0))
# Forward to The Brrrgh (Walrus Way) - Tunnel at (630, -50, 0) facing -90
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(615, -65, 645, -35, 23, entryPos=(175, -80, 0.025), entryHpr=(90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-50, 700, -100, 100)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DD_sz.ogg')
G["music"].setLoop(True)
G["music"].play()