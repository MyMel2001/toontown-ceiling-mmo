import xml.etree.ElementTree as ET
from panda3d.core import *
from direct.actor.Actor import Actor

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
                # Visgroups usually have their own pos/hpr
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
            # Create a dummy node to hold transform
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
        # We don't really use width yet but we could scale the walls
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
                # Walls are often composed of several heights, 
                # but Toontown DNA uses scaling to achieve height.
                new_np.setSx(width) # Assume base width is 20
                new_np.setSy(width) # Assume base width is 20
                new_np.setSz(height) # Assume base height is 24
                self.parseNode(xml_node, new_np)
            except Exception as e:
                print(f"Failed to load wall model {model_path} for code {code}: {e}")
        else:
            dummy = parent.attachNewNode("wall")
            self.parseNode(xml_node, dummy)

    def handleSign(self, xml_node, parent):
        sign_node = parent.find("**/sign_origin")
        if sign_node.isEmpty():
            sign_node = parent.attachNewNode("sign")
        
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
        
        # Toontown baselines can have text
        text_node = xml_node.find('text')
        if text_node is not None and text_node.text:
            tn = TextNode('dna_text')
            tn.setText(text_node.text)
            
            # Load default Toontown font
            try:
                font = loader.loadFont('phase_3/fonts/Comic.ttf')
                if font:
                    tn.setFont(font)
            except:
                pass

            np = baseline_node.attachNewNode(tn)
            np.setPos(np, -1, -1, 0)
            np.setScale(.69) # Default scale for text
        
        self.parseNode(xml_node, baseline_node)
