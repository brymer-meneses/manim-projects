from manim import *

def _conclusion(self):
    conclusion = Tex("Thanks for Watching!").scale(2).set_color_by_gradient(BLUE, GREEN)
    self.play(Write(conclusion))
    self.wait(1)

    self.play(Unwrite(conclusion))
    self.wait(1)