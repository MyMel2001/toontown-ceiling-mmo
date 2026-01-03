from direct.actor.Actor import Actor
from panda3d.core import *
from direct.task import Task
import random
from thirdparty.nametag.toonNametag import createNametag

suitTypes = {
    'A': 'phase_3.5/models/char/suitA-mod.bam',
    'B': 'phase_3.5/models/char/suitB-mod.bam',
    'C': 'phase_3.5/models/char/suitC-mod.bam'
}

suitAnims = {
    'neutral': 'phase_4/models/char/suitA-neutral.bam',
    'walk': 'phase_4/models/char/suitA-walk.bam',
}
# Note: For simplicity using A anims for all for now, or I'd need to map them all.

class Cog:
    def __init__(self, type='A', head=None, name="Cog"):
        self.type = type
        
        # Determine correct animation paths based on type
        # Suit A and B are usually in phase_4, C is in phase_3.5
        neutral_anim = suitAnims['neutral'].replace('A', type)
        walk_anim = suitAnims['walk'].replace('A', type)
        
        if type == 'C':
            neutral_anim = neutral_anim.replace('phase_4', 'phase_3.5')
            walk_anim = walk_anim.replace('phase_4', 'phase_3.5')
            
        self.node = Actor(suitTypes[type], {
            'neutral': neutral_anim,
            'walk': walk_anim
        })
        
        # Add nametag
        self.nametag = createNametag(name, bg=(0.2, 0.2, 0.2, 0.8), fg=(0.8, 0.8, 0.8, 1), fontPath='phase_3/fonts/vtRemingtonPortable.ttf')
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
                for part in head_model.getChildren():
                    part.hide()
                
                cog_head_name = name.lower().replace(" ", "")
                head_part = head_model.find(f"**/{cog_head_name}*")
                
                if head_part.isEmpty():
                    # Fallback names
                    if "flunky" in cog_head_name: head_part = head_model.find("**/flunky")
                    elif "pencilpusher" in cog_head_name: head_part = head_model.find("**/pencilpusher")
                    elif "yesman" in cog_head_name: head_part = head_model.find("**/yesman")
                
                if not head_part.isEmpty():
                    head_part.show()
                elif head_model.getNumChildren() > 0:
                    head_model.getChild(0).show()
            except Exception as e:
                print(f"Failed to load Cog head: {head_path}: {e}")
            
        self.node.reparentTo(render)
        self.node.loop('neutral')
        self.name = name
        
    def setPos(self, x, y, z):
        self.node.setPos(x, y, z)
        
    def setH(self, h):
        self.node.setH(h)

    def cleanup(self):
        self.node.cleanup()
        self.node.removeNode()

class CogManager:
    def __init__(self):
        self.cogs = []
        # Clear existing update task if it exists to avoid duplicates
        base.taskMgr.remove("CogManagerUpdate")
        base.taskMgr.add(self.update, "CogManagerUpdate")
        
    def spawnCog(self, type='A', head=None, pos=(0,0,0), name="Cog"):
        cog = Cog(type, head, name=name)
        cog.setPos(*pos)
        cog.orig_pos = Point3(*pos)
        cog.target_pos = cog.orig_pos + Point3(random.uniform(-1255, 1255), random.uniform(-1255, 1255), 0)
        self.cogs.append(cog)
        return cog

    def update(self, task):
        dt = globalClock.getDt()
        for cog in self.cogs:
            dist = (cog.node.getPos() - cog.target_pos).length()
            if dist > 1:
                cog.node.lookAt(cog.target_pos)
                cog.node.setPos(cog.node.getPos() + cog.node.getQuat().getForward() * 5 * dt)
                if cog.node.getCurrentAnim() != 'walk':
                    cog.node.loop('walk')
            else:
                cog.target_pos = cog.orig_pos + Point3(random.uniform(-50, 50), random.uniform(-50, 50), 0)
        return Task.cont
