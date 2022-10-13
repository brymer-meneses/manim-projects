from manim import *

def _intro(self):
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
    self.play(Write(names), run_time=5)
    self.wait(2)
    self.play(Unwrite(names))
    self.play(Unwrite(group_name))
    self.wait(1)

    # Introduction
    title = Title("Problem")

    problem =MathTex(r"S", r" = \sum_{n=1}^{\infty} \frac{2n}{2n!}") #type: ignore
    problem[0].set_color(TEAL)

    brace = Brace(problem, DOWN)
    converges = brace.get_text("Converges?").set_color(BLUE_B)
    diverges = brace.get_text("Diverges?").set_color(RED_B)

    details = VGroup(group_name, title, problem, brace, converges, diverges)

    self.play(LaggedStart(Write(title), Write(problem), lag_ratio=3))

    self.wait(1)
    self.play(LaggedStart(GrowFromCenter(brace), GrowFromCenter(converges), lag_ratio=1))
    self.wait(1)
    self.play(Transform(converges, diverges), run_time=3)
    self.wait(1)
    self.play(Unwrite(details))

