from direct.gui.DirectGui import *
from panda3d.core import *
from direct.fsm.FSM import FSM
from direct.interval.IntervalGlobal import *

class Battle(FSM):
    def __init__(self, toon, cog, remote=False):
        FSM.__init__(self, "Battle")
        self.toon = toon
        self.cog = cog
        self.cog.inBattle = True
        self.remote = remote

        if not self.remote:
            if hasattr(base, "localAvatar") and hasattr(base.localAvatar, "physControls"):
                base.localAvatar.physControls.disableAvatarControls()
        
        self.battleFrame = DirectFrame(frameColor=(0, 0, 0, 0.7), frameSize=(-0.8, 0.8, -0.6, 0.6),
                                       pos=(0, 0, -0.4))
        if self.remote: self.battleFrame.hide()
        
        self.title = DirectLabel(text="Select a Gag", scale=0.1, pos=(0, 0, 0.4), 
                                 parent=self.battleFrame, text_fg=(1,1,1,1), frameColor=(0,0,0,0))
        
        self.cogInfo = DirectLabel(text=f"{self.cog.name} (Level {self.cog.level})", scale=0.08, pos=(0, 0, 0.3),
                                   parent=self.battleFrame, text_fg=(1, 0.8, 0.8, 1), frameColor=(0, 0, 0, 0))

        self.gags = [
            ("Cream Pie Slice", "throw", "phase_5/models/props/cream-pie-slice.bam"),
            ("Fruit Pie Slice", "throw", "phase_5/models/props/fruit-pie-slice.bam"),
            ("Squirting Flower", "squirt", "phase_3.5/models/props/squirting-flower.bam"),
            ("Glass of Water", "squirt", "phase_5/models/props/glass-mod.bam")
        ]
        
        self.gagDamage = {
            "Cream Pie Slice": 5,
            "Fruit Pie Slice": 10,
            "Squirting Flower": 3,
            "Glass of Water": 6
        }

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
        damage = self.gagDamage.get(gagName, 5)
        print(f"Toon uses {gagName}! Deals {damage} damage.")
        
        if hasattr(base, "net"):
            base.net.sendBattleAction(self.cog.cogId, damage)

        # Load gag prop
        try:
            prop = loader.loadModel(modelPath)
            prop.reparentTo(self.toon.find("**/def_joint_right_hold"))
            prop.setScale(1.25,1.25,1.25)
        except:
            prop = None

        # Play animation based on track
        anim = "Pie Throw" if track == "throw" else "Walk" # Walk as fallback for squirt if not found
        self.toon.play(anim)
        
        # Cog reaction
        Sequence(
            Wait(0.5),
            Func(self.cog.node.play, "Walk"), # Walk as fallback for cringe for now
            # Func(self.cog.takeDamage, damage), # Damage now synced from server
            Wait(1.5),
            Func(self.cleanupProp, prop),
            Func(self.checkBattleEnd)
        ).start()

    def checkBattleEnd(self):
        if self.cog.hp <= 0:
            print(f"{self.cog.name} defeated!")
            self.cog.node.play("Walk") # Replace with death animation if available, Walk for now
            Sequence(
                Wait(1.0),
                Func(self.cleanup),
                Func(self.cog.cleanup)
            ).start()
        elif hasattr(base, "localAvatar") and base.localAvatar.hp <= 0:
            print("Toon defeated!")
            self.cleanup()
            # Logic for toon "dying" and going back to playground
            if hasattr(base, "loadZone") and hasattr(base, "getPlaygroundForZone"):
                base.loadZone(base.getPlaygroundForZone(getattr(base, "zID", 1)))
        else:
            self.cogTurn()

    def cleanupProp(self, prop):
        if prop:
            prop.removeNode()

    def cogTurn(self):
        if not self.cog or self.cog.node.isEmpty(): return
        damage = self.cog.level * 2
        print(f"Cog attacks Toon! Deals {damage} damage.")
        self.cog.node.play("Walk") 
        self.toon.play("Cringe")
        
        if hasattr(base, "localAvatar"):
            base.localAvatar.hp -= damage
            if base.localAvatar.hp < 0: base.localAvatar.hp = 0
            if hasattr(base, "laffMeter"):
                base.laffMeter.updateLaff()
        
        Sequence(
            Wait(2.0),
            Func(self.checkBattleEndAfterCog)
        ).start()

    def checkBattleEndAfterCog(self):
        if hasattr(base, "localAvatar") and base.localAvatar.hp <= 0:
            self.checkBattleEnd()
        else:
            self.battleFrame.show()
        
    def enterRun(self):
        self.cleanup()
        
    def cleanup(self):
        self.battleFrame.destroy()
        if not self.cog.node.isEmpty():
            self.cog.node.setPos(self.cog_orig_pos)
            self.cog.node.loop("Neutral")
        self.cog.inBattle = False
        
        if hasattr(base, "localAvatar") and hasattr(base.localAvatar, "physControls"):
            base.localAvatar.physControls.enableAvatarControls()

        if hasattr(base, "battleMgr"):
            base.battleMgr.stopBattle()
        
        self.request("Off")

class BattleManager:
    def __init__(self):
        self.currentBattle = None
        
    def startBattle(self, toon, cog, remote=False):
        if not self.currentBattle:
            if not remote and hasattr(base, "net"):
                base.net.requestBattle(cog.cogId)
            self.currentBattle = Battle(toon, cog, remote=remote)
            self.currentBattle.request("Wait")

    def stopBattle(self):
        self.currentBattle = None
