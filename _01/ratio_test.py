from manim import *

def _ratio_test(self):
    ratio_test = Tex("Ratio Test").scale(2).set_color_by_gradient(BLUE, GREEN)
    self.play(Write(ratio_test), run_time=1.5)
    self.wait(1)

    ratio_test_section_header = Title("Ratio Test")
    self.play(Transform(ratio_test, ratio_test_section_header), run_time=1.5)
    self.wait(1)

    # Ratio Test
    u_n = MathTex(r"u_{n}", r" = \frac{2n}{2n!}") #type:ignore
    u_n[0].set_color(YELLOW_A)

    L = MathTex(
        r"{{L}} = \lim_{n \to \infty} \left|\frac{u_{n+1}}{u_{n}}\right|").next_to(ratio_test_section_header, DOWN) # type: ignore
    L.set_color_by_tex_to_color_map({"L": TEAL})

    conditions = VGroup(
        Tex(r"If ", "$L$", "$<1$ ", "then the series converges"),
        Tex(r"If ", "$L$", "$>1$ ", "or if ", r"$L$", r"$\to\infty$", " then the series diverges"),
        Tex(r"If ", "$L$", "$=1$ ", "then no conclusion can be made"),
    ).arrange(DOWN, MED_SMALL_BUFF) #type: ignore

    conditions.scale(0.5).next_to(L,DOWN)

    conditions[0][1].set_color(TEAL)
    conditions[1][1].set_color(TEAL)
    conditions[1][4].set_color(TEAL)
    conditions[2][1].set_color(TEAL)

    self.play(Write(u_n))
    self.wait(1)
    self.play(u_n.animate.move_to(2.5 * DOWN).scale(0.7))

    ratio_test_conditions = VGroup( L, conditions).next_to(u_n, UP, buff=LARGE_BUFF)

    ratio_test_box = SurroundingRectangle(ratio_test_conditions, GRAY_A, buff=MED_LARGE_BUFF)
    self.play(GrowFromCenter(ratio_test_conditions))
    self.play(Create(ratio_test_box))

    self.wait(1)

    self.play(
        Unwrite(ratio_test_conditions),
        Uncreate(ratio_test_box)
    )       
    self.play(Unwrite(u_n))

    # RATIO TEST SOLVING PART

    ratio_test_lines = VGroup(
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{\frac{2(n+1)}{2(n+1)!}}{\frac{2n}{2n!}}\right|"), # type: ignore
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{2(n+1)\cdot 2n!}{2(n+1)!\cdot 2n}\right|"), # type: ignore
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot 2n!}{(n+1)!\cdot 2n}\right|"), # type: ignore
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot n!}{(n+1)!\cdot n}\right|"), # type: ignore
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot n!}{(n+1)\cdot n\cdot n!}\right|"), # type: ignore
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)}{(n+1)\cdot n}\right|"), # type: ignore
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{1}{n}\right|"), # type: ignore
        MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", "0"), # type: ignore
        MathTex(r"L", r"=", "0"), # type: ignore
    )

    ratio_test_lines.scale(0.8)
    
    self.play(Write(ratio_test_lines[0]))
    
    for i in range(1, 9):
        self.play(ReplacementTransform(ratio_test_lines[i-1], ratio_test_lines[i]))
        self.wait(1)


    conditions = VGroup(
        Tex(r"If ", "$L$", "$<1$ ", "then the series converges"),
        Tex(r"If ", "$L$", "$>1$ ", "or if ", r"$L$", r"$\to\infty$", " then the series diverges"),
        Tex(r"If ", "$L$", "$=1$ ", "then no conclusion can be made"),
    ).arrange(DOWN, MED_SMALL_BUFF, center=False) #type: ignore

    conditions.scale(0.5).next_to(ratio_test_lines[8],DOWN)
    conditions[0][1].set_color(TEAL)
    conditions[1][1].set_color(TEAL)
    conditions[1][4].set_color(TEAL)
    conditions[2][1].set_color(TEAL)

    self.play(Write(conditions), run_time=2)
    self.wait(1)
    self.play(Indicate(conditions[0], color=YELLOW))
    self.wait(1)

    self.play(Unwrite(conditions))
    self.play(Unwrite(ratio_test_lines[8]))



