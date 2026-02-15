G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_5/dna/toontown_central_2100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to TTC
# G["loadStreet"]('phase_4/dna/toontown_central_sz.xml', pos=(0,0,0))
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Setup tunnel collision to go back to TTC
base.localAvatar.setPos(0, 20, 0)

# Tunnels in Loopy Lane
LoadingZone = G["LoadingZone"]
# Back to TTC Playground - Tunnel at (0, 0, 0) facing 180
# Corrected TTC exit position: TTC tunnel is at (-146.117, -4.0677) roughly
LoadingZone.define(-10, -10, 10, 10, 1, entryPos=(-140, 4, 0.025), entryHpr=(90, 0, 0))
# Forward to Daisy's Garden Playground (end of street)
LoadingZone.define(-365, -405, -355, -395, 3, entryPos=(22, 60, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-400, 100, -500, 100)

# Setup tunnel at end of street to Melodyland
# Coordinates for MML tunnel in TTC 2100 are approx (0, 600, 0)
# G["loadStreet"]('phase_6/dna/minnies_melody_land_sz.xml', pos=(0, 600, 0), zone_key="next_sz")

G["music"].stop()
G["music"] = loader.loadSfx('phase_3.5/audio/bgm/TC_SZ.ogg')
G["music"].setLoop(True)
G["music"].play()
