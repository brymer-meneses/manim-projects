from manim import *
from intro import _intro
from ratio_test import _ratio_test
from limit_test import _limit_test
from conclusion import _conclusion

class Presentation(Scene):
    def construct(self):
        _intro(self)
        _ratio_test(self)
        _limit_test(self)
        _conclusion(self)

if __name__ == "__main__":
    import os
    os.system("manim -pql main.py Presentation")