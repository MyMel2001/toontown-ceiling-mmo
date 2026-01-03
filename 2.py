G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_6/dna/donalds_dock_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

LoadingZone = G["LoadingZone"]
# Tunnel back to TTC now through Loopy Lane (12)
LoadingZone.define(-191, -102, -205, -116, 12)

# Seaweed Street (1100)
# (In Donald's Dock, Seaweed Street is the one connecting to TTC, 
# but zone 18 is listed as Seaweed Street. 
# We'll use linktunnel_dd_1225 for Seaweed Street 18 if Loopy Lane 12 is at 1101)
LoadingZone.define(-208, 82, -222, 68, 18)
# Barnacle Boulevard (1200)
# (Wait, if Seaweed is 18, Barnacle is 19. Using 1225 was Barnacle in my previous note.
# Let's use 1301 for Lighthouse Lane 20)
LoadingZone.define(172, -44, 158, -58, 20)
# Outdoor Zone (6000)
LoadingZone.define(-46, 179, -60, 165, 6)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/DOCKS.ogg')
G["music"].setLoop(True)
G["music"].play()

# Streets are loaded progressively from tunnels
# Seaweed Street
# loadStreet('phase_6/dna/donalds_dock_1100.xml', pos=(0,0,0))

# Cogs removed from playground
