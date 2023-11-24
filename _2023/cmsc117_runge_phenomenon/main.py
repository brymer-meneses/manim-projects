import numpy as np
import polyinterp as pi

from manim import *
from manim_slides import Slide

class Presentation(Slide):
  def construct(self):
    self.play_blank_slide()
    self.play_introduction()
    self.play_newton_lagrange_interpolation()

  def play_blank_slide(self):
    self.wait(1)
    self.next_slide()

  def play_introduction(self):
    text = Text("Runge Phenomenon").set_color_by_gradient(BLUE, GREEN).scale(1.5)
    self.play(Write(text))
    self.wait(1)

    self.next_slide()
    self.play(Unwrite(text))
    self.wait(1)

  def play_newton_lagrange_interpolation(self):
    axes = Axes(x_range=[-10, 10])
    func_graph = axes.plot(lambda x: np.sin(x), color=BLUE)

    self.play(LaggedStart(Create(axes), Create(func_graph), lag_ratio=0.5))
    self.wait(1)

    self.next_slide()
    approx_graph = axes.plot(
      pi.NewtonLagrangeInterpolation(
        lambda x: np.sin(x), np.linspace(-10, 10, 10)
      ),
      color=GREEN,
    )
    self.play(LaggedStart(Create(approx_graph), lag_ratio=0.5))
    self.wait(1)

    self.next_slide()
    self.play(
      LaggedStart(
        Uncreate(approx_graph),
        Uncreate(func_graph),
        Uncreate(axes),
        lag_ratio=0.5,
      )
    )
    self.wait(1)
