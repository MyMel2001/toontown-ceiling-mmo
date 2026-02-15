G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/minnies_melody_land_4100.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)

# Load the tunnel back to MML
# G["loadStreet"]('phase_6/dna/minnies_melody_land_sz.xml', pos=(0,0,0))

# Setup tunnel collision
base.localAvatar.setPos(0, 20, 0)

LoadingZone = G["LoadingZone"]
# Back to MML Playground
LoadingZone.define(-170, 35, -160, 45, 0, entryPos=(-25, -200, 0.025), entryHpr=(0, 0, 0))
# Forward to TTC (Loopy Lane)
LoadingZone.define(-464.72, 205, -454.72, 215, 1, entryPos=(0, 0, 0.025), entryHpr=(0, 0, 0))

if hasattr(base, "cogMgr"):
    base.cogMgr.setZoneBounds(-500, 100, -50, 300)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_sz.ogg')
G["music"].setLoop(True)
G["music"].play()
