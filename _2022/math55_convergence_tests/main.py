from manim import *
from intro import _intro
from ratio_test import _ratio_test
from limit_test import _limit_test
from conclusion import _conclusion

class Presentation(Scene):
    def construct(self):
        self.next_section("Intro", skip_animations=False)
        _intro(self)

        self.next_section("Ratio Test", skip_animations=False)
        _ratio_test(self)
        
        self.next_section("Limit Test", skip_animations=False)
        _limit_test(self)

        self.next_section("Conclusion", skip_animations=False)
        _conclusion(self)

if __name__ == "__main__":
    import os
    os.system("manim -qh main.py Presentation")
