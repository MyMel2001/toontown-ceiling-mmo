G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_5/dna/toontown_central_2100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Setup tunnel collision to go back to TTC
# Spawn near the tunnel back to TTC in this street
base.localAvatar.setPos(-90, -70, 0)

# Tunnels in Loopy Lane
LoadingZone = G["LoadingZone"]
# Back to TTC Playground - Tunnel at (-90.03, -79.94, 0) facing -90
# Loading zone in front of tunnel (heading -90 means tunnel faces west, player approaches from east/+X)
LoadingZone.define(-100, -90, -80, -70, 1, entryPos=(-68, -203, 0.025), entryHpr=(-31, 0, 0))
# Forward to Daisy's Garden Playground - Tunnel at (-360, -400, 0) facing 180
# Loading zone in front of tunnel (heading 180 means tunnel faces south, player approaches from north/+Y)
LoadingZone.define(-370, -410, -350, -390, 3, entryPos=(-60, -95, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-400, 100, -500, 100)

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_SZ.ogg')
G["music"].setLoop(True)
G["music"].play()