# Fix in order of importance

Fix/add these in order of importance for game design and a good game overall.

## Planned features...

* Make Trolley games really function.
* Make quest givers/takers really function (when you press q near the quest giving NPCs in Toontown Central, you cant turn in a task or get a task)

## Known Major Issues.

* ~~***DNA Loader*** DNA loading is a bit nutzo-buttso. (SOME text behind/blending in with signs or ahead of signs, depending on the sign. And some signs undergound.)
  - Text now renders in front of signs using depth write/test and cull bins
* ~~***Loading Zones*** Loading zone positions are WAY off in most areas EXCEPT FOR Toontown Central's playground and streets. They should be right in front of the tunnels, not behind/around them.
* ~~***COGS out of bounds*** COGS are out of bounds of streets and wont respect collisions even when they happen to go within bounds. This causes COGS to be out of bounds most of the time.

## Known slightly less major issues

* ~~***Zone Loading*** Since zone loading always teleports the player at a specific position instead of where we should be based on context of where we were before, therefore we are out of bounds in streets when loaded in.