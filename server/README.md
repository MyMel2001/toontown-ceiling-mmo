# Toontown Ceiling MMO (Server-side)

This is a lightweight multiplayer game server for a Toontown-style game built with Panda3D networking. It runs headless (no graphics) and manages players, zones, NPC enemies (“Cogs”), movement, chat, and simple battles over TCP on port 1913.

Core architecture:
- Uses Panda3D’s `QueuedConnectionManager`, `QueuedConnectionListener`, `QueuedConnectionReader`, and `ConnectionWriter` for networking.
- Main server class: `ToontownServer(ShowBase)`.
- Maintains:
  - `clients`: connected player state (`name`, `dna`, `zone`, `position`, animation, etc.)
  - `cogs`: NPC enemies grouped by zone
  - stable per-connection integer IDs (`connIds`)
- Runs 3 recurring tasks:
  - `listenTask`: accepts new TCP clients
  - `readTask`: processes incoming packets/disconnects
  - `cogUpdateTask`: updates Cog AI movement
- Made to combine the chaos of Toontown Injector exploiters around 2013 (minus remote shell exploits) with the pure humor that was Toontown House.

Zone system:
- World is divided into numeric zone IDs.
- `zoneBounds` defines rectangular movement/spawn bounds per zone.
- Safe zones/playgrounds do not spawn enemies.
- Players only receive updates for entities in the same zone.

Networking protocol (packet IDs):
- `1` LOGIN
- `2` PLAYER POSITION UPDATE
- `3` ZONE CHANGE
- `4` CHAT
- `5` PLAYER SPAWN
- `6` PLAYER DESPAWN
- `7` COG SPAWN
- `8` COG POSITION UPDATE
- `9` BATTLE START / REQUEST
- `10` BATTLE ACTION
- `11` COG DESPAWN
- `12` BATTLE UPDATE

Player flow:
1. Client logs in with name, DNA/avatar data, zone, position, rotation.
2. Server stores player state.
3. Existing players and Cogs in the zone are sent to the new player.
4. Other players in the zone are notified of the new player spawn.
5. Position updates and chat are broadcast only within the same zone.
6. Zone changes despawn/resync entities between zones.
7. Disconnects remove the player and release any active battle ownership.

Cog (enemy NPC) system:
- Cogs are lazily spawned per zone when players enter.
- Each Cog has:
  - name/type/level
  - HP/max HP
  - position + target position
  - heading (`h`)
  - battle state
- 5–8 Cogs spawn per active non-safe zone.
- AI is a simple random-walk:
  - move toward a target point
  - pick a new random target when reached
  - clamp movement inside zone bounds
- Cog positions are broadcast every update tick.

Battle system:
- A player can request battle ownership of a Cog.
- Cog enters `inBattle=True` and stores owning player ID.
- Battle actions apply damage directly to Cog HP.
- On death:
  - battle update is broadcast
  - Cog despawns after 2 seconds
  - replacement Cog respawns after 10 seconds
- If a player disconnects or changes zone, owned Cogs are released from battle.

Important implementation notes:
- No authentication/security/validation.
- No persistence/database.
- No threading; everything runs in Panda3D task loop.
- Server trusts client movement and damage values.
- Cog updates are broadcast every tick, which may be bandwidth-heavy.
- Data serialization is manual via `NetDatagram`.
- Architecture is authoritative only for entity replication/state distribution, not anti-cheat.
