import xml.etree.ElementTree as ET
from panda3d.core import NodePath, Vec3

def parse_node(xml_node, panda_node):
    for child in xml_node:
        if child.tag in ['prop', 'group', 'visgroup', 'landmark_building', 'flat_building', 'node', 'street']:
            name = child.get('name', child.get('code', child.get('id', child.tag)))
            new_np = panda_node.attachNewNode(name)
            parse_node(child, new_np)
        elif child.tag == 'pos':
            panda_node.setPos(float(child.get('x', 0)), float(child.get('y', 0)), float(child.get('z', 0)))
        elif child.tag in ['nhpr', 'hpr']:
            panda_node.setHpr(float(child.get('h', 0)), float(child.get('p', 0)), float(child.get('r', 0)))

def get_tunnels(path):
    tree = ET.parse(path)
    root = tree.getroot()
    scene = NodePath("scene")
    parse_node(root, scene)
    
    tunnels = []
    # Find all tunnel nodes
    for np in scene.findAllMatches("**/linktunnel*"):
        pos = np.getPos(scene)
        hpr = np.getHpr(scene)
        tunnels.append((np.getName(), pos, hpr))
    
    # Also look for Goofy Speedway tunnel in TTC
    for np in scene.findAllMatches("**/prop_GS_tunnel*"):
        pos = np.getPos(scene)
        hpr = np.getHpr(scene)
        tunnels.append((np.getName(), pos, hpr))

    # Also look for Outdoor Zone entrance in DD
    for np in scene.findAllMatches("**/prop_outdoor_zone_entrance*"):
        pos = np.getPos(scene)
        hpr = np.getHpr(scene)
        tunnels.append((np.getName(), pos, hpr))
        
    return tunnels

dna_files = [
    ('MML', 'phase_6/dna/minnies_melody_land_sz.xml'),
    ('TTC', 'phase_4/dna/toontown_central_sz.xml'),
    ('DD', 'phase_6/dna/donalds_dock_sz.xml'),
    ('DG', 'phase_8/dna/daisys_garden_sz.xml'),
    ('BR', 'phase_8/dna/the_burrrgh_sz.xml'),
    ('DL', 'phase_8/dna/donalds_dreamland_sz.xml'),
    ('CashHQ', 'phase_10/dna/cog_hq_cashbot_sz.xml'),
    ('SellHQ', 'phase_9/dna/cog_hq_sellbot_sz.xml'),
    ('LawHQ', 'phase_11/dna/cog_hq_lawbot_sz.xml'),
    ('BossHQ', 'phase_12/dna/cog_hq_bossbot_sz.xml'),
    # TTC Streets
    ('LoopyLane', 'phase_5/dna/toontown_central_2100.xml'),
    ('PunchlinePlace', 'phase_5/dna/toontown_central_2200.xml'),
    ('SillyStreet', 'phase_5/dna/toontown_central_2300.xml'),
    # DD Streets
    ('BarnacleBlvd', 'phase_6/dna/donalds_dock_1100.xml'),
    ('SeaweedSt', 'phase_6/dna/donalds_dock_1200.xml'),
    ('LighthouseLane', 'phase_6/dna/donalds_dock_1300.xml'),
    # MM Streets
    ('TenorTerrace', 'phase_6/dna/minnies_melody_land_4100.xml'),
    ('AltoAve', 'phase_6/dna/minnies_melody_land_4200.xml'),
    ('BaritoneBlvd', 'phase_6/dna/minnies_melody_land_4300.xml'),
    # DG Streets
    ('ElmSt', 'phase_8/dna/daisys_garden_5100.xml'),
    ('LabyrinthLane', 'phase_8/dna/daisys_garden_5200.xml'),
    ('OakSt', 'phase_8/dna/daisys_garden_5300.xml'),
    # BR Streets
    ('WalrusWay', 'phase_8/dna/the_burrrgh_3100.xml'),
    ('SleetSt', 'phase_8/dna/the_burrrgh_3200.xml'),
    ('PolarPlace', 'phase_8/dna/the_burrrgh_3300.xml'),
    # DL Streets
    ('LullabyLane', 'phase_8/dna/donalds_dreamland_9100.xml'),
    ('PajamaPlace', 'phase_8/dna/donalds_dreamland_9200.xml'),
]

for name, path in dna_files:
    print(f"\n--- {name} ({path}) ---")
    try:
        tunnels = get_tunnels(path)
        for t_name, pos, hpr in tunnels:
            print(f"Tunnel: {t_name}")
            print(f"  Pos: {pos}")
            print(f"  Hpr: {hpr}")
    except Exception as e:
        print(f"  Error: {e}")
