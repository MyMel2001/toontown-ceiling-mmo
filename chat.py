from direct.gui.DirectGui import *
from panda3d.core import *

class ChatManager:
    def __init__(self):
        self.chatLog = DirectScrolledFrame(
            canvasSize=(-1, 1, -10, 1),
            frameSize=(-1.3, 1.3, -0.4, 0.4),
            pos=(0, 0, -0.7),
            frameColor=(0, 0, 0, 0.3),
            parent=base.a2dTopLeft,
            scale=0.3
        )
        self.chatLog.setPos(0.4, 0, -0.15)
        
        self.entry = DirectEntry(
            scale=0.05,
            pos=(0, 0, 0.1),
            numLines=1,
            focus=0,
            command=self.sendChat,
            parent=base.a2dBottomCenter
        )
        
        self.messages = []
        base.accept("t", self.entry.setFocus)

    def sendChat(self, text):
        if not text: return
        self.entry.enterText("")
        self.entry.setFocus() # Keep focus after sending
        if hasattr(base, "net"):
            base.net.sendChat(text)

    def displayMessage(self, sender_id, text):
        name = "Unknown"
        if hasattr(base, "net"):
            name = base.net.playerNames.get(sender_id, f"Player {sender_id}")
            if sender_id == id(base.net.connection):
                name = "You"
        
        msg = f"{name}: {text}"
        self.messages.append(msg)
        
        # Update UI
        for child in self.chatLog.getCanvas().getChildren():
            child.removeNode()
            
        for i, m in enumerate(reversed(self.messages[-20:])):
            lbl = DirectLabel(
                text=m,
                scale=0.142,
                pos=(-0.9, 0, 0.8 - i*0.15),
                frameColor=(0,0,0,0),
                text_align=TextNode.ALeft,
                text_fg=(1,1,1,1),
                parent=self.chatLog.getCanvas()
            )
