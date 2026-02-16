G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_5/dna/toontown_central_2200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Setup tunnel collision to go back to TTC
# Spawn near the tunnel back to TTC in this street
base.localAvatar.setPos(-75, 105, 0)

# Tunnels in Punchline Place
LoadingZone = G["LoadingZone"]
# Back to TTC Playground - Tunnel at (-75, 115, 0) facing -90
# Loading zone in front of tunnel (heading -90 means tunnel faces west, player approaches from east/+X)
LoadingZone.define(-90, 105, -70, 125, 1, entryPos=(-240, 64, 0.025), entryHpr=(-90, 0, 0))
# Forward to Minnie's Melody Land - Tunnel at (-580, -30, 0) facing 180
# Loading zone in front of tunnel (heading 180 means tunnel faces south, player approaches from north/+Y)
LoadingZone.define(-595, -45, -565, -15, 0, entryPos=(-25, -210, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-600, 100, -100, 100)

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_SZ.ogg')
G["music"].setLoop(True)
G["music"].play()