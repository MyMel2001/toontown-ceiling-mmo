G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/the_burrrgh_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# Walrus Way (3126 -> 23) - Tunnel at (160.26, -80.77, -0.62) facing 90 HPR
# Zone placed in front of tunnel (extending toward -Y)
LoadingZone.define(150, -90, 170, -70, 23, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))
# Sleet Street (3233 -> 24) - Tunnel at (-22.77, -253.67, -0.85) facing 23 HPR
# Zone placed in front of tunnel (extending toward -X and -Y)
LoadingZone.define(-12, -245, -33, -262, 24, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))
# Polar Place (3301 -> 25) - Tunnel at (100.11, 152.01, -0.54) facing 150 HPR
# Zone placed in front of tunnel (extending toward +X and -Y)
LoadingZone.define(115, 145, 90, 170, 25, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/TB_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Walrus Way
# loadStreet('phase_8/dna/the_burrrgh_3100.xml', pos=(0,0,0))

# Cogs removed from playground
