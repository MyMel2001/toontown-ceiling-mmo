G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_3300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to BR
base.localAvatar.setPos(80, 195, 0)

LoadingZone = G["LoadingZone"]
# Back to BR Playground - Tunnel at (80, 200, 0) facing -180
# Loading zone in front of tunnel (player approaches from +Y direction)
LoadingZone.define(70, 190, 90, 210, 9, entryPos=(100, 152, 0.025), entryHpr=(150, 0, 0))
# Forward to Lawbot HQ - Tunnel at (205.29, 370, -0.414) facing -90
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(195, 360, 215, 380, 11, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-50, 300, -50, 450)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_sz.ogg')
G["music"].setLoop(True)
G["music"].play()