from manim import *

def _limit_test(self):
    limit_test = Tex("Limit Comparison Test").scale(2).set_color_by_gradient(BLUE, GREEN)
    self.play(Write(limit_test))
    self.wait(1)

    title = Title("Limit Comparison Test")
    self.play(Transform(limit_test, title))
    given1 = MathTex(r"u_n", r"\text{ and }", r"v_n")
    given2 = MathTex(r"L", r"=\lim_{n \to \infty} ", r"{{u_n}", r"\over", r"{v_n}}")
    conditions = VGroup(
        Tex(r"If ", r"$L$", r"$=0$ and $\sum$",r"$v_n$", r" converges, then $\sum$", r"$u_n$", r" converges"),
        Tex(r"If ", r"$L$", r"$=\infty$ and $\sum$", r"$v_n$", r" diverges, then $\sum$", r"$u_n$", r" diverges"),
        Tex(r"If $0<$", r"$L$", r"$<\infty$, then either both series converge or both diverge"),
    ).arrange(DOWN, MED_SMALL_BUFF).scale(.6)

    given1[0].set_color(BLUE)
    given1[2].set_color(GREEN)
    given2[0].set_color(TEAL)
    given2[2].set_color(BLUE)
    given2[4].set_color(GREEN)
    conditions[0][1].set_color(TEAL)
    conditions[0][3].set_color(GREEN)
    conditions[0][5].set_color(BLUE)
    conditions[1][1].set_color(TEAL)
    conditions[1][3].set_color(GREEN)
    conditions[1][5].set_color(BLUE)
    conditions[2][1].set_color(TEAL)

    self.play(Write(given1))
    self.wait(1)

    self.play(given1.animate.move_to(2 * DOWN).scale(0.7))
    self.play(Write(given2))
    self.wait(1)

    self.play(given2.animate.next_to(title, DOWN))
    self.play(Write(conditions))
    self.wait(1)

    box = SurroundingRectangle(conditions, YELLOW, buff=.2)
    self.play(Create(box))
    self.wait(5)

    self.play(Unwrite(VGroup(box, conditions)))
    self.wait(1)

    given = MathTex(r"u_n", r"=", r"\frac{2n}{2n!}", r"\text{ and }", r"v_n", r"=", r"\frac{n^3}{n!}").shift(2 * DOWN).scale(0.7)
    given[0].set_color(BLUE)
    given[4].set_color(GREEN)
    given[2].set_color(BLUE)
    given[6].set_color(GREEN)
    
    self.play(TransformMatchingTex(given1, given))

    # Limit Comparison Test Solving Part

    limit_test_lines = VGroup(
        MathTex(r"L", r"=\lim_{n \to \infty} ", r"{{\frac{2n}{2n!}", r"\over", r"\frac{n^3}{n!}}"),
        MathTex(r"L", r"=\lim_{n \to \infty} ", r"{{\frac{n}{n!}", r"\over", r"\frac{n^3}{n!}}"),
        MathTex(r"L", r"=\lim_{n \to \infty} ", r"{{n}", r"\over", r"{n^3}}"),
        MathTex(r"L", r"=\lim_{n \to \infty} ", r"{{1}", r"\over", r"{n^2}}"),
        MathTex(r"L", r"=0"),
    )

    limit_test_lines[0][2].set_color(BLUE)
    limit_test_lines[0][4].set_color(GREEN)

    for lines in limit_test_lines:
        lines[0].set_color(TEAL)

    self.play(ReplacementTransform(VGroup(given2, given), limit_test_lines[0]))
    self.wait(1)

    for i in range(1, 5):
        self.play(TransformMatchingTex(limit_test_lines[i - 1], limit_test_lines[i], path_arc=90 * DEGREES))
        self.wait(1)

    conditions = VGroup(
        Tex(r"If ", r"$L$", r"$=0$ and $\sum$",r"$v_n$", r" converges, then $\sum$", r"$u_n$", r" converges"),
        Tex(r"If ", r"$L$", r"$=\infty$ and $\sum$", r"$v_n$", r" diverges, then $\sum$", r"$u_n$", r" diverges"),
        Tex(r"If $0<$", r"$L$", r"$<\infty$, then either both series converge or both diverge"),
    ).arrange(DOWN, MED_SMALL_BUFF).scale(.6)
    conditions.arrange(LEFT, buff=MED_SMALL_BUFF)

    conditions[0][1].set_color(TEAL)
    conditions[0][3].set_color(GREEN)
    conditions[0][5].set_color(BLUE)
    conditions[1][1].set_color(TEAL)
    conditions[1][3].set_color(GREEN)
    conditions[1][5].set_color(BLUE)
    conditions[2][1].set_color(TEAL)
    
    self.play(limit_test_lines[4].animate.shift(2 * UP))
    self.play(Write(conditions))
    self.wait(1)

    self.play(Indicate(conditions[0]))
    self.wait(1)

    self.play(Unwrite(limit_test_lines[4]))
    self.play(Unwrite(conditions))
    self.play(Unwrite(limit_test))
    self.wait(1)
