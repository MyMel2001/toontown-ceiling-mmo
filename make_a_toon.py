from direct.gui.DirectGui import *
from panda3d.core import *
from thirdparty.createToon.src.toon.CeilingToon import Toon
from thirdparty.createToon.src.toon.ToonDNA import species_dict, colorsList, shirt_dict, short_dict, skirt_dict
from pickAToon import toonDnaArray, toonNameArray

class MakeAToon:
    def __init__(self, callback):
        self.callback = callback
        self.mainFrame = DirectFrame(frameColor=(0, 0, 0, 0.8), frameSize=(-1, 1, -1, 1))
        
        # Lists for cycling
        self.species_list = list(species_dict.values())
        self.color_list = list(colorsList.keys())
        self.shirt_list = list(shirt_dict.keys())
        self.short_list = list(short_dict.keys())
        self.skirt_list = list(skirt_dict.keys())
        self.torso_list = ['ss', 'ms', 'ls', 'sd', 'md', 'ld']
        self.leg_list = ['s', 'm', 'l']
        self.head_type_list = ['ss', 'sl', 'ls', 'll']

        # Default DNA
        self.species = 'ca'
        self.head_type = 'ss'
        self.eyelashes = False
        self.torso = 'ss'
        self.legs = 's'
        self.head_color = 'White'
        self.arm_color = 'White'
        self.glove_color = 'White'
        self.leg_color = 'White'
        self.shirt = "Cattlelog Shirt 1"
        self.shorts = "Catalog Pants 1"
        self.skirt = "Catalog Skirts 1"
        self.shirt_color = 'White'
        self.bottom_color = 'White'
        self.name = "New Toon"
        
        self.toon = None
        self.updateToon()
        
        # UI
        self.title = DirectLabel(text="Make A Toon", scale=0.1, pos=(0, 0, 0.9), parent=self.mainFrame)
        
        # Left Side - Body
        self.speciesBtn = DirectButton(text="Species", scale=0.06, pos=(-0.8, 0, 0.7),
                                       command=self.nextSpecies, parent=self.mainFrame)
        self.headTypeBtn = DirectButton(text="Head Type", scale=0.06, pos=(-0.8, 0, 0.55),
                                       command=self.nextHeadType, parent=self.mainFrame)
        self.torsoBtn = DirectButton(text="Torso", scale=0.06, pos=(-0.8, 0, 0.4),
                                       command=self.nextTorso, parent=self.mainFrame)
        self.legsBtn = DirectButton(text="Legs", scale=0.06, pos=(-0.8, 0, 0.25),
                                       command=self.nextLegs, parent=self.mainFrame)
        self.eyelashBtn = DirectButton(text="Eyelashes", scale=0.06, pos=(-0.8, 0, 0.1),
                                       command=self.toggleEyelashes, parent=self.mainFrame)

        # Middle Left - Colors
        self.headColorBtn = DirectButton(text="Head Color", scale=0.06, pos=(-0.4, 0, 0.7),
                                       command=self.nextHeadColor, parent=self.mainFrame)
        self.armColorBtn = DirectButton(text="Arm Color", scale=0.06, pos=(-0.4, 0, 0.55),
                                       command=self.nextArmColor, parent=self.mainFrame)
        self.legColorBtn = DirectButton(text="Leg Color", scale=0.06, pos=(-0.4, 0, 0.4),
                                       command=self.nextLegColor, parent=self.mainFrame)
        self.gloveColorBtn = DirectButton(text="Glove Color", scale=0.06, pos=(-0.4, 0, 0.25),
                                       command=self.nextGloveColor, parent=self.mainFrame)

        # Middle Right - Clothes
        self.shirtBtn = DirectButton(text="Shirt", scale=0.06, pos=(0.4, 0, 0.7),
                                       command=self.nextShirt, parent=self.mainFrame)
        self.bottomBtn = DirectButton(text="Bottom", scale=0.06, pos=(0.4, 0, 0.55),
                                       command=self.nextBottom, parent=self.mainFrame)
        self.shirtColorBtn = DirectButton(text="Shirt Color", scale=0.06, pos=(0.4, 0, 0.4),
                                       command=self.nextShirtColor, parent=self.mainFrame)
        self.bottomColorBtn = DirectButton(text="Bottom Color", scale=0.06, pos=(0.4, 0, 0.25),
                                       command=self.nextBottomColor, parent=self.mainFrame)

        self.nameEntry = DirectEntry(initialText=self.name, scale=0.05, pos=(-0.2, 0, -0.7),
                                     numLines=1, focus=1, parent=self.mainFrame)
        
        self.doneBtn = DirectButton(text="Done", scale=0.1, pos=(0.7, 0, -0.8),
                                    command=self.done, parent=self.mainFrame)

    def nextSpecies(self):
        idx = self.species_list.index(self.species)
        self.species = self.species_list[(idx + 1) % len(self.species_list)]
        self.updateToon()

    def nextHeadType(self):
        idx = self.head_type_list.index(self.head_type)
        self.head_type = self.head_type_list[(idx + 1) % len(self.head_type_list)]
        self.updateToon()

    def nextTorso(self):
        idx = self.torso_list.index(self.torso)
        self.torso = self.torso_list[(idx + 1) % len(self.torso_list)]
        self.updateToon()

    def nextLegs(self):
        idx = self.leg_list.index(self.legs)
        self.legs = self.leg_list[(idx + 1) % len(self.leg_list)]
        self.updateToon()

    def toggleEyelashes(self):
        self.eyelashes = not self.eyelashes
        self.updateToon()

    def nextHeadColor(self):
        idx = self.color_list.index(self.head_color)
        self.head_color = self.color_list[(idx + 1) % len(self.color_list)]
        self.updateToon()

    def nextArmColor(self):
        idx = self.color_list.index(self.arm_color)
        self.arm_color = self.color_list[(idx + 1) % len(self.color_list)]
        self.updateToon()

    def nextLegColor(self):
        idx = self.color_list.index(self.leg_color)
        self.leg_color = self.color_list[(idx + 1) % len(self.color_list)]
        self.updateToon()

    def nextGloveColor(self):
        idx = self.color_list.index(self.glove_color)
        self.glove_color = self.color_list[(idx + 1) % len(self.color_list)]
        self.updateToon()

    def nextShirt(self):
        idx = self.shirt_list.index(self.shirt)
        self.shirt = self.shirt_list[(idx + 1) % len(self.shirt_list)]
        self.updateToon()

    def nextBottom(self):
        if self.torso.endswith('s'):
            idx = self.short_list.index(self.shorts)
            self.shorts = self.short_list[(idx + 1) % len(self.short_list)]
        else:
            idx = self.skirt_list.index(self.skirt)
            self.skirt = self.skirt_list[(idx + 1) % len(self.skirt_list)]
        self.updateToon()

    def nextShirtColor(self):
        idx = self.color_list.index(self.shirt_color)
        self.shirt_color = self.color_list[(idx + 1) % len(self.color_list)]
        self.updateToon()

    def nextBottomColor(self):
        idx = self.color_list.index(self.bottom_color)
        self.bottom_color = self.color_list[(idx + 1) % len(self.color_list)]
        self.updateToon()

    def updateToon(self):
        if self.toon:
            self.toon.toonActor.cleanup()
            self.toon.toonActor.removeNode()
            
        short_tex = self.shorts if self.torso.endswith('s') else None
        skirt_tex = self.skirt if self.torso.endswith('d') else None
        
        self.toon = Toon(self.species, self.head_type, self.eyelashes, self.torso, self.legs, 
                         self.head_color, self.arm_color, self.glove_color, self.leg_color, 
                         self.shirt, short_tex, skirt_tex, self.shirt_color, self.bottom_color,
                         None, None, 0, None, None, None, "Neutral", True, False)
        self.toon.toonActor.reparentTo(self.mainFrame)
        self.toon.toonActor.setPos(0, 5, -0.5)
        self.toon.toonActor.setScale(.25,.25,.25)
        self.toon.toonActor.setH(180)

    def done(self):
        name = self.nameEntry.get()
        short_tex = self.shorts if self.torso.endswith('s') else None
        skirt_tex = self.skirt if self.torso.endswith('d') else None
        
        dna = [self.species, self.head_type, self.eyelashes, self.torso, self.legs, 
               self.head_color, self.arm_color, self.glove_color, self.leg_color, 
               self.shirt, short_tex, skirt_tex, self.shirt_color, self.bottom_color,
               None, None, 0, None, None, None, "Neutral", True, False]
        self.toon.toonActor.setScale(1,1,1)
        toonDnaArray.append(dna)
        toonNameArray.append(name)
        
        self.destroy()
        self.callback(len(toonNameArray) - 1)

    def destroy(self):
        if self.toon:
            self.toon.toonActor.cleanup()
            self.toon.toonActor.removeNode()
        self.mainFrame.destroy()
