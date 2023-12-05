import numpy as np

from manim import *
from manim_slides import Slide

import polyinterp

class Presentation(Slide, ZoomedScene):
  def clear_all(self, except_mobjects=[]):
    animations = []
    for mobject in self.mobjects:
      if mobject in except_mobjects:
        continue
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
    self.play_mitigation()
    self.play_ending()
    
  def play_introduction(self):
    func = lambda t: 2 * np.sin(t) + 2

    text = VGroup(
        Tex(
          "Suppose we wanted to approximate a function $f$",
          substrings_to_isolate=["$f$"],
          tex_to_color_map={"$f$": BLUE},
        ),
        Tex("for any value $x$ given the following points:"),
      ).arrange(DOWN).scale(1.2)
    
    self.next_slide()
    self.play(Write(text))
    self.wait(0.1)

    self.next_slide()
    self.play(text.animate.to_edge(UP).scale(0.8), run_time=1)

    axes = Axes(x_range=[-2, 5], y_range=[-2, 5]).scale(0.7).set_opacity(0.5)
    axes.next_to(text, DOWN, buff=LARGE_BUFF)
    labels = axes.get_axis_labels(
      x_label=Tex("$x$"),
      y_label=Tex("$f(x)$", color=BLUE)
    )

    xs = np.linspace(1, 4, 3)
    ys = func(xs)
    points = VGroup(*[Dot(axes.coords_to_point(x, y), color=WHITE, radius=0.05) for x, y in zip(xs, ys)])

    interval = VGroup(
      DashedLine(dash_length=0.1, start=axes.coords_to_point(1, -2), end=axes.coords_to_point(1, 5), color=GRAY),
      DashedLine(dash_length=0.1, start=axes.coords_to_point(4, -2), end=axes.coords_to_point(4, 5), color=GRAY),
    )

    self.play(
      Create(axes), 
      Create(interval), 
      Create(labels), 
      run_time=1
    )

    func_graph = axes.plot(func, color=BLUE)
    for x, y, point in zip(xs, ys, points):
      label = Tex(f"$({x:.2}, {y:.2})$").next_to(point, RIGHT, buff=0).scale(0.5)
      self.play(Create(point), FadeIn(label), run_time=0.2)
      self.wait(0.1)
      self.next_slide()
      self.play(FadeOut(label))

    self.next_slide()
    self.play(
      Transform(
        text,
        MathTex(
          r"f(x) = \; ??",
          substrings_to_isolate=["f(x)"],
          tex_to_color_map={"f(x)": BLUE},
        ).move_to(text)
      ),
      Create(func_graph),
      run_time=1
    )
    self.wait(0.1)

    approx_graph = axes.plot(polyinterp.NewtonLagrangeInterpolation(func, xs), color=RED)

    self.next_slide()
    self.play(
      Transform(
        text,
        MathTex(
          r"p_n(x) \approx f(x)",
          substrings_to_isolate=["f(x)", "p_n(x)"],
          tex_to_color_map={"f(x)": BLUE, "p_n(x)": RED},
        ).move_to(text)
      ),
      Create(approx_graph),
      run_time=1
    )
    self.wait(0.1)

    err = axes.get_area(approx_graph, [1, 4], bounded_graph=func_graph, color=YELLOW, opacity=0.2)
    self.next_slide()
    self.play(
      Transform(
        text,
        MathTex(
          r"||f - p_n|| < \epsilon",
          substrings_to_isolate=["f", "p_n"],
          tex_to_color_map={"f": BLUE, "p_n": RED},
        ).move_to(text)),
      FadeIn(err),
      run_time=1
    )
    self.wait(0.1)

    self.clear_all()


  def play_polynomial_approximation(self):
    title = Title("Stone-Weierstrass Polynomial Approximation")

    s1 = Tex(
      "Given a continuous function $f$$: [a,b] \\to \mathbb{R}$ and $\epsilon > 0$,",
      substrings_to_isolate=["$f$"],
      tex_to_color_map={"$f$": BLUE},
    ).next_to(title, DOWN).scale(0.8)
    s2 = Tex(
      "there exists $n = n($$f$$, \epsilon) > 0$ and a polynomial $p_n$ $\in \mathbb{R}_{n}[x]$ of degree $n$",
      substrings_to_isolate=["$f$", "$p_n$"],
      tex_to_color_map={"$f$": BLUE, "$p_n$": RED},
    ).next_to(s1, DOWN).scale(0.8)
    s3 = Tex(
      "such that $||$$f$ $-$ $p_n$$||_{\infty} < \epsilon$.",
      substrings_to_isolate=["$f$", "$p_n$"],
      tex_to_color_map={"$f$": BLUE, "$p_n$": RED},
    ).next_to(s2, DOWN).scale(0.8)
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
"""Given a continuous function $f$ $ : [a,b] \\to \mathbb{R}$ and $n$
distinct points $x_0, x_1, \dots, x_n$ in $[a,b]$, find a polynomial $p_n$
$\in \mathbb{R}_n[x]$ of degree $n$ such that $p_n(x_k)$ $ = $ $f(x_k)$ for all $k
= 0, 1, \dots, n$.""",
      substrings_to_isolate=["$f$", "$p_n$", "$p_n(x_k)$", "$f(x_k)$"],
      tex_to_color_map={"$f$": BLUE, "$p_n$": RED, "$p_n(x_k)$": RED, "$f(x_k)$": BLUE}
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
        lag_ratio=0.5
      )
    )
    self.wait(0.1)
    
    self.next_slide()
    self.play(
      LaggedStart(
        Create(points),
        lag_ratio=0.5
      )
    )
    self.wait(0.1)

    self.next_slide()
    for point in points:
      self.play(Flash(point))
      self.wait(0.1)
      self.next_slide()
    
    self.play(
      LaggedStart(
        Create(approx_graph),
        lag_ratio=0.5
      )
    )
    self.wait(0.1)

    self.clear_all()
  
  def play_lagrange_interpolation(self):
    title = Title("Lagrange Polynomial")

    text = Tex(
"""Given a continuous function $f$ $: [a,b] \\to \mathbb{R}$ and $n$
distinct points $x_0, x_1, \dots, x_n$ in $[a,b]$, the Lagrange polynomial
$L_{f, n}$ $\in \mathbb{R}_n[x]$ is defined by""",
      substrings_to_isolate=["$f$", "$L_{f, n}$"],
      tex_to_color_map={"$f$": BLUE, "$L_{f, n}$": RED}
    ).next_to(title, DOWN).scale(0.7)

    lagrange_poly = MathTex(
      r"L_{f, n}(x) = \sum_{k = 0}^n f(x_k) \prod_{\substack{j = 0 \\ j \neq k}}^n \frac{x - x_j}{x_k - x_j}",
      substrings_to_isolate=[r"\frac{x - x_j}{x_k - x_j}", "f", "L_{f, n}"],
      tex_to_color_map={"f": BLUE, "L_{f, n}": RED, r"\frac{x - x_j}{x_k - x_j}": WHITE}
    ).next_to(text, DOWN)
    self.play(
      LaggedStart(
        Write(title),
        Write(text),
        Write(lagrange_poly),
        lag_ratio=0.5
      )
    )
    self.wait(0.1)

    self.next_slide()
    self.play(
      Unwrite(text),
      Unwrite(lagrange_poly),
      run_time=0.5
    )
    self.wait(0.1)

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
                         font="Monospace").scale(0.8).next_to(title, DOWN)
    rendered_code.line_numbers.set_color(WHITE)
                        
    self.play(Create(rendered_code))
    self.wait(0.1)

    self.clear_all()

    self.play_lagrange_graph()

  def play_lagrange_graph(self):
    function = VGroup(
      Tex("Consider the function"),
      MathTex(r"f(x)=e^{-x^2}",
        substrings_to_isolate=["f"],
        tex_to_color_map={"f": BLUE}
      ),
    ).arrange(DOWN).set_z_index(110)

    axes = Axes(x_range=[-2, 2], y_range=[-2, 2], tips=False).scale(0.8)

    self.play(Write(function))
    self.next_slide()
    self.play(Unwrite(function[0]))
    self.play(function[1].animate.move_to(0.8 * axes.get_corner(UP + LEFT)).scale(.6))
    bg1 = BackgroundRectangle(function[1], fill_opacity=0.5).set_z_index(100)

    self.play(FadeIn(bg1))
    
    f = lambda x: np.exp(-x**2)
    f_graph = axes.plot(f, color=BLUE)

    labels = axes.get_axis_labels()

    start_line = DashedLine(
      dash_length=0.1,
      start=axes.coords_to_point(1, -2),
      end=axes.coords_to_point(1, 2),
      color=GRAY,
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
              Create(MathTex("-1").next_to(start_line, DOWN).scale(0.6)),
              Create(MathTex("1").next_to(end_line, DOWN).scale(0.6)),
              Create(labels), 
              Create(f_graph, run_time=1))
    self.wait(0.1)

    self.next_slide()

    for n in range(2, 12):
      nodes = np.linspace(-1, 1, n)

      lagrange_func = polyinterp.NewtonLagrangeInterpolation(f, nodes)
      x_max, supnorm = polyinterp.supnorm(lambda x: f(x) - lagrange_func(x), -1, 1, 1000)

      num = MathTex(f"n = {n}").move_to(0.8 * axes.get_corner(UP + RIGHT)).scale(0.6)
      err = MathTex(
        f"||f - L_{{f, n}}||_\infty = {supnorm:.5f}",
        substrings_to_isolate=["f", "L_{f, n}", "\infty"],
        tex_to_color_map={"f": BLUE, "L_{f, n}": RED, "\infty": WHITE}
      ).next_to(num, DOWN).scale(0.6)
      bg = BackgroundRectangle(VGroup(num,err), color=BLACK, fill_opacity=0.5)

      points = VGroup(*[Dot(axes.coords_to_point(x, f(x)), color=WHITE, radius=0.05) for x in nodes])
      approx_graph = axes.plot(lagrange_func, color=ORANGE.interpolate(RED, (n-2)/9))

      for elem in [num, err, bg]:
        elem.set_z_index(100)

      line = DashedLine(
        start=axes.coords_to_point(x_max, f(x_max)),
        end=axes.coords_to_point(x_max, lagrange_func(x_max))
      )

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

    question = Tex(r"Is it true that for any $f : [a,b] \to \mathbb{R}$, will \\ $||f - L_{f, n}||_\infty \to 0$ when $n \to \infty$?")
    bg = BackgroundRectangle(question, buff=MED_LARGE_BUFF)

    self.play(
      LaggedStart(
        Create(bg),
        Write(question),
        lag_ratio=0.5
      ),
      run_time=1
    )
    self.wait(0.1)
    
    self.clear_all()

  def play_runge_phenomenon(self):
    text = VGroup(
      Tex("Unfortunately, the answer is no!").scale(1.4).set_color_by_gradient(ORANGE, RED),
      Tex(r"It can be shown that for equally spaced nodes including the endpoints, \\ a function $f$ may result to $||f - L_{f,n}||_\infty \to \infty$ as $n \to \infty$. "),
      Tex(r"This is called the ", "Runge's Phenonenon", "!")
    ).arrange(DOWN).scale(0.8)

    self.play(Write(text))
    self.play(text[2][1].animate.set_color_by_gradient(BLUE, GREEN), run_time=0.5)

    self.next_slide()
    self.play(
      Succession(
        Unwrite(text[0]),
        Unwrite(text[1]),
        LaggedStart(text[2].animate.to_edge(UP))
      )
    )

    runge_image = ImageMobject("assets/runge.jpeg").next_to(text[2], DOWN, buff=MED_SMALL_BUFF)
    runge_name = Tex("Carl David Tolmé Runge (1856 - 1927)").next_to(runge_image, DOWN)

    self.play(
      LaggedStart(
        GrowFromCenter(runge_image),
        Write(runge_name),
        lag_ratio=0.5
      )
    )
    self.wait(0.1)

    self.next_slide()
    self.play(
      Unwrite(text),
      Unwrite(runge_name),
      FadeOut(runge_image),
      run_time=0.5
    )

    function = VGroup(
      Tex("Consider the function"),
      MathTex(r"f", r"(x)=\frac{1}{1 + 25x^2}"),
    ).arrange(DOWN).set_z_index(110)

    function[1][0].set_color(BLUE)

    axes = Axes(x_range=[-2, 2], y_range=[-1, 1.5], tips=False).scale(0.8)

    self.play(Write(function))
    self.next_slide()
    self.play(Unwrite(function[0]))
    self.play(function[1].animate.move_to(0.8 * axes.get_corner(UP + LEFT)).scale(.6))
    bg1 = BackgroundRectangle(function[1], fill_opacity=0.5).set_z_index(100)

    self.play(FadeIn(bg1))

    f = lambda x: 1/(1 + 25 * x ** 2)
    f_graph = axes.plot(f, color=BLUE)

    labels = axes.get_axis_labels()

    start_line = DashedLine(
      dash_length=0.1,
      start=axes.coords_to_point(1, -1),
      end=axes.coords_to_point(1, 1),
      color=GRAY
    )
    end_line = DashedLine(
      dash_length=0.1,
      start=axes.coords_to_point(-1, -1),
      end=axes.coords_to_point(-1, 1),
      color=GRAY
    )

    previous = {}

    self.play(Create(axes), 
              Create(start_line), 
              Create(end_line), 
              Create(MathTex("-1").next_to(start_line, DOWN).scale(0.6)),
              Create(MathTex("1").next_to(end_line, DOWN).scale(0.6)),
              Create(labels), 
              Create(f_graph, run_time=1))
    self.wait(0.1)

    self.next_slide()

    for n in range(2, 12):
      nodes = np.linspace(-1, 1, n)

      lagrange_func = polyinterp.NewtonLagrangeInterpolation(f, nodes)
      x_max, supnorm = polyinterp.supnorm(lambda x: f(x) - lagrange_func(x), -1, 1, 1000)

      num = MathTex(f"n = {n}").move_to(0.8 * axes.get_corner(UP + RIGHT)).scale(0.6)
      err = MathTex(
        f"||f - L_{{f, n}}||_\infty = {supnorm:.5f}",
        substrings_to_isolate=["f", "L_{f, n}", "\infty"],
        tex_to_color_map={"f": BLUE, "L_{f, n}": ORANGE.interpolate(RED, (n-2)/9), "\infty": WHITE}
      ).next_to(num, DOWN).scale(0.6)
      bg = BackgroundRectangle(VGroup(num, err), color=BLACK, fill_opacity=0.5)

      points = VGroup(*[Dot(axes.coords_to_point(x, f(x)), color=WHITE, radius=0.05) for x in nodes])
      approx_graph = axes.plot(lagrange_func, color=ORANGE.interpolate(RED, (n-2)/9))

      for elem in [num, err, bg]:
        elem.set_z_index(approx_graph.z_index + 1)

      line = DashedLine(
        start=axes.coords_to_point(x_max, f(x_max)),
        end=axes.coords_to_point(x_max, lagrange_func(x_max)))

      if previous == {}:
        self.next_slide()
        self.play(
          LaggedStart(
            Create(line),
            Create(bg),
            Write(num),
            Write(err),
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
          Create(line),
          Transform(previous["num"], num),
          Transform(previous["err"], err),
          Transform(previous["points"], points),
          Transform(previous["graph"],  approx_graph),
          run_time=0.5
        )
      self.wait(0.1)

      self.next_slide()
      self.play(Uncreate(line), run_time=0.2)
    self.wait(0.1)

    self.clear_all()

  def play_mitigation(self):
    text = Tex("So how can we mitigate this?").scale(1.2)
    blist = BulletedList(
      " Choose different interpolation points",
      " Use piecewise polynomials",
    )

    VGroup(text, blist).arrange(DOWN, buff=MED_LARGE_BUFF).center()

    self.play(Write(text))
    self.wait(0.1)

    self.next_slide()
    self.play(Write(blist))
    self.wait(0.1)

    self.clear_all()
  
  def play_ending(self):

    text = Tex("That's all folks!").set_color_by_gradient(BLUE, GREEN).scale(1.5).center()
    cat = ImageMobject("assets/cat.jpeg").center()
    bg = BackgroundRectangle(text, fill_opacity=0.5, buff=MED_LARGE_BUFF)
    bg.set_z_index(text.z_index - 1)
    cat.set_z_index(bg.z_index - 1)

    self.play(GrowFromCenter(cat))
    self.wait(0.1)
    self.next_slide()

    self.play(Write(text), Create(bg))
    
    self.clear_all()
