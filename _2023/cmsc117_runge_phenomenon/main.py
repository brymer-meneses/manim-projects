import numpy as np

from manim import *
from manim_slides import Slide

import polyinterp

class Presentation(Slide, ZoomedScene):
  def construct(self):
    self.wait(0.1)

    self.play_introduction()
    self.play_polynomial_approximation()
    self.play_polynomial_interpolation_problem()
    self.play_newton_lagrange_interpolation()
    self.play_runge_phenomenon()

  def play_introduction(self):
    title = Text("Runge Phenomenon").scale(1.2).set_color_by_gradient(BLUE, GREEN)
    
    self.next_slide()
    self.play(Write(title), run_time=0.5)
    self.wait(0.1)

    self.next_slide()
    self.play(Unwrite(title), run_time=0.5)
    self.wait(0.1)
  
  def play_polynomial_approximation(self):
    title = Title("Stone-Weierstrass Polynomial Approximation")

    s1 = Tex("Given a continuous function $f : [a,b] \\to \mathbb{R}$,").next_to(title, DOWN).scale(0.8)
    s2 = Tex("there exists $n = n(f, \epsilon) > 0$ and a polynomial $p_n \in \mathbb{R}_{n}[x]$ of degree $n$").next_to(s1, DOWN).scale(0.8)
    s3 = Tex("such that $||f - p_n|| < \epsilon$.").next_to(s2, DOWN).scale(0.8)

    axes = Axes(x_range=[-np.pi + 0.4, np.pi + 0.4], y_range=[-1, 1], tips=False).scale(0.6).next_to(s3, DOWN)
    f = lambda x: np.sin(x)
    f_graph = axes.plot(f, color=BLUE)
    p_graph = axes.plot(polyinterp.NewtonLagrangeInterpolation(f, np.linspace(-np.pi, np.pi, 4)), color=RED)

    self.play(
      LaggedStart(
        Write(title),
        Write(s1),
        Create(axes),
        Create(f_graph, run_time=1),
        lag_ratio=0.5
      )
    )
    self.wait(0.1)

    self.next_slide()
    self.play(
        LaggedStart(
          Write(s2),
          Create(p_graph, run_time=1),
          lag_ratio=0.5
        )
      )
    self.wait(0.1)

    self.next_slide()
    self.play(
      LaggedStart(
        Write(s3),
        lag_ratio=0.5
        )
      )
    self.wait(0.1)
    
    self.next_slide()
    self.play(
      LaggedStart(
        Uncreate(axes),
        Uncreate(f_graph),
        Uncreate(p_graph),
        Unwrite(s3),
        Unwrite(s2),
        Unwrite(s1),
        Unwrite(title),
        lag_ratio=0.5
      ),
      run_time=1
    )
    self.wait(0.1)

  def play_polynomial_interpolation_problem(self):
    pass

  def play_newton_lagrange_interpolation(self):
    axes = Axes(x_range=[-2, 2], y_range=[-2, 2], tips=False)
    f = lambda x: 1/(1 + 25 * x ** 2)
    f_graph = axes.plot(f, color=BLUE)

    labels = axes.get_axis_labels()

    start_line = DashedLine(
      dash_length=0.1,
      start=axes.coords_to_point(1, -2),
      end=axes.coords_to_point(1, 2),
      color=GRAY
    )
    end_line = DashedLine(
      dash_length=0.1,
      start=axes.coords_to_point(-1, -2),
      end=axes.coords_to_point(-1, 2),
      color=GRAY
    )

    previous = {}

    self.play(Create(axes), 
              Create(start_line), 
              Create(end_line), 
              Create(labels), 
              Create(f_graph, run_time=1))
    self.wait(0.1)

    self.next_slide()

    for n in range(2, 12):
      nodes = np.linspace(-1, 1, n)

      lagrange_func = polyinterp.NewtonLagrangeInterpolation(f, nodes)
      x_max, supnorm = polyinterp.supnorm(lambda x: f(x) - lagrange_func(x), -1, 1, 1000)

      num = MathTex(f"n = {n}").move_to(0.8 * axes.get_corner(UP + RIGHT)).scale(0.8)
      bg = BackgroundRectangle(num, color=BLACK, fill_opacity=0.5)


      points = VGroup(*[Dot(axes.coords_to_point(x, f(x)), color=WHITE, radius=0.05) for x in nodes])
      approx_graph = axes.plot(lagrange_func, color=ORANGE.interpolate(RED, (n-2)/9))

      for elem in [num, bg]:
        elem.set_z_index(approx_graph.z_index + 1)

      line = DashedLine(
        start=axes.coords_to_point(x_max, f(x_max)),
        end=axes.coords_to_point(x_max, lagrange_func(x_max)))
      brace = Brace(line, direction=RIGHT)
      err = MathTex(f"{supnorm:0.5}").next_to(brace, RIGHT)

      if previous == {}:
        self.next_slide()
        self.play(
          LaggedStart(
            Create(bg),
            Write(num),
            Create(points),
            Create(approx_graph),
            lag_ratio=0.5
          ),
          run_time=0.75
        )
        
        previous["num"] = num
        previous["points"] = points
        previous["graph"] = approx_graph
      else:
        self.play(
          Transform(previous["num"], num),
          Transform(previous["points"], points),
          Transform(previous["graph"],  approx_graph),
          run_time=0.5
        )


      self.play(LaggedStart(
        Create(line),
        Write(err),
        Create(brace),
        ), run_time=0.2)
      self.wait(0.1)

      self.next_slide()
      self.play(
        Uncreate(line),
        Uncreate(brace),
        Unwrite(err),
        run_time=0.2
        )

    self.play(
      Unwrite(previous["num"]),
      Uncreate(previous["points"]),
      Uncreate(previous["graph"]),
    )
    
    self.play(
      LaggedStart(
        Uncreate(f_graph),
        Uncreate(axes),
        Uncreate(start_line),
        Uncreate(end_line),
        Uncreate(labels),
        lag_ratio=0.5,
      )
    )
    self.wait(0.1)

  def play_runge_phenomenon(self):
    pass