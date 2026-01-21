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
            ("SUPER Cream Pie Slice", "throw", "phase_5/models/props/cream-pie-slice.bam"),
            ("Squirting Flower", "squirt", "phase_3.5/models/props/squirting-flower.bam"),
            ("Glass of Water", "squirt", "phase_5/models/props/glass-mod.bam")        
            ]
        self.gagDamage = {
            "Cream Pie Slice": 5,
            "Fruit Pie Slice": 10,
            "SUPER Cream Pie Slice": 69,
            "Squirting Flower": 3,
            "Glass of Water": 6
        }

        self.gagButtons = []
        numGags = len(self.gags)
        cols = 2 if numGags <= 10 else 3
        
        for i, (name, track, model) in enumerate(self.gags):
            row = i // cols
            col = i % cols
            
            # Calculate grid layout
            x_range = 1.0
            x_start = -x_range / 2
            x_offset = x_range / (cols - 1) if cols > 1 else 0
            
            # Center if the last row is incomplete
            items_in_last_row = numGags % cols
            is_last_row = row == (numGags - 1) // cols
            if is_last_row and items_in_last_row > 0 and items_in_last_row < cols:
                last_row_x_start = -(x_offset * (items_in_last_row - 1)) / 2
                x_pos = last_row_x_start + col * x_offset
            else:
                x_pos = x_start + col * x_offset
                
            z_start = 0.2
            z_offset = 0.13
            z_pos = z_start - row * z_offset
            
            # Auto-sizing: slightly scale down for long names or many gags
            btn_scale = 0.064
            if len(name) > 15:
                btn_scale = 0.064
            if numGags > 12:
                btn_scale *= 0.8

            btn = DirectButton(text=name, scale=btn_scale, pos=(x_pos, 0, z_pos),
                               command=self.doAttack, extraArgs=[name, track, model], parent=self.battleFrame)
            self.gagButtons.append(btn)

        self.runBtn = DirectButton(text="Run", scale=0.1, pos=(0, 0, -0.4),
                                   command=self.request, extraArgs=["Run"], parent=self.battleFrame)
        
        # Battle positioning
        self.cog_orig_pos = self.cog.node.getPos()
        self.cog.node.setPos(self.toon.getPos() + self.toon.getQuat().getForward() * 10)
        self.cog.node.lookAt(self.toon)
        self.toon.lookAt(self.cog.node)

    def doAttack(self, gagName, track, modelPath):
        if hasattr(base, "localAvatar") and base.localAvatar.hp <= 0:
            return
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
            # Update battle task progress
            if hasattr(base, 'tasksHUD'):
                base.tasksHUD.updateTaskProgress('battle', 1)
            self.cog.node.play("Walk") # Replace with death animation if available, Walk for now
            Sequence(
                Wait(1.0),
                Func(self.cleanup),
                Func(self.cog.cleanup),
                Func(self.request, "Off")
            ).start()
        elif hasattr(base, "localAvatar") and base.localAvatar.hp <= 0:
            print("Toon defeated!")
            self.cleanup()
            self.request("Off")
            # LaffMeter handles teleportation via updateLaff()
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
        if self.state == "Off": return
        if hasattr(base, "localAvatar") and base.localAvatar.hp <= 0:
            self.checkBattleEnd()
        elif self.cog and not self.cog.node.isEmpty():
            self.battleFrame.show()
        else:
            self.cleanup()
            self.request("Off")
        
    def enterRun(self):
        print("Running away from battle...")
        if hasattr(base, "loadZone") and hasattr(base, "getPlaygroundForZone") and hasattr(base, "zID"):
            # Teleport back to the playground of the current neighborhood
            playground = base.getPlaygroundForZone(base.zID)
            print(f"Teleporting to playground: {playground}")
            base.loadZone(playground)
        else:
            self.cleanup()
        self.demand("Off")

    def cleanup(self):
        if not hasattr(self, "battleFrame") or self.battleFrame is None:
            return
            
        self.battleFrame.destroy()
        self.battleFrame = None
        
        if self.cog and not self.cog.node.isEmpty():
            self.cog.node.setPos(self.cog_orig_pos)
            self.cog.node.loop("Neutral")
            self.cog.inBattle = False
        
        if hasattr(base, "localAvatar") and hasattr(base.localAvatar, "physControls"):
            base.localAvatar.physControls.enableAvatarControls()

        if hasattr(base, "battleMgr"):
            base.battleMgr.stopBattle()

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
