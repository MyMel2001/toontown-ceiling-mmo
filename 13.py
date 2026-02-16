G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_5/dna/toontown_central_2300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Setup tunnel collision to go back to TTC
# Spawn near the tunnel back to TTC in this street
base.localAvatar.setPos(0, -10, 0)

# Tunnels in Silly Street
LoadingZone = G["LoadingZone"]
# Back to TTC Playground - Tunnel at (0, 0, 0) facing 90
# Loading zone in front of tunnel (heading 90 means tunnel faces west/-X, player approaches from east/+X)
# Since tunnel is at origin, place zone slightly in +X direction
LoadingZone.define(-5, -15, 15, 5, 1, entryPos=(28, 176, 0.025), entryHpr=(171, 0, 0))
# Forward to Donald's Dock - Tunnel at (780, 90, 0) facing -90
# Loading zone in front of tunnel (heading -90 means tunnel faces east/+X, player approaches from west/-X)
LoadingZone.define(765, 80, 795, 100, 2, entryPos=(165, -51, 0.025), entryHpr=(90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-100, 800, -100, 150)

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_SZ.ogg')
G["music"].setLoop(True)
G["music"].play()