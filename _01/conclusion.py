from manim import *

def _conclusion(self):

    header = Tex("Conclusion").set_color_by_gradient(YELLOW, RED)
    header.scale(1.5)

    section_header = Title("Conclusion")

    self.play(Write(header))
    self.wait(1)
    self.play(Transform(header, section_header))
    self.wait(1)

    messages = VGroup( 
            Tex("In conclusion, using the", " ratio test ", "and the", " limit test ", "we can conclude that the", " series,"),
            MathTex(r"\sum_{n=1}^{\infty}\frac{2n}{2n!}"), #type: ignore
            Tex("is,", " convergent ", r"$\blacksquare$.")
            )
    messages.scale(0.8)

    messages.arrange(DOWN, buff=MED_LARGE_BUFF)
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
    self.play(Unwrite(header))
    self.wait(1)

    quote = VGroup( 
                Tex(r"``Mathematics", " is the ",  "alphabet ", "with which").scale(1.2), #type:ignore
                Tex(r"God",  " has written the ",  "universe", ".''").scale(1.2), #type: ignore
                Tex("Galileo Galilei").scale(0.8).set_color(BLUE_B) #type: ignore
            )

    quote[0][0].set_color(BLUE)
    quote[0][2].set_color(YELLOW)
    quote[1][0].set_color(TEAL)
    quote[1][2].set_color(GREEN)


    quote.arrange(DOWN, MED_SMALL_BUFF)


    for line in quote:
        self.play(Write(line))
        self.wait(1)

    self.play(Unwrite(quote))

    self.wait(1)
    thanks = Tex("Thanks for Watching!").scale(2).set_color_by_gradient(BLUE, GREEN)
    self.play(Write(thanks))
    self.wait(1)

    self.play(Unwrite(thanks))
    self.wait(1)
