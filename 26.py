G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_9100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DL
base.localAvatar.setPos(5, 35, 0)

LoadingZone = G["LoadingZone"]
# Back to DL Playground - Tunnel at (5, 40, 0) facing 0
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(-5, 25, 15, 55, 10, entryPos=(-65, -195, 0.025), entryHpr=(0, 0, 0))
# Forward to Minnie's Melody Land (Baritone Boulevard) - Tunnel at (-99.28, -508.92, 0) facing 180
# Loading zone in front of tunnel (player approaches from +Y direction)
LoadingZone.define(-115, -520, -85, -498, 17, entryPos=(60, 0, 0.025), entryHpr=(180, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-150, 100, -550, 100)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_sz.ogg')
G["music"].setLoop(True)
G["music"].play()