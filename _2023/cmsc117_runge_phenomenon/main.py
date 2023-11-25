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
    axes = Axes(x_range=[-2, 2], y_range=[-2, 2])
    f = lambda x: 1/(1 + 25 * x ** 2)
    f_graph = axes.plot(f, color=BLUE)

    self.play(Create(axes), Create(f_graph, run_time=1))
    self.wait(0.1)

    self.next_slide()

    previous_num = None
    previous_points = None
    previous_graph = None
    previous_err  = None

    for n in range(2, 20):
      nodes = np.linspace(-1, 1, n)

      num = MathTex(f"n = {n}").move_to(0.8 * axes.get_corner(UP + RIGHT))
      err = MathTex(f"|| f(x) - p_{{{n-1}}} || = {0}").next_to(num, DOWN)

      points = VGroup(*[Dot(axes.coords_to_point(x, f(x)), color=GRAY) for x in nodes])
      approx_graph = axes.plot(
        NewtonLagrangeInterpolation(f, nodes),
        color=GREEN,
      )

      if previous_graph is None:
        self.play(Succession(Write(num), 
                             Write(err), 
                             Create(points), 
                             Create(approx_graph)))
        self.wait(0.1)

        previous_num = num
        previous_points = points
        previous_graph = approx_graph
        previous_err = err

      else:
        self.play(
          Transform(previous_num, num),
          Transform(previous_err, err),
          Transform(previous_points, points),
          Transform(previous_graph, approx_graph),
          run_time=0.5
        )

      self.next_slide()
      self.wait(0.1)

    self.play(
      Unwrite(previous_num),
      Uncreate(previous_points),
      Uncreate(previous_graph),
    )
    
    self.play(
      LaggedStart(
        Uncreate(f_graph),
        Uncreate(axes),
        lag_ratio=0.5,
      )
    )
    self.wait(0.1)
