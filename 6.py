import random
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *

G = get_builtins()

# Trolley Game Zone
print("[Trolley] Initializing game logic...")

# Setup game UI
title = DirectLabel(text="TROLLEY GAME", scale=0.15, pos=(0, 0, 0.8), 
                    frameColor=(0,0,0,0.5), text_fg=(1,1,1,1))

# Instructions
instr = DirectLabel(text="Use ARROW KEYS to move!\nPress ESC to exit game.", 
                    scale=0.07, pos=(0, 0, 0.6), 
                    frameColor=(0,0,0,0), text_fg=(1,1,0,1))

def exitGame():
    title.destroy()
    instr.destroy()
    base.ignore('escape')
    # Return to TTC Playground
    base.loadZone(1, entryPos=(-127, -65, 0.025), entryHpr=(90, 0, 0))

base.accept('escape', exitGame)

# Simple timer to auto-exit
def timerTask(task):
    if task.time > 30.0: # 30 second game
        exitGame()
        return task.done
    return task.cont

base.taskMgr.add(timerTask, "trolleyTimer")

# Background music
G["music"].stop()
G["music"] = loader.loadSfx('phase_4/audio/bgm/MG_SZ.ogg')
G["music"].setLoop(True)
G["music"].play()

print("[Trolley] Game ready!")