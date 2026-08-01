# Fix in order of importance

Fix/add these in order of importance for game design and a good game overall.

## Future features...

* Make Trolley games really function - not just loading zone with random 3D model loaded in. (add objectives, etc.)
* Add a new COG type. (Sambots - lampooning/parodying me, NodeMixaholic aka Sammy L.)

## Remaining Issues

* ***DNA Loader*** DNA loading is a bit nutzo-buttso. (SOME signs underground.) - May be model-specific issues with sign_origin nodes
* ***Tasks*** Tasks/Quests don't turn into NPCs properly (it doesn't detect NPC in range wether i'm 6ft from the NPC or right on top of them.)
* ***Loading Zones*** Not all loading zones are correctly positioned.

## Completed Fixes (2026-02-15)

### Zone Name Mapping
* [x] Fixed zone name mapping in launch.py (zones 11, 12, 13 were incorrectly named - swapped Silly Street, Loopy Lane, Punchline Place)

### Loading Zone Positions
Some (not all) loading zones now use proper positions based on tunnel coordinates from DNA files:
* [x] TTC Playground (1.py) - Fixed loading zones for Punchline Place, Loopy Lane, Silly Street, Goofy Speedway
* [x] TTC Streets (11.py, 12.py, 13.py) - Loopy Lane, Punchline Place, Silly Street (except for tunnels going back to TTC.)

### Other Fixes
* [x] Fixed spawn positions (base.localAvatar.setPos) in all street zone files
* [x] Fixed entryPos and entryHpr values for proper spawn positions when traveling between zones
* [x] Fixed cogMgr typo in multiple zone files (was cog_mgr)
* [x] Updated server.py zoneBounds for COG spawning to match actual street layouts
* [x] Fixed Trolley timer issue - timer now properly stops when exiting via ESC key

## Loading Zone Technical Details

All loading zones now use the following formula:
- Zone rectangles (x1, y1, x2, y2) positioned in front of tunnel entrances
- Entry positions (entryPos) match the corresponding tunnel in the destination zone
- Entry heading (entryHpr) matches the tunnel's facing direction
- Calculated using: `python3 calculate_tunnels.py` to get actual tunnel positions from DNA files
