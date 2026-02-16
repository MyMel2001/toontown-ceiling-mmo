G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_3200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to BR
base.localAvatar.setPos(120, 145, 0)

LoadingZone = G["LoadingZone"]
# Back to BR Playground - Tunnel at (120, 150, 0) facing -180
# Loading zone in front of tunnel (player approaches from +Y direction)
LoadingZone.define(110, 140, 130, 160, 9, entryPos=(-23, -254, 0.025), entryHpr=(23, 0, 0))
# Forward to Minnie's Melody Land (Alto Avenue) - Tunnel at (155, 370, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(145, 360, 165, 380, 16, entryPos=(140, 400, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-100, 300, -50, 450)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_sz.ogg')
G["music"].setLoop(True)
G["music"].play()