G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/daisys_garden_5100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Spawn near the tunnel back to DG
base.localAvatar.setPos(-61, 3, 0)

# Tunnels in Elm Street
LoadingZone = G["LoadingZone"]
# Back to DG Playground - Tunnel at (-60.8, 8.2, 0) facing 90
# Loading zone in front of tunnel (player approaches from -X direction)
LoadingZone.define(-75, -2, -46, 18, 3, entryPos=(187, 192, 0.025), entryHpr=(126, 0, 0))
# Forward to TTC (Punchline Place - but actually this goes to a different street)
# Tunnel at (678.14, 98.25, 0) facing -90
LoadingZone.define(668, 88, 688, 108, 12, entryPos=(-75, 115, 0.025), entryHpr=(-90, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-100, 700, -50, 150)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GARDEN_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()