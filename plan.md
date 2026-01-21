# Fix in order of importance

Fix/add these in order of importance for game design and a good game overall.

## Future features...

* Add real Trolley games.
* Randomize Trolley games.
* One single Task giver in Toontown Central with tasks to do for fun.
* Hold "end" key to show tasks HUD, release to hide again - just like the original game.

## Known Major Issues.

* ***DNA Loader*** Fonts in Playground/Street/CogHQ DNA are set to a placeholder font instead of the corresponding fonts. (All fonts are in phase_3/fonts)
* ***DNA Loader*** DNA loading is a bit nutzo-buttso. (Flat walls not colliding, and some signs underground.)
* ***Loading Zones*** Loading zone positions are WAY off in most areas besides Toontown Central's playground and streets. They should be right in front of the tunnels, not behind/around them.

## Known slightly less major issues

* ***Zone Loading*** Since zone loading always teleports the player at 0,0,0 instead of where we should be based on context of where we were before, we go out of bounds in streets.
* ***COGS out of bounds*** COGS are out of bounds of streets and wont respect collisions even when they happen to go within bounds. This causes COGS to be out of bounds most of the time. This won't be a major issue until we are about to implement task system.

