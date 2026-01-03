from direct.actor.Actor import Actor
from panda3d.core import *
from direct.task import Task
from direct.gui.DirectGui import *
import random
from thirdparty.nametag.toonNametag import createNametag

suitTypes = {
    'A': 'phase_3.5/models/char/suitA-mod.bam',
    'B': 'phase_3.5/models/char/suitB-mod.bam',
    'C': 'phase_3.5/models/char/suitC-mod.bam'
}

suitAnims = {
    'Neutral': 'phase_4/models/char/suitA-neutral.bam',
    'Walk': 'phase_4/models/char/suitA-walk.bam',
}
# Note: For simplicity using A anims for all for now, or I'd need to map them all.

class Cog:
    def __init__(self, type='A', head=None, name="Cog", level=1, cogId=0):
        self.type = type
        self.level = level
        self.cogId = cogId
        self.maxHp = (level + 1) * (level + 2)
        self.hp = self.maxHp
        
        # Determine correct animation paths based on type
        # Suit A and B are usually in phase_4, C is in phase_3.5
        neutral_anim = suitAnims['Neutral'].replace('A', type)
        walk_anim = suitAnims['Walk'].replace('A', type)
        
        if type == 'C':
            neutral_anim = neutral_anim.replace('phase_4', 'phase_3.5')
            walk_anim = walk_anim.replace('phase_4', 'phase_3.5')
            
        self.node = Actor(suitTypes[type], {
            'Neutral': neutral_anim,
            'Walk': walk_anim
        })
        
        # Add nametag
        self.nametag = createNametag(f"{name}\nLevel {level}", bg=(0.2, 0.2, 0.2, 0.8), fg=(0.8, 0.8, 0.8, 1), fontPath='phase_3/fonts/vtRemingtonPortable.ttf')
        self.nametag.setScale(0.8)
        
        # Find the head joint for nametag placement
        head_joint = self.node.find('**/joint_head')
        if head_joint.isEmpty():
            head_joint = self.node.find('**/def_head')
        
        if not head_joint.isEmpty():
            self.nametag.reparentTo(head_joint)
            self.nametag.setPos(0, 0, 2)
        else:
            self.nametag.reparentTo(self.node)
            self.nametag.setPos(0, 0, 8)
        
        if not head:
            # Auto-determine head model if not provided
            if type == 'C': head = 'phase_3.5/models/char/suitC-heads.bam'
            else: head = f'phase_4/models/char/suit{type}-heads.bam'

        if head:
            # Fix: Ensure correct path for heads (many are in phase_4, some in phase_3.5)
            head_path = head
            
            # Cog A and B heads are in phase_4, C heads are in phase_3.5
            if type == 'A' or type == 'B':
                head_path = head_path.replace("phase_3.5", "phase_4")
            elif type == 'C':
                head_path = head_path.replace("phase_4", "phase_3.5")
            
            try:
                head_model = loader.loadModel(head_path)
                # Find the head joint
                head_joint = self.node.find('**/joint_head')
                if head_joint.isEmpty():
                    head_joint = self.node.find('**/def_head')
                
                if not head_joint.isEmpty():
                    head_model.reparentTo(head_joint)
                else:
                    head_model.reparentTo(self.node.find('**/+Character').getChild(0))
                
                # Filter Cog head pieces
                for part in head_model.findAllMatches('**'):
                    part.hide()
                
                cog_head_name = name.lower().replace(" ", "").replace("&", "")
                head_part = head_model.find(f"**/{cog_head_name}*")
                
                if head_part.isEmpty():
                    # Fallback names
                    if "flunky" in cog_head_name: head_part = head_model.find("**/flunky")
                    elif "pencilpusher" in cog_head_name: head_part = head_model.find("**/pencilpusher")
                    elif "yesman" in cog_head_name: head_part = head_model.find("**/yesman")
                    elif "mover" in cog_head_name: head_part = head_model.find("**/movershaker")
                    elif "bigcheese" in cog_head_name: head_part = head_model.find("**/thebigcheese")
                
                if not head_part.isEmpty():
                    head_part.show()
                    # Also show all parents up to the head_model root
                    p = head_part.getParent()
                    while p and p != head_model:
                        p.show()
                        p = p.getParent()
                elif head_model.getNumChildren() > 0:
                    head_model.getChild(0).show()
                    head_model.getChild(0).showThrough()
            except Exception as e:
                print(f"Failed to load Cog head: {head_path}: {e}")
            
        self.node.reparentTo(render)
        self.node.loop('Neutral')
        self.name = name
        self.inBattle = False
        
        # Create HP Meter
        self.hpMeter = DirectWaitBar(text="", value=100, range=100, scale=0.5, pos=(0, 0, 0.8), 
                                     barColor=(0, 1, 0, 1), frameColor=(0, 0, 0, 0.5),
                                     relief=DGG.FLAT)
        self.hpMeter.reparentTo(self.nametag)
        self.updateHpMeter()
        
    def takeDamage(self, amount):
        self.hp -= amount
        if self.hp < 0: self.hp = 0
        self.updateHpMeter()
        return self.hp <= 0

    def updateHpMeter(self):
        if hasattr(self, 'hpMeter'):
            self.hpMeter['value'] = (float(self.hp) / self.maxHp) * 100
            if self.hpMeter['value'] > 50:
                self.hpMeter['barColor'] = (0, 1, 0, 1)
            elif self.hpMeter['value'] > 20:
                self.hpMeter['barColor'] = (1, 1, 0, 1)
            else:
                self.hpMeter['barColor'] = (1, 0, 0, 1)

    def setPos(self, x, y, z):
        self.node.setPos(x, y, z)
        
    def setH(self, h):
        self.node.setH(h)

    def cleanup(self):
        self.node.cleanup()
        self.node.removeNode()

class CogManager:
    def __init__(self):
        self.cogs = {} # cogId: Cog object
        # Client CogManager no longer handles movement, server does
        
    def spawnCog(self, type='A', head=None, pos=(0,0,0), name="Cog", level=1, cogId=0):
        if cogId in self.cogs:
            self.cogs[cogId].cleanup()
            
        cog = Cog(type, head, name=name, level=level, cogId=cogId)
        cog.setPos(*pos)
        self.cogs[cogId] = cog
        return cog

    def removeCog(self, cogId):
        if cogId in self.cogs:
            self.cogs[cogId].cleanup()
            del self.cogs[cogId]

    def updateCog(self, cogId, pos, h, anim):
        if cogId in self.cogs:
            cog = self.cogs[cogId]
            if not cog.inBattle:
                cog.setPos(*pos)
                cog.setH(h)
                if cog.node.getCurrentAnim() != anim:
                    cog.node.loop(anim)

    def cleanup(self):
        for cog in self.cogs.values():
            cog.cleanup()
        self.cogs = {}
