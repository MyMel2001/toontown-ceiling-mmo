G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_4300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to MML
base.localAvatar.setPos(695, 210, 0)

LoadingZone = G["LoadingZone"]
# Back to MML Playground - Tunnel at (694.9, 215, 0) facing -90
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(680, 200, 710, 230, 0, entryPos=(-170, 44, 0.025), entryHpr=(-90, 0, 0))
# Forward to Donald's Dreamland (Lullaby Lane) - Tunnel at (60, 0, 0) facing 180
# Loading zone in front of tunnel (player approaches from +Y direction)
LoadingZone.define(50, -10, 70, 10, 26, entryPos=(5, 40, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-50, 800, -100, 300)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_sz.ogg')
G["music"].setLoop(True)
G["music"].play()