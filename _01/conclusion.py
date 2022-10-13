from manim import *

def _conclusion(self):
    conclusion = Title("Conclusion")
    self.play(Write(conclusion))
    self.wait(1)

    self.play(Unwrite(conclusion))
    self.wait(1)