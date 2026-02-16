G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_4100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to MML
base.localAvatar.setPos(-165, 35, 0)

LoadingZone = G["LoadingZone"]
# Back to MML Playground - Tunnel at (-165, 40, 0) facing -90
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(-180, 30, -150, 50, 0, entryPos=(-25, -210, 0.025), entryHpr=(0, 0, 0))
# Forward to TTC (Punchline Place) - Tunnel at (-459.72, 210, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(-475, 200, -445, 220, 12, entryPos=(-75, 115, 0.025), entryHpr=(-90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-500, 100, -50, 300)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_sz.ogg')
G["music"].setLoop(True)
G["music"].play()