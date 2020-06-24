from manimlib.imports import *
from manimlib.animation.animation import Animation
import math
import manimlib.constants as consts


class Title(Scene):
    def construct(self):
        text = TextMobject("Elliptic Curve Cryptography", color=YELLOW).scale(1.6)
        text2 = TextMobject("Jasper Parish")
        text2.next_to(text,DOWN)

        self.play(Write(text))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        self.wait()


class Chapter1(Scene):
    def construct(self):
        text = TextMobject("Chapter 1:")
        text2 = TextMobject("Cryptography", color=YELLOW).scale(1.6)
        text2.next_to(text,DOWN)

        self.play(Write(text))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        self.wait()


class Chapter2(Scene):
    def construct(self):
        text = TextMobject("Chapter 2:")
        text2 = TextMobject("Modular Arithmetic", color=YELLOW).scale(1.6)
        text2.next_to(text,DOWN)

        self.play(Write(text))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        self.wait()



class Chapter3(Scene):
    def construct(self):
        text = TextMobject("Chapter 3:")
        text2 = TextMobject("Groups", color=YELLOW).scale(1.6)
        text2.next_to(text,DOWN)

        self.play(Write(text))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        self.wait()


class Chapter4(Scene):
    def construct(self):
        text = TextMobject("Chapter 4:")
        text2 = TextMobject("Elliptic Curves", color=YELLOW).scale(1.6)
        text2.next_to(text,DOWN)

        self.play(Write(text))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        self.wait()


class Chapter5(Scene):
    def construct(self):
        text = TextMobject("Chapter 5:")
        text2 = TextMobject("The Finale", color=YELLOW).scale(1.6)
        text2.next_to(text,DOWN)

        self.play(Write(text))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        self.wait()

class Conclusion(Scene):
    def construct(self):
        text = TextMobject("Conclusion").scale(1.6)

        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait()

