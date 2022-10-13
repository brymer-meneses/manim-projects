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
        ratio_test_section_header = Title("Ratio Test")
        self.play(Transform(details, ratio_test_section_header), run_time=1.5)

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
        self.play(u_n.animate.move_to(2.5 * DOWN).scale(0.7))

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

        # RATIO TEST SOLVING PART

        ratio_test_lines = VGroup(
            VGroup( 
                MathTex(r"\lim_{n \to \infty} \left|u_{n+1}\over{u_{n}}\right|", r"=", r"\lim_{n \to \infty}\left|\frac{\frac{2(n+1)}{2(n+1)!}}{\frac{2n}{2n!}}\right|"), # type: ignore
                MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{2(n+1)\cdot 2n!}{2(n+1)!\cdot 2n}\right|"), # type: ignore
                MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot 2n!}{(n+1)!\cdot 2n}\right|"), # type: ignore
                MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot n!}{(n+1)!\cdot n}\right|"), # type: ignore
            ),
            VGroup( 
                MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)\cdot n!}{(n+1)\cdot n\cdot n!}\right|"), # type: ignore
                MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{(n+1)}{(n+1)\cdot n}\right|"), # type: ignore
                MathTex(r"=", r"\lim_{n \to \infty}\left|\frac{1}{n}\right|"), # type: ignore
            )
        )


        ratio_test_lines.scale(0.8)
        ratio_test_lines[0].arrange(DOWN, MED_SMALL_BUFF)
        ratio_test_lines[1].arrange(DOWN, MED_SMALL_BUFF)

        self.play(Write(ratio_test_lines[0][0]))
        self.wait(2)
        self.play(
            TransformMatchingTex(ratio_test_lines[0][0].copy(), ratio_test_lines[0][1], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(ratio_test_lines[0][1].copy(), ratio_test_lines[0][2], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(ratio_test_lines[0][2].copy(), ratio_test_lines[0][3], path_arc=90 * DEGREES)
        )
        self.wait(2)
        # self.play(
        #     TransformMatchingTex(lines[2].copy(), lines[3], path_arc=90 * DEGREES)
        # )
        # self.wait(2)
        # self.play(
        #     TransformMatchingTex(lines[3].copy(), lines[4], path_arc=90 * DEGREES)
        # )

        self.wait(5)
        self.play(Unwrite(ratio_test_lines))

        self.play(Unwrite(details))

        # Limit Comparison Test

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


        # Conclusion

        conclusion = Title("Conclusion")
        self.play(Write(conclusion))
        self.wait(1)

        self.play(Unwrite(conclusion))
        self.wait(1)

if __name__ == "__main__":
    import os
    os.system("manim -pql main.py Presentation")
