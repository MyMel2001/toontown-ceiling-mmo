from direct.gui.DirectGui import *
from panda3d.core import *
from thirdparty.createToon.src.toon.CeilingToon import Toon
from thirdparty.createToon.src.toon.ToonDNA import species_dict, colorsList, shirt_dict, short_dict, skirt_dict
from pickAToon import toonDnaArray, toonNameArray

class MakeAToon:
    def __init__(self, callback):
        self.callback = callback
        self.mainFrame = DirectFrame(frameColor=(0, 0, 0, 0.8), frameSize=(-1, 1, -1, 1))
        
        # Default DNA
        self.species = 'ca'
        self.head_type = 'ss'
        self.eyelashes = False
        self.torso = 'ss'
        self.legs = 's'
        self.color = 'White'
        self.name = "New Toon"
        
        self.toon = Toon(self.species, self.head_type, self.eyelashes, self.torso, self.legs, 
                         self.color, self.color, self.color, self.color, 
                         "Cattlelog Shirt 1", "Catalog Pants 1", None, "White", "White",
                         None, None, 0, None, None, None, "Neutral", True, False)
        self.toon.toonActor.reparentTo(self.mainFrame)
        self.toon.toonActor.setPos(0, 5, -0.5)
        self.toon.toonActor.setH(180)
        
        # UI
        self.title = DirectLabel(text="Make A Toon", scale=0.1, pos=(0, 0, 0.9), parent=self.mainFrame)
        
        self.speciesBtn = DirectButton(text="Next Species", scale=0.07, pos=(-0.7, 0, 0.7),
                                       command=self.nextSpecies, parent=self.mainFrame)
        
        self.colorBtn = DirectButton(text="Next Color", scale=0.07, pos=(-0.7, 0, 0.5),
                                     command=self.nextColor, parent=self.mainFrame)
        
        self.nameEntry = DirectEntry(initialText=self.name, scale=0.05, pos=(-0.2, 0, -0.7),
                                     numLines=1, focus=1, parent=self.mainFrame)
        
        self.doneBtn = DirectButton(text="Done", scale=0.1, pos=(0.7, 0, -0.8),
                                    command=self.done, parent=self.mainFrame)

    def nextSpecies(self):
        species_list = list(species_dict.values())
        idx = species_list.index(self.species)
        self.species = species_list[(idx + 1) % len(species_list)]
        self.updateToon()

    def nextColor(self):
        colors = list(colorsList.keys())
        idx = colors.index(self.color)
        self.color = colors[(idx + 1) % len(colors)]
        self.updateToon()

    def updateToon(self):
        self.toon.toonActor.cleanup()
        self.toon.toonActor.removeNode()
        self.toon = Toon(self.species, self.head_type, self.eyelashes, self.torso, self.legs, 
                         self.color, self.color, self.color, self.color, 
                         "Cattlelog Shirt 1", "Catalog Pants 1", None, "White", "White",
                         None, None, 0, None, None, None, "Neutral", True, False)
        self.toon.toonActor.reparentTo(self.mainFrame)
        self.toon.toonActor.setPos(0, 5, -0.5)
        self.toon.toonActor.setH(180)

    def done(self):
        name = self.nameEntry.get()
        # Add to global arrays (for this session)
        dna = [self.species, self.head_type, self.eyelashes, self.torso, self.legs, 
               self.color, self.color, self.color, self.color, 
               "Cattlelog Shirt 1", "Catalog Pants 1", None, "White", "White",
               None, None, 0, None, None, None, "Neutral", True, False]
        
        toonDnaArray.append(dna)
        toonNameArray.append(name)
        
        self.destroy()
        self.callback(len(toonNameArray) - 1)

    def destroy(self):
        self.toon.toonActor.cleanup()
        self.toon.toonActor.removeNode()
        self.mainFrame.destroy()
