from manim import *

def _conclusion(self):
    conclusion = Tex("Thanks for Watching!").scale(2).set_color_by_gradient(BLUE, GREEN)
    self.play(Write(conclusion))
    self.wait(1)


    messages = VGroup( 
            Tex("In conclusion, using the", " ratio test ", "and the", " limit test ", "we can conclude that the", " series,"),
            MathTex(r"\sum_{n=1}^{\infty}\frac{2n}{2n!}"), #type: ignore
            Tex("is,", " convergent ", r"$\blacksquare$.")
            )
    messages.scale(0.8)

    messages.arrange(DOWN, buff=MED_SMALL_BUFF)
    messages[0][-1].set_color_by_gradient(BLUE, GREEN)
    messages[0][1].set_color(TEAL)
    messages[0][3].set_color(GREEN)
    messages[1].set_color_by_gradient(BLUE, GREEN).scale(1.5)
    messages[2][1].set_color(YELLOW)
    
    box = SurroundingRectangle(messages, buff=MED_SMALL_BUFF, color=WHITE)

    for message in messages:
        self.play(Write(message))
        self.wait(1)

    self.play(Create(box))
    self.wait(1)
    self.play(Unwrite(messages))
    self.wait(1)
    self.play(Uncreate(box))
    self.wait(1)
    self.play(Unwrite(conclusion))
    self.wait(1)
