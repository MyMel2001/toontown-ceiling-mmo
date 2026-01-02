from direct.gui.DirectGui import *
from panda3d.core import *
from pickAToon import toonDnaArray, toonNameArray, getToon, get_builtins
from networking import Networking
from make_a_toon import MakeAToon

class PickAToonMenu:
    def __init__(self, callback):
        self.callback = callback
        self.mainFrame = DirectFrame(frameColor=(0, 0, 0, 0.5), frameSize=(-1, 1, -1, 1))
        
        self.title = DirectLabel(text="Pick A Toon", scale=0.15, pos=(0, 0, 0.8), parent=self.mainFrame)
        
        self.toonButtons = []
        for i in range(len(toonNameArray)):
            btn = DirectButton(text=toonNameArray[i], scale=0.1, pos=(0, 0, 0.5 - i*0.2),
                               command=self.selectToon, extraArgs=[i], parent=self.mainFrame)
            self.toonButtons.append(btn)
            
        self.makeToonBtn = DirectButton(text="Make A Toon", scale=0.1, pos=(0, 0, -0.7),
                                       command=self.makeToon, parent=self.mainFrame)

    def selectToon(self, index):
        self.destroy()
        self.callback(index)

    def makeToon(self):
        self.destroy()
        MakeAToon(self.callback)

    def destroy(self):
        self.mainFrame.destroy()
