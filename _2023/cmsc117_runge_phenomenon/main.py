import numpy as np

from manim import *
from manim_slides import Slide

from polyinterp import NewtonLagrangeInterpolation

class Presentation(Slide):
  def construct(self):
    self.play_blank_slide()
    self.play_introduction()
    self.play_newton_lagrange_interpolation()

  def play_blank_slide(self):
    self.wait(0.1)
    self.next_slide()

  def play_introduction(self):
    text = Text("Runge Phenomenon").set_color_by_gradient(BLUE, GREEN).scale(1.5)

    self.play(Write(text), run_time=0.5)
    self.wait(0.1)

    self.next_slide()
    self.play(Unwrite(text), run_time=0.5)
    self.wait(0.1)

  def play_newton_lagrange_interpolation(self):
    axes = Axes(x_range=[-10, 10])
    f = lambda x: np.sin(x)
    f_graph = axes.plot(f, color=BLUE)

    self.play(Create(axes), Create(f_graph, run_time=1))
    self.wait(0.1)

    self.next_slide()
    for n in [5, 10, 15, 20, 25]:
      nodes = np.linspace(-10, 10, n)
      points = VGroup(*[Dot(axes.coords_to_point(x, f(x))) for x in nodes])
      approx_graph = axes.plot(
        NewtonLagrangeInterpolation(f, nodes),
        color=GREEN,
      )

      self.play(Succession(Create(points), Create(approx_graph)))
      self.wait(0.1)

      self.next_slide()
      self.play(
        FadeOut(points),
        Uncreate(approx_graph),
      )
      self.wait(1)
    
    self.play(
      LaggedStart(
        Uncreate(f_graph),
        Uncreate(axes),
        lag_ratio=0.5,
      )
    )
    self.wait(0.1)
