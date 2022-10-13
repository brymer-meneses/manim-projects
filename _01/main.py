from manim import *

class Presentation(Scene):

    def construct(self):
        group_name = (
            Text("Problem 2A").move_to(UP).set_color_by_gradient(BLUE, GREEN).scale(1.5)
        ).scale(1.5)
        names = VGroup(
            Text("Daniel David Bador"),
            Text("Jude Gatchalian"),
            Text("John Kenneth Herrera"),
            Text("Brymer Meneses"),
        )
        names.arrange(DOWN, buff=MED_SMALL_BUFF)  # type:ignore
        names.scale(0.4).next_to(group_name, DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(group_name), run_time=2)
        self.wait(2)
        self.play(Write(names), run_time=5)
        self.play(Unwrite(names))

        # Introduction
        title = Title("Problem")

        problem =MathTex(r"S", r" = \sum_{n=1}^{\infty} \frac{2n}{2n!}") #type: ignore
        problem[0].set_color(TEAL)

        brace = Brace(problem, DOWN)
        converges = brace.get_text("Converges?").set_color(BLUE_B)
        diverges = brace.get_text("Diverges?").set_color(RED_B)

        details = VGroup(group_name, title, problem, brace, converges, diverges)

        ratio_test = Tex("Ratio Test").scale(2).set_color_by_gradient(BLUE, GREEN)

        self.play(LaggedStart(Transform(group_name, title), Write(problem), lag_ratio=3))
        self.wait(1)
        self.play(LaggedStart(GrowFromCenter(brace), GrowFromCenter(converges), lag_ratio=1))
        self.wait(1)
        self.play(Transform(converges, diverges), run_time=3)
        self.wait(1)
        self.play(Transform(details, ratio_test), run_time=1.5)
        self.wait(1)
        self.play(Unwrite(details))
        self.wait(1)

        # Ratio Test
        u_n = MathTex(r"u_{n}", r" = \frac{2n}{2n!}") #type:ignore
        u_n[0].set_color(YELLOW_A)

        L = MathTex(
            r"{{L}} = \lim_{n \to \infty} \left|\frac{u_{n+1}}{u_{n}}\right|").next_to(title, DOWN) # type: ignore
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
        self.play(u_n.animate.move_to(2 * DOWN).scale(0.7))

        ratio_test = VGroup(
            Text("Ratio Test").scale(0.75).set_color(BLUE_A),
            L, conditions
        ).next_to(u_n, UP, buff=LARGE_BUFF)

        ratio_test_box = SurroundingRectangle(ratio_test, GRAY_A, buff=MED_LARGE_BUFF)
        self.play(GrowFromCenter(ratio_test))
        self.play(Create(ratio_test_box))

        self.wait(1)

        self.play(
            Unwrite(ratio_test),
            Uncreate(ratio_test_box)
        )       
        self.play(Unwrite(u_n))

        # Solving Part 

        ratio_test_lines = VGroup(
            MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{\frac{2(n+1)}{2(n+1)!}}{\frac{2n}{2n!}}\right|"), # type: ignore
            MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{2(n+1)\cdot 2n!}{2(n+1)!\cdot 2n}\right|"), # type: ignore
            MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot 2n!}{(n+1)!\cdot 2n}\right|"), # type: ignore
            MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot n!}{(n+1)!\cdot n}\right|"), # type: ignore
            # MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot n!}{(n+1)\cdot n\cdot n!}\right|"), # type: ignore
            # MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)}{(n+1)\cdot n}\right|"), # type: ignore
            # MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{1}{n}\right|"), # type: ignore
        )
        ratio_test_lines.arrange(DOWN,MED_SMALL_BUFF)

        ratio_test_lines[0].set_color_by_tex_to_color_map({"{u_{n+1}}": RED})


        for line in ratio_test_lines:
            self.play(Write(line))

        # Limit Comparison Test

        limit_test = Tex("Limit Comparison Test").scale(2).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(limit_test))
        self.wait(1)

        title = Title("Limit Comparison Test")
        self.play(Transform(limit_test, title))
        given = Tex(r"Given $u_n$ and $v_n$, we have $L=\displaystyle\lim_{n \to \infty} \frac{u_n}{v_n}$ where").next_to(
            title, DOWN)
        conditions = VGroup(
            Tex(r"If $L=0$ and $\sum v_n$ converges, then $\sum v_n$ converges"),
            Tex(r"If $L=\infty$ and $\sum v_n$ diverges, then $\sum v_n$ diverges"),
            Tex(r"If $0<L<\infty$, then either both series converge or both diverge"),
        ).arrange(DOWN, MED_SMALL_BUFF).scale(.7).next_to(given, DOWN*2)
        limit_test_solution = VGroup(
            given, conditions
        )

        self.play(Write(limit_test_solution))
        self.wait(1)

        box = SurroundingRectangle(conditions, YELLOW, buff=.2)
        self.play(Create(box))
        self.wait(5)

        self.play(Unwrite(limit_test_solution))
        self.play(Unwrite(limit_test))
        self.play(Uncreate(box))
        self.wait(1)


        # Conclusion

        conclusion = Title("Conclusion")
        self.play(Write(conclusion))
        self.wait(1)

        self.play(Unwrite(conclusion))
        self.wait(1)

if __name__ == "__main__":
    import os
    os.system("manim -pql main.py Presentation")
