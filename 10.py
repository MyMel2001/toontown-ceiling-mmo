G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_8/dna/donalds_dreamland_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# Lullaby Lane (zone 26) - Tunnel at (-65.2, -195.2, -6.7) facing 0 HPR
# Loading zone in front of tunnel (player approaches from -Y direction)
LoadingZone.define(-75, -210, -55, -180, 26, entryPos=(5, 40, 0.025), entryHpr=(0, 0, 0))
# Pajama Place (zone 27) - Tunnel at (55, 195, -6.65) facing 180 HPR
# Loading zone in front of tunnel (player approaches from +Y direction)
LoadingZone.define(45, 180, 65, 210, 27, entryPos=(80, 130, 0.025), entryHpr=(0, 0, 0))

G["music"].stop()
G["music"] = loader.loadSfx('phase_8/audio/bgm/DL_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()