from pickAToon import createNPC

G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_4/dna/toontown_central_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

# Create quest giver NPCs in Toontown Central
# Quest Giver 1 at position from DNA: npc_questgiver_origin_0
createNPC(['mi', 'ss', False, 'ss', 'l', 'Blue', 'Red', 'Green', 'Red', '2019 Winter Laff-o-lympics Gold Medal', 'Beta Bug Hunter Shorts', 'Beta Bug Hunter Skirt', 'Amber', 'Aqua', None, None, 4, None, None, None, 'Neutral', True, False], -21.5, -83.8, 0.525, 0, 0, 0, "Professor Pete")

# Quest Giver 2 at position from DNA: npc_questgiver_origin_1
createNPC(['ca', 'ls', False, 'ls', 'l', 'Cartoonival Blue', 'Cartoonival Blue', 'White', 'Cartoonival Blue', '2019 Winter Laff-o-lympics Bronze Medal', 'Bee Shorts', None, 'Amber', 'White', None, 'Aviator Shades', 1, None, None, 'Aqua Toon Boots', 'Neutral', True, False], -30.9, -85.1, 0.525, 180, 0, 0, "Doctor Dimwit")

LoadingZone = G["LoadingZone"]
# Punchline Place (To Docks)
LoadingZone.define(-38.3287, 91.7318, -53.18, 101.799, 13)
# Loopy Lane (To Melodyland)
LoadingZone.define(-146.117, -4.0677, -153.27, 12.1799, 12)
# Silly Street (To Garden)
LoadingZone.define(34.5333, -163.679, 24.6789, -148.533, 11)

# Toontown Central Playground Extras
# Goofy Speedway
LoadingZone.define(35.5112, 158.154, 21.1569, 161.036, 4)
# The Trolley - Randomize game loading
def loadRandomTrolleyGame():
    import random
    game_models = [
        ("phase_4/models/minigames/maze_4player.bam", "Maze Game"),
        ("phase_4/models/minigames/cogthief_game.bam", "Cog Game"),
        ("phase_4/models/minigames/tag_game.bam", "Tag Game")
    ]
    selected = random.choice(game_models)
    return selected

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
