G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_4200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to MML
base.localAvatar.setPos(80, 160, 0)

LoadingZone = G["LoadingZone"]
# Back to MML Playground - Tunnel at (80, 165, 0) facing 180
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(70, 155, 90, 175, 0, entryPos=(80, 170, 0.025), entryHpr=(180, 0, 0))
# Forward to The Brrrgh (Sleet Street) - Tunnel at (140, 400, 0) facing 0
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(130, 390, 150, 410, 24, entryPos=(120, 150, 0.025), entryHpr=(-180, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-100, 200, -50, 450)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_sz.ogg')
G["music"].setLoop(True)
G["music"].play()