G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_1100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DD
base.localAvatar.setPos(155, -45, 0)

LoadingZone = G["LoadingZone"]
# Back to DD Playground - Tunnel at (160, -50, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(145, -60, 175, -40, 2, entryPos=(-198, -108, 0.025), entryHpr=(-34, 0, 0))
# Forward to TTC (Silly Street) - Tunnel at (370, -30, 0) facing 0
# Loading zone in front of tunnel (player approaches from -Y direction, heading 0 faces +Y)
LoadingZone.define(360, -45, 380, -15, 13, entryPos=(5, -5, 0.025), entryHpr=(90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-50, 450, -100, 100)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DD_sz.ogg')
G["music"].setLoop(True)
G["music"].play()