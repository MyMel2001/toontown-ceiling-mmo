# Fix in order of importance

Fix/add these in order of importance for game design and a good game overall.

## Future features...

* Make Trolley games really function.

## Known Major Issues.

* ***DNA Loader*** Fonts in Playground/Street/CogHQ DNA are set to a placeholder font instead of the corresponding fonts. (All fonts are in phase_3/fonts). No, this isn't properly implemented yet, although several attempts have been made.
* ***DNA Loader*** DNA loading is a bit nutzo-buttso. (SOME signs underground.)
* ***Loading Zones*** Loading zone positions are WAY off in most areas EXCEPT FOR Toontown Central's playground and streets. They should be right in front of the tunnels, not behind/around them.
* ***COGS out of bounds*** COGS are out of bounds of streets and wont respect collisions even when they happen to go within bounds. This causes COGS to be out of bounds most of the time. This won't be a major issue until we are about to implement task system.

## Known slightly less major issues

* ***Zone Loading*** Since zone loading always teleports the player at a specific position instead of where we should be based on context of where we were before, we are out of bounds in streets when first loaded in.

