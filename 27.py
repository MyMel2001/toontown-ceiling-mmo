G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_9200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DL
base.localAvatar.setPos(80, 125, 0)

LoadingZone = G["LoadingZone"]
# Back to DL Playground - Tunnel at (80, 130, 0) facing 0
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(70, 120, 90, 140, 10, entryPos=(55, 195, 0.025), entryHpr=(180, 0, 0))
# Forward to Cashbot HQ - Tunnel at (-146.74, -76.49, -0.5) facing -60
# Loading zone in front of tunnel
LoadingZone.define(-160, -90, -135, -65, 8, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-200, 100, -100, 200)

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_sz.ogg')
G["music"].setLoop(True)
G["music"].play()