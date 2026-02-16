G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

# Set zone bounds for Cog collisions (based on MML playground size)
if hasattr(base, 'cogMgr'):
    base.cogMgr.setZoneBounds(-80, 80, -100, 100)

LoadingZone = G["LoadingZone"]
# Alto Avenue (zone 16) - Tunnel at (80, 169.99, -0.17) facing 180 HPR
# Loading zone in front of tunnel (player approaches from -Y direction, heading 180 faces -Y)
LoadingZone.define(70, 160, 90, 180, 16, entryPos=(80, 165, 0.025), entryHpr=(180, 0, 0))
# Baritone Boulevard (zone 17) - Tunnel at (-170.01, 44.58, -0.5) facing -90 HPR
# Loading zone in front of tunnel (player approaches from +X direction)
LoadingZone.define(-185, 35, -155, 55, 17, entryPos=(695, 215, 0.025), entryHpr=(-90, 0, 0))
# Tenor Terrace (zone 15) - Tunnel at (-25, -209.95, -0.17) facing 0 HPR
# Loading zone in front of tunnel (player approaches from -Y direction, heading 0 faces +Y)
LoadingZone.define(-35, -220, -15, -200, 15, entryPos=(-165, 40, 0.025), entryHpr=(-90, 0, 0))

global isCurrentZone
isCurrentZone = True

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()