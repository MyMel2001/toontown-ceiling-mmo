from direct.actor.Actor import Actor
from panda3d.core import NodePath, Filename

class ToonHead:
    def __init__(self, species, headType, hasEyelashes):
        self.head_model = NodePath('toon_head')
        self.species = species
        self.headType = headType # e.g., 'ls', 'ss'
        self.hasEyelashes = hasEyelashes
        self.generate()

    def generate(self):
        # Determine the base model path
        phase = 'phase_3'
        path = ''
        if self.species == 'b': path = 'phase_3/models/char/bear-heads-1000'
        elif self.species == 'ca': path = 'phase_3/models/char/cat-heads-1000'
        elif self.species == 'cr': path = 'phase_3/models/char/crocodile-heads-1000'
        elif self.species == 'de': path = 'phase_3/models/char/deer-heads-1000'
        elif self.species == 'du': path = 'phase_3/models/char/duck-heads-1000'
        elif self.species == 'h': path = 'phase_3/models/char/horse-heads-1000'
        elif self.species == 'mo': path = 'phase_3/models/char/monkey-heads-1000'
        elif self.species == 'mi': path = 'phase_3/models/char/mouse-heads-1000'
        elif self.species == 'p': path = 'phase_3/models/char/pig-heads-1000'
        elif self.species == 'r': path = 'phase_3/models/char/rabbit-heads-1000'
        elif self.species == 'd':
            # Dogs are special and use specific models per size
            if self.headType == 'ss': path = 'phase_3/models/char/tt_a_chr_dgm_shorts_head_1000'
            elif self.headType == 'sl': path = 'phase_3/models/char/tt_a_chr_dgs_shorts_head_1000'
            elif self.headType == 'ls': path = 'phase_3/models/char/tt_a_chr_dgm_skirt_head_1000'
            elif self.headType == 'll': path = 'phase_3/models/char/tt_a_chr_dgl_shorts_head_1000'
        elif self.species == 'ri': path = 'phase_3/models/char/tt_a_chr_rgy_shorts_head_1000'

        if not path:
            print(f"Unknown species: {self.species}")
            return

        full_model = loader.loadModel(path + ".bam")
        
        # Determine piece names
        head_size = 'short' if self.headType[0] == 's' else 'long'
        muzzle_size = 'short' if self.headType[1] == 's' else 'long'

        if self.species == 'd' or self.species == 'ri':
            # These specific models just need everything shown
            full_model.copyTo(self.head_model)
            for part in self.head_model.findAllMatches('**/*'):
                part.show()
        else:
            # Extract specific pieces and copy them to our clean head_model
            pieces = [
                f'**/head-{head_size}',
                f'**/head-front-{head_size}',
                f'**/muzzle-{muzzle_size}-neutral',
                f'**/eyes-{head_size}',
                f'**/ears-{head_size}',
                f'**/joint_pupilL_{head_size}',
                f'**/joint_pupilR_{head_size}'
            ]
            
            # Special case for rabbits who sometimes just have 'eyes'
            if self.species == 'r':
                pieces.append('**/eyes')

            # Special cases for deer antlers
            if self.species == 'de':
                pieces.append(f'**/antlers-{head_size}')
                pieces.append(f'**/nose-{muzzle_size}')

            for p in pieces:
                node = full_model.find(p)
                if not node.isEmpty():
                    new_node = node.copyTo(self.head_model)
                    new_node.show()

        if self.hasEyelashes:
            self.applyEyelashes()

    def applyEyelashes(self):
        # Eyelashes logic
        head_size = 'short' if self.headType[0] == 's' else 'long'
        lash_path = ''
        if self.species == 'b': lash_path = 'phase_3/models/char/bear-lashes'
        elif self.species == 'ca': lash_path = 'phase_3/models/char/cat-lashes'
        elif self.species == 'cr': lash_path = 'phase_3/models/char/crocodile-lashes'
        elif self.species == 'd': lash_path = 'phase_3/models/char/dog-lashes'
        elif self.species == 'de': lash_path = 'phase_3/models/char/deer-lashes'
        elif self.species == 'du': lash_path = 'phase_3/models/char/duck-lashes'
        elif self.species == 'h': lash_path = 'phase_3/models/char/horse-lashes'
        elif self.species == 'mo': lash_path = 'phase_3/models/char/monkey-lashes'
        elif self.species == 'mi': lash_path = 'phase_3/models/char/mouse-lashes'
        elif self.species == 'p': lash_path = 'phase_3/models/char/pig-lashes'
        elif self.species == 'r': lash_path = 'phase_3/models/char/rabbit-lashes'
        
        if lash_path:
            try:
                lashes = loader.loadModel(lash_path + ".bam")
                # TT lashes usually have 'open-short' or 'open-long'
                specific_lash = lashes.find(f'**/open-{head_size}')
                if specific_lash.isEmpty() and self.species in ['de', 'r']:
                    specific_lash = lashes.find('**/open-short')
                
                if not specific_lash.isEmpty():
                    parent = self.head_model.find(f'**/eyes-{head_size}')
                    if parent.isEmpty():
                        parent = self.head_model.find('**/eyes')
                    
                    if not parent.isEmpty():
                        specific_lash.copyTo(parent)
            except:
                pass

    def removeHead(self):
        self.head_model.removeNode()
