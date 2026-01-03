G = get_builtins()
dna_loader = G["dna_loader"]
currentLand.currentLandModels[zones[zID]] = dna_loader.loadDNA('phase_10/dna/cog_hq_cashbot_sz.xml')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0, 0, 0)

G = get_builtins()
LoadingZone = G["LoadingZone"]
# To TTC (Approximate coordinates for the exit tunnel)
LoadingZone.define(170, -450, 150, -470, 1)

G["music"].stop()
G["music"] = loader.loadSfx('phase_9/audio/bgm/encntr_suit_winning_variation.ogg')
G["music"].setLoop(True)
G["music"].play()

# Cogs removed from Cashbot HQ area
