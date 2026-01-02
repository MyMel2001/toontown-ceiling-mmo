from direct.gui.DirectGui import *
from panda3d.core import *
from direct.fsm.FSM import FSM
from direct.interval.IntervalGlobal import *

class Battle(FSM):
    def __init__(self, toon, cog):
        FSM.__init__(self, "Battle")
        self.toon = toon
        self.cog = cog
        
        self.battleFrame = DirectFrame(frameColor=(0, 0, 0, 0.7), frameSize=(-0.8, 0.8, -0.6, 0.6),
                                       pos=(0, 0, -0.4))
        
        self.title = DirectLabel(text="Select a Gag", scale=0.1, pos=(0, 0, 0.4), 
                                 parent=self.battleFrame, text_fg=(1,1,1,1), frameColor=(0,0,0,0))

        self.gags = [
            ("Cupcake", "throw", "phase_3.5/models/props/cupcake.bam"),
            ("Fruit Pie Slice", "throw", "phase_3.5/models/props/fruit-pie-slice.bam"),
            ("Squirting Flower", "squirt", "phase_3.5/models/props/squirt-flower.bam"),
            ("Glass of Water", "squirt", "phase_3.5/models/props/glass-of-water.bam")
        ]

        self.gagButtons = []
        for i, (name, track, model) in enumerate(self.gags):
            btn = DirectButton(text=name, scale=0.07, pos=(-0.4 if i < 2 else 0.4, 0, 0.2 - (i%2)*0.2),
                               command=self.doAttack, extraArgs=[name, track, model], parent=self.battleFrame)
            self.gagButtons.append(btn)

        self.runBtn = DirectButton(text="Run", scale=0.08, pos=(0, 0, -0.4),
                                   command=self.request, extraArgs=["Run"], parent=self.battleFrame)
        
        # Battle positioning
        self.cog_orig_pos = self.cog.node.getPos()
        self.cog.node.setPos(self.toon.getPos() + self.toon.getQuat().getForward() * 10)
        self.cog.node.lookAt(self.toon)
        self.toon.lookAt(self.cog.node)

    def doAttack(self, gagName, track, modelPath):
        self.battleFrame.hide()
        print(f"Toon uses {gagName}!")
        
        # Load gag prop
        try:
            prop = loader.loadModel(modelPath)
            prop.reparentTo(self.toon.find("**/def_joint_right_hold"))
        except:
            prop = None

        # Play animation based on track
        anim = "throw" if track == "throw" else "walk" # walk as fallback for squirt if not found
        self.toon.play(anim)
        
        # Cog reaction
        Sequence(
            Wait(0.5),
            Func(self.cog.node.play, "cringe"),
            Wait(1.5),
            Func(self.cleanupProp, prop),
            Func(self.cogTurn)
        ).start()

    def cleanupProp(self, prop):
        if prop:
            prop.removeNode()

    def cogTurn(self):
        if not self.cog or self.cog.node.isEmpty(): return
        print("Cog attacks Toon!")
        self.cog.node.play("walk") 
        self.toon.play("cringe")
        
        Sequence(
            Wait(2.0),
            Func(self.battleFrame.show)
        ).start()
        
    def enterRun(self):
        self.cleanup()
        
    def cleanup(self):
        self.battleFrame.destroy()
        self.cog.node.setPos(self.cog_orig_pos)
        self.cog.node.loop("neutral")

class BattleManager:
    def __init__(self):
        self.currentBattle = None
        
    def startBattle(self, toon, cog):
        if not self.currentBattle:
            self.currentBattle = Battle(toon, cog)
            self.currentBattle.request("Wait")
