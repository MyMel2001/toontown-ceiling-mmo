G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_5300.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DG
base.localAvatar.setPos(-85, -55, 0)

# Tunnels in Oak Street
LoadingZone = G["LoadingZone"]
# Back to DG Playground - Tunnel at (-85, -60, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(-100, -70, -70, -50, 3, entryPos=(-60, -95, 0.025), entryHpr=(0, 0, 0))
# Forward to Sellbot HQ - Tunnel at (-310.95, 315.88, -0.475) facing -180
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(-325, 305, -296, 326, 5, entryPos=(10, -241, 100.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-400, 100, -100, 400)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_sz.ogg')
G["music"].setLoop(True)
G["music"].play()