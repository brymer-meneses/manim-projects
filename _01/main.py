from manim import *
from limit_test import _limit_test
from ratio_test import _ratio_test
from intro import _intro

class Presentation(Scene):

    def construct(self):

        _intro(self)

        _ratio_test(self)
        # Limit Comparison Test
        _limit_test(self)

        # Conclusion

        conclusion = Title("Conclusion")
        self.play(Write(conclusion))
        self.wait(1)

        self.play(Unwrite(conclusion))
        self.wait(1)

if __name__ == "__main__":
    import os
    os.system("manim -pql main.py Presentation")
