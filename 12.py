G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_5/dna/toontown_central_2200.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to TTC
# G["loadStreet"]('phase_4/dna/toontown_central_sz.xml', pos=(0,0,0))
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Setup tunnel collision to go back to TTC
base.localAvatar.setPos(0, 20, 0)

# Tunnels in Punchline Place
LoadingZone = G["LoadingZone"]
# Back to TTC Playground - Tunnel at (0, 0, 0) facing 180
LoadingZone.define(-10, -10, 10, 10, 1, entryPos=(-45, 106, 0.025), entryHpr=(0, 0, 0))
# Forward to Minnie's Melody Land (end of street)
LoadingZone.define(-585, -35, -575, -25, 0, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-600, 100, -100, 100)

# Setup tunnel at end of street to Donald's Docks
# G["loadStreet"]('phase_6/dna/donalds_dock_sz.xml', pos=(0, 600, 0), zone_key="next_sz")

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_SZ.ogg')
G["music"].setLoop(True)
G["music"].play()
