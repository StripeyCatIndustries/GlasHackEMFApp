import app
import sys
import os

from events.input import Buttons, BUTTON_TYPES

class GlasHackApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.font_size = 60
        ctx.rgb(1, 1, 1).move_to(-51, -50).text("glas")
        ctx.rgb(1, 1, 1).move_to(-60, 10).text("hack")
        ctx.rgb(1, 1, 1).move_to(-32, 75).text(".[ ]")
 
__app_export__ = GlasHackApp
