G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_5200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DG
base.localAvatar.setPos(-35, 0, 0)

# Tunnels in Labyrinth Lane
LoadingZone = G["LoadingZone"]
# Back to DG Playground - Tunnel at (-35, 5, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(-50, -5, -20, 15, 3, entryPos=(-109, 293, 0.025), entryHpr=(-130, 0, 0))
# Forward to Donald's Dock (Seaweed Street) - Tunnel at (695.05, 84.8, 0) facing -90
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(680, 75, 710, 95, 18, entryPos=(-295, -430, 0.025), entryHpr=(-90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-100, 800, -100, 150)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_sz.ogg')
G["music"].setLoop(True)
G["music"].play()