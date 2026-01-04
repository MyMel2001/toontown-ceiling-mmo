from thirdparty.createToon.src.toon.CeilingToon import Toon 
from thirdparty.nametag.toonNametag import createNametag
toonDnaArray = [['mi', 'ss', False, 'ss', 'l', 'Blue', 'Red', 'Green', 'Red', '2019 Winter Laff-o-lympics Gold Medal', 'Beta Bug Hunter Shorts', 'Beta Bug Hunter Skirt', 'Amber', 'Aqua', None, None, 4, None, None, None, 'Neutral', True, False], ['ca', 'ls', False, 'ls', 'l', 'Cartoonival Blue', 'Cartoonival Blue', 'White', 'Cartoonival Blue', '2019 Winter Laff-o-lympics Bronze Medal', 'Bee Shorts', None, 'Amber', 'White', None, 'Aviator Shades', 1, None, None, 'Aqua Toon Boots', 'Neutral', True, False],['cr', 'ss', False, 'sd', 'm', 'Amber', 'Cartoonival Blue', 'White', 'Cartoonival Blue', None, None, None, 'White', 'White', None, None, 4, None, None, None, 'Neutral', True, False],['ri', 'ls', False, 'ss', 's', 'Black', 'Cartoonival Blue', 'White', 'Cartoonival Blue', None, None, None, 'White', 'White', None, None, 4, None, None, None, 'Neutral', True, False]] # Define your toons here! Each one should be it's own array nested inside instead of a Toon object.
toonNameArray = ["Poodletooth", "Gato", "Mr. Croc", "Cartoonie"]
npcArray = []

import builtins
def get_builtins():
  """Due to the way Python works, ``__builtins__`` can strangely be either a module or a dictionary,
  depending on whether the file is executed directly or as an import. I couldn’t care less about this
  detail, so here is a method that simply returns the namespace as a dictionary."""
  return builtins.__dict__

def getToon(array):
    return Toon(*array)

def createNPC(dnaArray,x,y,z,h,p,r,name):
    npc = Toon(*dnaArray)
    npc.toonActor.setPos(x,y,z)
    npc.toonActor.setHpr(h,p,r)
    head = npc.toonActor.findAllMatches('**/head*')
    nametag = createNametag(name, (1,1,1,.5), (1,1,0,1))
    nametag.setPos(0,0,3.2)
    nametag.reparentTo(head[0])
    npcArray.append(npc)
    npc.toonActor.reparentTo(render)
    return npc 

def destroyNPCS():
    for element in npcArray:
        if element.toonActor and not element.toonActor.isEmpty():
            element.toonActor.removeNode()
    npcArray.clear()

def pickAToon(num):
    global pickedToonArray
    pickedToonArray = toonDnaArray[num]
    G = get_builtins()
    G["PlayerName"] = toonNameArray[num]
    return getToon(pickedToonArray)
    
def defineToon():
    return pickAToon(3) #define what toon to be, starting at 0
