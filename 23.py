G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_3100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to BR
base.localAvatar.setPos(175, -75, 0)

LoadingZone = G["LoadingZone"]
# Back to BR Playground - Tunnel at (175, -80, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(165, -95, 185, -65, 9, entryPos=(160, -81, 0.025), entryHpr=(90, 0, 0))
# Forward to Donald's Dock (Lighthouse Lane) - Tunnel at (440, 210, 0) facing -90
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(425, 200, 455, 220, 20, entryPos=(630, -50, 0.025), entryHpr=(-90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-100, 500, -150, 300)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_sz.ogg')
G["music"].setLoop(True)
G["music"].play()