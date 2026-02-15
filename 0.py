G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

# Set zone bounds for Cog collisions (based on MML playground size)
if hasattr(base, 'cogMgr'):
    base.cogMgr.setZoneBounds(-80, 80, -100, 100)

LoadingZone = G["LoadingZone"]
# Loopy Lane (To TTC) - Tunnel at (80, 169.99, -0.17) facing 180 HPR
# Zone placed in front of tunnel (extending toward -Y)
LoadingZone.define(65, 155, 95, 185, 11, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))

# Tenor Terrace (4340 -> 15) - Tunnel at (-25, -209.95, -0.17) facing 0 HPR
# Zone placed in front of tunnel (extending toward -Y)
LoadingZone.define(-40, -220, -10, -200, 15, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))
# Alto Avenue (4127 -> 16) - Tunnel at (80, 169.99, -0.17) facing 180 HPR
# Zone placed in front of tunnel (extending toward -Y)
LoadingZone.define(65, 155, 95, 185, 16, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))
# Baritone Boulevard (4222 -> 17) - Tunnel at (-170.012, 44.58, -0.5) facing -90 HPR
# Zone placed in front of tunnel (extending toward +Y)
LoadingZone.define(-180, 34, -160, 54, 17, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))

global isCurrentZone
isCurrentZone = True

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Tenor Terrace
# loadStreet('phase_6/dna/minnies_melody_land_4100.xml', pos=(0,0,0))

# Cogs removed from playground
