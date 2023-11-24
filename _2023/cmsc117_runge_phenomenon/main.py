import numpy as np
import polyinterp as pi

from manim import *
from manim_slides import Slide


class Presentation(Slide):
  def construct(self):
    self.wait(1)
    
    self.next_slide()
    self.play_introduction()

    self.next_slide()
    axes = Axes(
      x_range=[-1, 1, 0.05],
      y_range=[-1, 1, 0.05],
      x_length=10,
    )

    self._show_function(lambda x: np.sin(x), axes)
    # func = pi.NewtonLagrangeInterpolation(lambda x: np.sin(x), np.linspace(-1, 1, 10))
    # print(func(0.5))
    # self._show_function(func, axes)

    self.next_slide()
    self.wait(1)

  def play_introduction(self):
    text = Text("Introduction")
    self.play(Write(text))
    self.wait(1)
    self.play(Unwrite(text))

  def _show_function(self, f, axes):
    graph = axes.plot(f, color=BLUE)
    self.play(LaggedStart(Write(axes), Write(graph)))

if __name__ == "__main__":
  func = pi.NewtonLagrangeInterpolation(lambda x: np.sin(x), np.linspace(-1, 1, 10))
  print(func(0.5))
    
