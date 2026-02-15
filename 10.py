G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# Lullaby Lane (9101 -> 26) - Tunnel at (-65.2, -195.2, -6.7) facing 0 HPR
# Zone placed in front of tunnel (extending toward -Y)
LoadingZone.define(-75, -205, -55, -185, 26, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))
# Pajama Place (9201 -> 27) - Tunnel at (55, 195, -6.65) facing 180 HPR
# Zone placed in front of tunnel (extending toward +Y)
LoadingZone.define(45, 185, 65, 205, 27, entryPos=(0, 20, 0.025), entryHpr=(0, 0, 0))

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Lullaby Lane
# loadStreet('phase_8/dna/donalds_dreamland_9100.xml', pos=(0,0,0))

# Cogs removed from playground
