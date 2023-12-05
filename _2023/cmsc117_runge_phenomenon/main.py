import numpy as np

from manim import *
from manim_slides import Slide

import polyinterp

class Presentation(Slide, ZoomedScene):
  def clear_all(self):
    animations = []
    for mobject in self.mobjects:
      if isinstance(mobject, Tex):
        animations.append(Unwrite(mobject))
      elif isinstance(mobject, VMobject):
        animations.append(Uncreate(mobject))
      else:
        animations.append(FadeOut(mobject))

    self.next_slide()
    self.play(LaggedStart(*animations, lag_ratio=0.5), run_time=1)
    self.wait(0.1)

  def construct(self):
    self.wait(0.1)
    self.play_introduction()
    self.play_polynomial_approximation()
    self.play_polynomial_interpolation_problem()
    self.play_lagrange_interpolation()
    self.play_runge_phenomenon()

  def play_introduction(self):
    func = lambda t: 2 * np.sin(t) + 2

    text = VGroup(
        Tex("Suppose we wanted to model the"),
        Tex("temperature", " $T$ " , "of a cat at any time", " $t$", ".")
      ).arrange(DOWN).scale(1.2)

    text[1][1].set_color(BLUE)

    self.next_slide()
    self.play(Write(text))
    self.play(text.animate.to_edge(UP).scale(0.8), run_time=1)

    axes = Axes(x_range=[-2, 5], y_range=[-2, 5]).scale(0.7).set_opacity(0.5)
    axes.next_to(text, DOWN, buff=LARGE_BUFF)
    labels = axes.get_axis_labels(x_label="t", y_label="T(t)")


    xs = np.linspace(1, 4, 3)
    ys = func(xs)
    points = VGroup(*[Dot(axes.coords_to_point(x, y), color=WHITE, radius=0.05) for x, y in zip(xs, ys)])

    interval = VGroup(
      DashedLine(dash_length=0.1, start=axes.coords_to_point(1, -2), end=axes.coords_to_point(1, 5), color=GRAY),
      DashedLine(dash_length=0.1, start=axes.coords_to_point(4, -2), end=axes.coords_to_point(4, 5), color=GRAY),
    )

    self.next_slide()

    self.play(
      Create(axes), 
      Create(interval), 
      Create(labels), 
    run_time=1)

    func_graph = axes.plot(func, color=BLUE)
    for x, y, point in zip(xs, ys, points):
      label = Tex(f"$({x:.2}, {y:.2})$").next_to(point, RIGHT, buff=0).scale(0.5)
      self.play(Create(point), FadeIn(label), run_time=0.2)
      self.wait(0.5)
      self.next_slide()
      self.play(FadeOut(label))

    self.next_slide()
    self.play(
      Transform(text, Tex("$T(t) = ??$").move_to(text)),
      Create(func_graph),
      run_time=1
    )
    self.wait(0.1)

    approx_graph = axes.plot(polyinterp.NewtonLagrangeInterpolation(func, xs), color=RED)

    self.next_slide()
    self.play(
      Transform(text, Tex(r"$p_n(t) \approx T(t)$").move_to(text)),
      Create(approx_graph),
      run_time=1
    )
    self.wait(0.1)

    err = axes.get_area(approx_graph, [1, 4], bounded_graph=func_graph, color=GRAY)
    self.next_slide()
    self.play(
      Transform(text, Tex(r"$|| T(t) - p_n(t) || < \epsilon$").move_to(text)),
      FadeIn(err),
      run_time=1
    )
    self.wait(0.1)

    self.clear_all()

  def play_polynomial_approximation(self):
    title = Title("Stone-Weierstrass Polynomial Approximation")

    s1 = Tex("Given a continuous function $f : [a,b] \\to \mathbb{R}$,").next_to(title, DOWN).scale(0.8)
    s2 = Tex("there exists $n = n(f, \epsilon) > 0$ and a polynomial $p_n \in \mathbb{R}_{n}[x]$ of degree $n$").next_to(s1, DOWN).scale(0.8)
    s3 = Tex("such that $||f - p_n|| < \epsilon$.").next_to(s2, DOWN).scale(0.8)

    axes = Axes(x_range=[-np.pi + 0.4, np.pi + 0.4], y_range=[-1, 1], tips=False).scale(0.6).next_to(s3, DOWN, buff=MED_LARGE_BUFF)
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
    self.clear_all()

  def play_polynomial_interpolation_problem(self):
    title = Title("Polynomial Interpolation Problem")

    text = Tex(
"""Given a continuous function $f : [a,b] \\to \mathbb{R}$ and $n$
distinct points $x_0, x_1, \dots, x_n$ in $[a,b]$, find a polynomial $p_n
\in \mathbb{R}_n[x]$ of degree $n$ such that $p_n(x_k) = f(x_k)$ for all $k
= 0, 1, \dots, n$."""
    ).next_to(title, DOWN).scale(0.7)

    axes = Axes(x_range=[-2, 2], y_range=[-2, 2], tips=False).next_to(text, DOWN).scale(0.8)

    func = lambda x: np.exp(-x**2)
    func_graph = axes.plot(func, color=BLUE)
    approx_graph = axes.plot(polyinterp.NewtonLagrangeInterpolation(func, np.linspace(-1, 1, 3)), color=RED)
    points = VGroup(*[Dot(axes.coords_to_point(x, func(x)), color=WHITE, radius=0.05) for x in np.linspace(-1, 1, 3)])

    self.play(
      LaggedStart(
        Write(title),
        Write(text),
        Create(axes),
        Create(func_graph, run_time=1),
        Create(points, run_time=1),
        Create(approx_graph, run_time=1),
        lag_ratio=0.5
      )
    )
    self.wait(0.1)

    self.clear_all()
    
  def play_lagrange_interpolation(self):
    code = """
def NewtonLagrangeInterpolation(f, x):
 n = len(x)
 d = np.zeros((n, n), dtype=float)
 d[:, 0] = f(x)
 for k in range(1, n):
   for l in range(k, n):
     d[l, k] = (d[l, k - 1] - d[l - 1, k - 1]) / (x[l] - x[l - k])

 def p(z):
   v = d[n - 1, n - 1]
   for k in range(1, n):
     v = v * (z - x[n - 1 - k]) + d[n - 1 - k, n - 1 - k]
   return v

 return p
"""
    rendered_code = Code(code=code, 
                         tab_width=4, 
                         background="window", 
                         language="Python", 
                         style="solarized-dark",
                         font="Monospace").scale(0.8)
    rendered_code.line_numbers.set_color(WHITE)
                        
    self.play(Create(rendered_code))
    self.next_slide()
    self.wait(0.1)

    self.clear_all()

    axes = Axes(x_range=[-2, 2], y_range=[-2, 2], tips=False)
    f = lambda x: np.exp(-x**2)
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

      num = MathTex(f"n = {n}").move_to(0.8 * axes.get_corner(UP + RIGHT)).scale(0.6)
      bg = BackgroundRectangle(num, color=BLACK, fill_opacity=0.5)


      points = VGroup(*[Dot(axes.coords_to_point(x, f(x)), color=WHITE, radius=0.05) for x in nodes])
      approx_graph = axes.plot(lagrange_func, color=ORANGE.interpolate(RED, (n-2)/9))

      for elem in [num, bg]:
        elem.set_z_index(approx_graph.z_index + 1)

      line = DashedLine(
        start=axes.coords_to_point(x_max, f(x_max)),
        end=axes.coords_to_point(x_max, lagrange_func(x_max))
        )
      err = MathTex(f"||f(x) - L_{{f, {n}}}|| = {round(supnorm, 6)}").next_to(num, DOWN).scale(0.6)

      if previous == {}:
        self.next_slide()
        self.play(
          LaggedStart(
            Create(bg),
            Write(num),
            Write(err),
            Create(line),
            Create(points),
            Create(approx_graph),
            lag_ratio=0.5
          ),
          run_time=0.75
        )
        
        previous["num"] = num
        previous["err"] = err
        previous["points"] = points
        previous["graph"] = approx_graph
      else:
        self.play(
          Transform(previous["num"], num),
          Transform(previous["err"], err),
          Transform(previous["points"], points),
          Transform(previous["graph"],  approx_graph),
          run_time=0.5
        )

      self.wait(0.1)

      self.next_slide()
      self.play(Uncreate(line), run_time=0.2)

    self.clear_all()

  def play_runge_phenomenon(self):
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

    self.clear_all()