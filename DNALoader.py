import xml.etree.ElementTree as ET
from panda3d.core import *
from direct.actor.Actor import Actor
import os

global scene

class DNALoader:
    def __init__(self):
        self.storage = {}
        self.dna_codes = {}

    def loadStorage(self, path):
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            for model in root.findall('model'):
                model_path = model.get('path')
                for store_node in model.findall('store_node'):
                    code = store_node.get('code')
                    node_name = store_node.get('node')
                    self.storage[code] = {'path': model_path, 'node': node_name}
        except Exception as e:
            print(f"Error loading storage DNA {path}: {e}")

    def loadDNA(self, path, parent=None):
        if parent is None:
            parent = render
        try:
            tree = ET.parse(path)
            root = tree.getroot()

            scene = NodePath("dna_scene")
            scene.reparentTo(parent)

            self.parseNode(root, scene)
            return scene
        except Exception as e:
            print(f"Error loading DNA {path}: {e}")
            return None

    def parseNode(self, xml_node, panda_node):
        for child in xml_node:
            if child.tag == 'prop' or child.tag == 'anim_prop' or child.tag == 'street':
                self.handleProp(child, panda_node)
            elif child.tag == 'group':
                group_node = panda_node.attachNewNode(child.get('name', 'group'))
                self.parseNode(child, group_node)
            elif child.tag == 'visgroup':
                vis_node = panda_node.attachNewNode(child.get('zone', 'visgroup'))
                self.parseNode(child, vis_node)
            elif child.tag == 'landmark_building':
                self.handleLandmark(child, panda_node)
            elif child.tag == 'flat_building':
                self.handleFlatBuilding(child, panda_node)
            elif child.tag == 'wall':
                self.handleWall(child, panda_node)
            elif child.tag == 'node':
                node = panda_node.attachNewNode(child.get('name', 'node'))
                self.parseNode(child, node)
            elif child.tag == 'pos':
                panda_node.setPos(float(child.get('x', 0)), float(child.get('y', 0)), float(child.get('z', 0)))
            elif child.tag == 'nhpr':
                panda_node.setHpr(float(child.get('h', 0)), float(child.get('p', 0)), float(child.get('r', 0)))
            elif child.tag == 'hpr':
                panda_node.setHpr(float(child.get('h', 0)), float(child.get('p', 0)), float(child.get('r', 0)))
            elif child.tag == 'scale':
                panda_node.setScale(float(child.get('x', 1)), float(child.get('y', 1)), float(child.get('z', 1)))
            elif child.tag == 'color':
                panda_node.setColor(float(child.get('r', 1)), float(child.get('g', 1)), float(child.get('b', 1)), float(child.get('a', 1)))
            elif child.tag == 'sign':
                self.handleSign(child, panda_node)
            elif child.tag == 'baseline':
                self.handleBaseline(child, panda_node)

    def handleProp(self, xml_node, parent):
        code = xml_node.get('code')
        if code in self.storage:
            entry = self.storage[code]
            model_path = entry['path']
            node_name = entry['node']
            if not model_path.endswith('.bam'):
                model_path += '.bam'
            try:
                full_model = loader.loadModel(model_path)
                if node_name:
                    model = full_model.find("**/" + node_name)
                else:
                    model = full_model.find("**/" + code)

                if model.isEmpty():
                    model = full_model

                new_np = parent.attachNewNode(code)
                model.copyTo(new_np)
                self.parseNode(xml_node, new_np)
            except Exception as e:
                print(f"Failed to load model {model_path} for code {code}: {e}")
        else:
            dummy = parent.attachNewNode(xml_node.get('name', xml_node.get('code', 'prop')))
            self.parseNode(xml_node, dummy)

    def handleLandmark(self, xml_node, parent):
        code = xml_node.get('code')
        if code in self.storage:
            entry = self.storage[code]
            model_path = entry['path']
            node_name = entry['node']
            if not model_path.endswith('.bam'):
                model_path += '.bam'
            try:
                full_model = loader.loadModel(model_path)
                if node_name:
                    model = full_model.find("**/" + node_name)
                else:
                    model = full_model.find("**/" + code)

                if model.isEmpty():
                    model = full_model

                new_np = parent.attachNewNode(code)
                model.copyTo(new_np)
                self.parseNode(xml_node, new_np)
            except Exception as e:
                print(f"Failed to load landmark model {model_path} for code {code}: {e}")
        else:
            print(f"Warning: Landmark code {code} not found in storage.")
            dummy = parent.attachNewNode(xml_node.get('id', 'landmark'))
            self.parseNode(xml_node, dummy)

    def handleFlatBuilding(self, xml_node, parent):
        building = parent.attachNewNode("flat_building")
        width = float(xml_node.get('width', 10))
        
        # Add collision to flat buildings
        building.setCollideMask(BitMask32(1))
        
        self.parseNode(xml_node, building)

    def handleWall(self, xml_node, parent):
        code = xml_node.get('code')
        height = float(xml_node.get('height', 24) or 1000)
        width = float(xml_node.get('width', 20) or 255)
        if code in self.storage:
            entry = self.storage[code]
            model_path = entry['path']
            node_name = entry['node']
            if not model_path.endswith('.bam'):
                model_path += '.bam'
            try:
                full_model = loader.loadModel(model_path)
                if node_name:
                    model = full_model.find("**/" + node_name)
                else:
                    model = full_model.find("**/" + code)

                if model.isEmpty():
                    model = full_model

                new_np = parent.attachNewNode(code)
                model.copyTo(new_np)
                new_np.setSx(width)
                new_np.setSy(width)
                new_np.setSz(height)
                
                # Add collision to walls so players and cogs can't pass through
                new_np.setCollideMask(BitMask32(1))
                
                self.parseNode(xml_node, new_np)
            except Exception as e:
                print(f"Failed to load wall model {model_path} for code {code}: {e}")
        else:
            dummy = parent.attachNewNode("wall")
            # Add collision to placeholder walls too
            dummy.setCollideMask(BitMask32(1))
            self.parseNode(xml_node, dummy)

    def handleSign(self, xml_node, parent):
        sign_node = parent.find("**/sign_origin")
        if sign_node.isEmpty():
            # If no sign_origin, try to find generic sign node or attach to parent
            sign_node = parent.find("**/sign")
            if sign_node.isEmpty():
                sign_node = parent.attachNewNode("sign")
                # Set a default position if no sign_origin exists to prevent underground signs
                # Using a higher Z and slightly forward Y to be visible on generic buildings
                sign_node.setPos(0, -0.1, 10.0)

        code = xml_node.get('code')
        if code and code in self.storage:
            entry = self.storage[code]
            model_path = entry['path']
            node_name = entry['node']
            if not model_path.endswith('.bam'):
                model_path += '.bam'
            try:
                full_model = loader.loadModel(model_path)
                if node_name:
                    model = full_model.find("**/" + node_name)
                else:
                    model = full_model.find("**/" + code)

                if model.isEmpty():
                    model = full_model

                new_np = sign_node.attachNewNode(code)
                new_np.setPos(new_np, .5, -.5, 0)
                model.copyTo(new_np)
            except Exception as e:
                print(f"Failed to load sign model {model_path} for code {code}: {e}")

        self.parseNode(xml_node, sign_node)

    def handleBaseline(self, xml_node, parent):
        baseline_node = parent.attachNewNode("baseline")
        
        # Set depth write and test to prevent z-fighting with signs
        baseline_node.setDepthWrite(True)
        baseline_node.setDepthTest(True)
        
        # Put text in a later cull bin to ensure it renders in front of signs
        baseline_node.setBin('fixed', 45)  # Higher than default (0) and shadow (40)
        
        # Enable transparency for text to handle anti-aliasing properly
        baseline_node.setTransparency(TransparencyAttrib.MAlpha)

        text_node = xml_node.find('text')
        if text_node is not None and text_node.text:
            tn = TextNode('dna_text')
            tn.setText(text_node.text)

            try:
                # Try to get font from DNA attributes, otherwise use default
                font_code = xml_node.get('font', None)
                
                # Font mapping for different zones/contexts
                font_map = {
                    'mickey': 'phase_3/fonts/MickeyFont.ttf',
                    'minnie': 'phase_3/fonts/MinnieFont.ttf',
                    'mickey_classic': 'phase_3/fonts/MickeyFontMaximum.bam',
                    'mickey_maximum': 'phase_3/fonts/MickeyFontMaximum.bam',
                    'mickey_standard': 'phase_3/fonts/MickeyFontStandard.bam',
                    'comic': 'phase_3/fonts/Comic.ttf',
                    'humanist': 'phase_3/fonts/Humanist.ttf',
                    'jiggery': 'phase_3/fonts/JiggeryPokery.ttf',
                    'ironwork': 'phase_3/fonts/Ironwork.ttf',
                    'aftershock': 'phase_3/fonts/Aftershock.ttf',
                    'danger': 'phase_3/fonts/Danger.ttf',
                    'alibi': 'phase_3/fonts/Alie.ttf',
                    'remington': 'phase_3/fonts/vtRemingtonPortable.ttf',
                    'portago': 'phase_3/fonts/Portago.ttf',
                    'pudding': 'phase_3/fonts/HastyPudding.ttf',
                    'hasty': 'phase_3/fonts/HastyPudding.ttf',
                    'scurlock': 'phase_3/fonts/Scurlock.ttf',
                    'oyster': 'phase_3/fonts/OysterBar.ttf',
                    'reddog': 'phase_3/fonts/RedDogSaloon.ttf',
                    'kingpin': 'phase_3/fonts/Kingpin.ttf',
                    'default': 'phase_3/fonts/ImpressBT.ttf'
                }
                
                # Determine font path
                font_path = None
                if font_code:
                    f_code = font_code.lower()
                    if f_code in font_map:
                        font_path = font_map[f_code]
                    else:
                        # Try to find it by name in phase_3/fonts
                        potential_path = f"phase_3/fonts/{font_code}.ttf"
                        if os.path.exists(potential_path):
                            font_path = potential_path
                        else:
                            potential_path = f"phase_3/fonts/{font_code}.bam"
                            if os.path.exists(potential_path):
                                font_path = potential_path

                if not font_path:
                    font_path = font_map['default']
                
                if os.path.exists(font_path):
                    font = loader.loadFont(font_path)
                    if font:
                        tn.setFont(font)
                else:
                    print(f"Font file not found at {font_path}, trying default")
                    default_font = font_map['default']
                    if os.path.exists(default_font):
                        font = loader.loadFont(default_font)
                        if font:
                            tn.setFont(font)
            except Exception as e:
                print(f"Error loading font: {e}")

            np = baseline_node.attachNewNode(tn)
            # Adjust position to render properly in front of signs
            # Negative Y moves it closer to camera, slightly offset to prevent z-fighting
            np.setPos(np, -1, -0.15, 0)  # Adjusted depth for better text rendering
            np.setScale(.69)

        self.parseNode(xml_node, baseline_node)
