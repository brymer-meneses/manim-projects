from manim import *


class Presentation(VectorScene, MovingCameraScene):
    def _introduction(self):
        group_name = (
            Text("Group 2").move_to(UP).set_color_by_gradient(BLUE, GREEN).scale(1.5)
        ).scale(1.5)
        names = VGroup(
            Text("Elijah Dela Cruz"),
            Text("Lance Rimando"),
            Text("Brymer Meneses"),
            Text("Wano Tayag"),
            Text("LJ Quierijero"),
        )
        names.arrange(DOWN, buff=MED_SMALL_BUFF)  # type:ignore
        names.scale(0.4).next_to(group_name, DOWN)

        self.play(Write(group_name), run_time=2)
        self.wait(2)
        self.play(Write(names), run_time=5)
        self.play(Unwrite(group_name))
        self.play(Unwrite(names))

    def _problem_statement(self):
        title = Title("Problem")
        given_two_vectors = Tex(
            r"Given two vectors $\mathbf{A}$ and $\mathbf{B}$",
        ).shift(UP)

        vec_a = MathTex(r"\mathbf{A}=\langle 8,6,0 \rangle").next_to(  # type:ignore
            given_two_vectors, DOWN, buff=MED_LARGE_BUFF
        )
        vec_a_1 = MathTex(
            r"\mathbf{A}",
            "=",
            r"8\mathbf{i}",
            "+",
            r"6\mathbf{j}",
            "+",
            r"0\mathbf{k}",  # type:ignore
        )


        vec_b = MathTex(r"\mathbf{B}", "=", r"3\mathbf{i}", "+", r"4\mathbf{j}", "+", r"0\mathbf{k}")  # type: ignore
        vec_b.next_to(vec_a, DOWN)
        # given_a = Tex(r"(a) \quad 3\mathbf{A}+\mathbf{B}").next_to(given, DOWN)
        # given_b = Tex(r"(b) \quad ||\mathbf{B}||\mathbf{A}+\mathbf{A}").next_to(
        #     given_a, DOWN
        # )
        # given_c = Tex(r"(c) \quad (||\mathbf{B}-\mathbf{A}||)\mathbf{A}").next_to(
        #     given_b, DOWN
        # )
        solve_for = Tex(
            r"Solve for: (a) $3\mathbf{A}+\mathbf{B}$, (b) $||\mathbf{B}||\mathbf{A}+\mathbf{A}$, (c) $(||B||-||A||)A$"
        ).next_to(vec_b, DOWN)

        self.play(Write(title), run_time=3)
        self.play(Write(given_two_vectors))
        self.play(Write(vec_a))
        self.wait(2)
        self.play(Transform(vec_a, vec_a_1))
        self.wait(2)
        self.play(Write(vec_b))
        self.wait(2)
        self.play(
            FadeOut(vec_a[-1]),
            FadeOut(vec_a[-2]),
            FadeOut(vec_b[-1]),
            FadeOut(vec_b[-2]),
        )
        self.wait(2)
        self.play(Write(solve_for))
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(given_two_vectors),
            FadeOut(vec_a),
            FadeOut(vec_b),
            FadeOut(solve_for),
        )

    def _first_problem(self):
        # problem = Tex("Find $3\mathbf{A}+\mathbf{B}$").scale(2.5).to_corner(UP + LEFT)
        self.camera.frame.save_state()
        self.camera.frame.set(width=50)
        grid = NumberPlane(
            x_range=[-50, 50, 3],
            y_range=[-50, 50, 3],
            x_length=150,
            y_length=150,
            # x_length=12, y_length=12
        )
        grid.add_coordinates()
        # basis_vectors = self.get_basis_vectors()
        vec_a = Line(
            start=grid.coords_to_point(0, 0),
            end=grid.coords_to_point(8, 6),
            stroke_color=GREEN,
        ).add_tip()

        vec_a_label = (
            MathTex(r"\mathbf{A}=\begin{bmatrix}8 \\ 6\end{bmatrix}")
            .next_to(vec_a, RIGHT, buff=0.1)
            .set_color(GREEN)
            .scale(1.8)
        )

        vec_b = Line(
            start=grid.coords_to_point(0, 0),
            end=grid.coords_to_point(3, 4),
            stroke_color=YELLOW,
        ).add_tip()

        vec_b_label = (
            MathTex(r"\mathbf{B}=\begin{bmatrix}3 \\ 4\end{bmatrix}")
            .next_to(
                vec_b,
                LEFT,
                buff=0.1,
            )
            .set_color(YELLOW)
            .scale(1.8)
        )

        vec_3a = Line(
            start=grid.coords_to_point(0, 0),
            end=grid.coords_to_point(3 * 8, 3 * 6),
            stroke_color=GREEN,
        ).add_tip()

        vec_3a_label = (
            MathTex(
                r"3\mathbf{A}=\begin{bmatrix}3\cdot 8 \\ 3\cdot 6\end{bmatrix}"  # type:ignore
            )
            .next_to(grid.coords_to_point(3 * 8 + 2, 3 * 6 + 2))
            .scale(1.8 * 2.5)
            .set_color(GREEN)
        )
        vec_3a_plus_b_1 = Line(
            start=grid.coords_to_point(3 * 8, 3 * 6),
            end=grid.coords_to_point(3 * 8 + 3, 3 * 6 + 4),
            stroke_color=YELLOW,
        ).add_tip()

        vec_3a_plus_b_2 = Line(
            start=grid.coords_to_point(0, 0),
            end=grid.coords_to_point(3 * 8 + 3, 3 * 6 + 4),
            stroke_color=RED,
        ).add_tip()

        vec_3a_plus_b_2_label = (
            MathTex(
                r"3\mathbf{A} + \mathbf{B}=\begin{bmatrix}3\cdot 8 + 3 \\ 3\cdot 6 + 4\end{bmatrix}"  # type:ignore
            )
            .next_to(vec_3a_plus_b_2, LEFT, buff=MED_SMALL_BUFF)
            .set_color(RED)
            .scale(1.8 * 2.5)
        )
        vec_3a_plus_b_2_label_final = (
            MathTex(
                r"3\mathbf{A} + \mathbf{B}=\begin{bmatrix}27 \\ 22\end{bmatrix}"  # type:ignore
            )
            .next_to(vec_3a_plus_b_2, LEFT, buff=MED_SMALL_BUFF)
            .set_color(RED)
            .scale(1.8 * 2.5)
        )
        # self.play(Write(problem))

        self.play(Create(grid, run_time=3, lag_ratio=0.1))
        # self.play(Create(basis_vectors))
        self.play(
            GrowFromPoint(vec_a, point=vec_a.get_start()),
            Write(vec_a_label),
            run_time=3,
        )
        self.play(
            GrowFromPoint(vec_b, point=vec_b.get_start()),
            Write(vec_b_label),
            run_time=3,
        )
        self.play(
            self.camera.frame.animate.move_to(grid.coords_to_point(12, 8)),
        )
        self.play(
            Transform(vec_a, vec_3a),
            Transform(vec_a_label, vec_3a_label),
            vec_b_label.animate.scale(2.5),
            self.camera.frame.animate.set(width=100),
            run_time=3,
        )
        self.play(
            Transform(vec_b, vec_3a_plus_b_1),
            vec_b_label.animate.next_to(vec_3a_plus_b_1, UP, buff=1.1),
            run_time=3,
        )
        self.play(
            GrowFromPoint(vec_3a_plus_b_2, point=vec_3a_plus_b_2.get_start()),
            LaggedStart(Write(vec_3a_plus_b_2_label)),
            run_time=3,
        )
        self.play(
            Transform(vec_3a_plus_b_2_label, vec_3a_plus_b_2_label_final), run_time=2
        )

        self.wait(2)
        self.play(
            Uncreate(grid),
            FadeOut(vec_b_label),
            FadeOut(vec_a_label),
            FadeOut(vec_3a_plus_b_2_label_final),
            FadeOut(vec_3a_plus_b_2_label),
            FadeOut(vec_3a_plus_b_2),
            FadeOut(vec_3a_plus_b_1),
            FadeOut(vec_3a),
            FadeOut(vec_a),
            FadeOut(vec_b),
        )
        self.play(Restore(self.camera.frame))
        final_answer = (
            MathTex(
                r"3",
                r"\mathbf{A}",
                "+",
                r"\mathbf{B}",
                "=",
                r"\begin{bmatrix}27 \\ 22\end{bmatrix}",
                should_center=True,
            )  # type:ignore
            .scale(2.5)
            .set_color_by_gradient(BLUE, GREEN)
        )
        self.play(Write(final_answer))
        self.wait(2)
        self.play(Unwrite(final_answer))
        return

    def _second_problem(self):
        self.camera.frame.set(height=10)
        lines = VGroup(
            MathTex(r"||B||", r"\mathbf{A}", "+", r"\mathbf{A}"),  # type: ignore
            MathTex("=", r"\sqrt{3^2 + 4^2}", r"\begin{bmatrix}8 \\ 6 \end{bmatrix}", "+", r"\begin{bmatrix}8 \\ 6 \end{bmatrix}"),  # type: ignore
            MathTex("=", r"5", r"\begin{bmatrix}8 \\ 6 \end{bmatrix}", "+", r"\begin{bmatrix}8 \\ 6 \end{bmatrix}"),  # type: ignore
            MathTex("=", r"\begin{bmatrix}40 \\ 30 \end{bmatrix}", "+", r"\begin{bmatrix}8 \\ 6 \end{bmatrix}"),  # type: ignore
            MathTex("=", r"\begin{bmatrix}48 \\ 36 \end{bmatrix}"),  # type:ignore
        )
        lines.arrange(DOWN, buff=SMALL_BUFF)
        lines[0].set_color_by_tex_to_color_map({"A": TEAL, "B": BLUE})
        lines[1].set_color_by_tex_to_color_map(
            {
                r"\begin{bmatrix}8 \\ 6 \end{bmatrix}": TEAL,
                r"\sqrt{3^2 + 4^2}": BLUE,
            }
        )
        lines[2].set_color_by_tex_to_color_map(
            {r"\begin{bmatrix}8 \\ 6 \end{bmatrix}": TEAL, r"5": BLUE}
        )
        lines[3].set_color_by_tex_to_color_map(
            {
                r"\begin{bmatrix}8 \\ 6 \end{bmatrix}": TEAL,
                r"\begin{bmatrix}40 \\ 30 \end{bmatrix}": GREEN,
            }
        )
        lines[4].set_color_by_tex_to_color_map(
            {
                r"\begin{bmatrix}48 \\ 36 \end{bmatrix}": RED,
            }
        )

        self.play(Write(lines[0]))
        self.wait(2)

        self.play(
            TransformMatchingTex(lines[0].copy(), lines[1], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(lines[2].copy(), lines[3], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(lines[3].copy(), lines[4], path_arc=90 * DEGREES)
        )
        self.wait(3)

        for line in lines:
            self.play(Unwrite(line), run_time=0.2)

        final_answer = (
            MathTex(
                r"||B||",
                r"\mathbf{A}",
                "+",
                r"\mathbf{A}",
                "=",
                r"\begin{bmatrix}48 \\ 36 \end{bmatrix}",
                should_center=True,
            )  # type:ignore
            .scale(2.5)
            .set_color_by_gradient(BLUE, GREEN)
        )
        self.play(Write(final_answer))
        self.wait(2)
        self.play(Unwrite(final_answer))

        return

    def _third_problem(self):
        lines = VGroup(
            MathTex(r"(||\mathbf{B}|| - ||\mathbf{A}||)\mathbf{A}", substrings_to_isolate=[r"\mathbf{A}", r"\mathbf{B}"]),  # type: ignore
            MathTex(r"=", r"(", r"\sqrt{3^2 + 4^2}", "-", r"\sqrt{8^2 + 6^2}", ")", r"\begin{bmatrix} 8 \\ 6 \end{bmatrix}"),  # type: ignore
            MathTex(r"=(5 - 10)", r"\begin{bmatrix} 8 \\ 6 \end{bmatrix}", substrings_to_isolate=["5", "10"]),  # type: ignore
            MathTex(r"=(-5)", r"\begin{bmatrix} 8 \\ 6 \end{bmatrix}"),  # type: ignore
            MathTex(r"=", r"\begin{bmatrix} -40 \\ -30 \end{bmatrix}"),  # type: ignore
        )
        lines.arrange(DOWN, buff=SMALL_BUFF)
        lines[0].set_color_by_tex_to_color_map({"A": TEAL, "B": BLUE})
        lines[1].set_color_by_tex_to_color_map(
            {
                r"\sqrt{8^2 + 6^2}": TEAL,
                r"\sqrt{3^2 + 4^2}": BLUE,
                r"\begin{bmatrix} 8 \\ 6 \end{bmatrix}": TEAL,
            }
        )
        lines[2].set_color_by_tex_to_color_map(
            {
                r"10": TEAL,
                r"5": BLUE,
                r"\begin{bmatrix} 8 \\ 6 \end{bmatrix}": TEAL,
            }
        )
        lines[3].set_color_by_tex_to_color_map(
            {
                r"10": TEAL,
                r"5": BLUE,
                r"\begin{bmatrix} 8 \\ 6 \end{bmatrix}": TEAL,
            }
        )
        lines[4][1].set_color(RED)

        self.play(Write(lines[0]))
        self.wait(2)
        self.play(
            TransformMatchingTex(lines[0].copy(), lines[1], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(lines[2].copy(), lines[3], path_arc=90 * DEGREES)
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(lines[3].copy(), lines[4], path_arc=90 * DEGREES)
        )

        self.wait(5)
        self.play(Unwrite(lines))

        final_answer = (
            MathTex(
                r"(||\mathbf{B}|| - ||\mathbf{A}||)\mathbf{A}=\begin{bmatrix} -40 \\ -30 \end{bmatrix}",  # type: ignore
            )
            .scale(2.5)
            .set_color_by_gradient(BLUE, GREEN)  # type: ignore
        )
        self.play(Write(final_answer))
        self.wait(2)
        self.play(Unwrite(final_answer))

        return

    def construct(self):
        self._introduction()
        self._problem_statement()
        self._first_problem()
        self._second_problem()
        self._third_problem()


if __name__ == "__main__":
    import os

    os.system("manim -pqm main.py Presentation")
