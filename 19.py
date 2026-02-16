G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_1200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DD
base.localAvatar.setPos(-180, -120, 0)

LoadingZone = G["LoadingZone"]
# Back to DD Playground - Tunnel at (-185, -125, 0) facing 0
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(-195, -140, -175, -110, 2, entryPos=(-215, 75, 0.025), entryHpr=(-90, 0, 0))
# Forward to Daisy's Garden (Labyrinth Lane) - Tunnel at (-295, -430, 0) facing -90
# Loading zone in front of tunnel (player approaches from +Y direction)
LoadingZone.define(-310, -445, -280, -415, 21, entryPos=(-35, 5, 0.025), entryHpr=(90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-400, 100, -500, 100)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DD_sz.ogg')
G["music"].setLoop(True)
G["music"].play()