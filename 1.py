G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_4/dna/toontown_central_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Silly Street (To Melodyland)
LoadingZone.define(-146.117, -4.0677, -153.27, 12.1799, 11)
# Loopy Lane (To Docks)
LoadingZone.define(-38.3287, 91.7318, -53.18, 101.799, 12)
# Punchline Place (To Garden)
LoadingZone.define(34.5333, -163.679, 24.6789, -148.533, 13)

# Toontown Central Playground Extras
# Goofy Speedway
LoadingZone.define(35.5112, 158.154, 21.1569, 161.036, 4)
# The Trolley
LoadingZone.define(-127.328, -80.7726, -140.133, -56.2604, 6)
# Toon Hall
LoadingZone.define(112.26, -3.75061, 105.029, 8.132, 7)

G["music"].stop()
G["music"] = loader.loadSfx('phase_4/audio/bgm/TC_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are now loaded progressively when approaching tunnels

# Load the Silly Street tunnel/street model
# No longer loading streets in playground
# loadStreet('phase_4/dna/toontown_central_sz.xml', pos=(0,0,0))

# hello from code-server on iPad
