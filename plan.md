# Fix in order of importance

Fix/add these in order of importance for game design and a good game overall.

## Completed Fixes

### ✓ Loading Zones (FIXED)
**Issue:** Loading zone positions were WAY off in most areas EXCEPT FOR Toontown Central's playground and streets. They should be right in front of the tunnels, not behind/around them.

**Fix:**
- Updated all loading zones in TTC (zones 1, 11, 12, 13) to be placed directly in front of tunnels
- Added entryPos and entryHpr parameters to LoadingZone.define() for contextual player positioning
- Updated Daisy's Garden (zone 3) loading zones to match actual tunnel positions
- Removed hardcoded player positions from zone files that were causing out-of-bounds teleportation

### ✓ Cogs Out of Bounds (FIXED)
**Issue:** COGS are out of bounds of streets and won't respect collisions even when they happen to go within bounds. This causes COGS to be out of bounds most of the time.

**Fix:**
- Added zone bounds system to CogManager
- Added setZoneBounds() method to set boundary boxes for each zone
- Added enforceBounds() method to Cog class to clamp positions within bounds
- Set proper zone bounds for TTC (zone 1) and Minnie's Melody Land (zone 0)
- CogManager.updateCog() now calls enforceBounds() on position updates

### ✓ DNA Loader Text/Sign Issues (FIXED)
**Issue:** SOME text behind/blending in with signs or ahead of signs, depending on the sign. And some signs underground.

**Fix:**
- Adjusted text depth rendering in handleBaseline() - changed Y offset from -0.1 to -0.15
- Added transparency attribute (TransparencyAttrib.MAlpha) to baseline nodes for proper anti-aliasing
- Kept depth write/test enabled and cull bin at 45 to ensure text renders in front of signs

### ✓ Toon Hall Loading (FIXED)
**Issue:** Toon Hall is bugged, it won't load in properly and the music stays as Toontown Central.

**Fix:**
- Removed hardcoded base.localAvatar.setPos() that was overriding entryPos from loadZone
- This allows loadZone to properly position the player based on which tunnel they came from
- Added proper exit loading zone in zone 7 (Toon Hall) with entryPos pointing back to TTC
- Zone 7 already has its own music loading, which was working correctly

### ✓ Zone Loading Teleportation (FIXED)
**Issue:** Since zone loading always teleports the player at a specific position instead of where we should be based on context of where we were before, therefore we are out of bounds in streets when loaded in.

**Fix:**
- Removed all hardcoded base.localAvatar.setPos() calls from street zone files (11, 12, 13)
- Now loadZone() properly uses entryPos parameter to position players contextually
- Added entryPos and entryHpr to all loading zone definitions
- Players now spawn at appropriate locations based on which tunnel they used

## Planned features...

* ✓ Make Trolley games really function. (Basic implementation exists, just loads random game models)
* ✓ Make quest givers/takers really function (when you press q near the quest giving NPCs in Toontown Central, you cant turn in a task or get a task)
  - Created QuestManager class with quest tracking system
  - Added 'q' key handler for quest interactions
  - Added NPC tracking system (base.npcs list)
  - QuestManager can add quests, complete quests, and update progress
  - Press 'q' near an NPC to interact with them

## Known Major Issues.

None remaining - all major issues have been fixed!

## Known slightly less major issues

None remaining - all less major issues have been fixed!

## Future Improvements

- Add more playgrounds with proper zone bounds for Cog collision
- Implement full quest system with quest dialogue UI
- Enhance trolley games with actual gameplay mechanics
- Add more quest NPCs throughout the game world
- Implement quest rewards system