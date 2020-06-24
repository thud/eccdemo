from manimlib.imports import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.animation.indication import *
from manimlib.animation.transform import *
from manimlib.utils.space_ops import angle_of_vector
import math
import manimlib.constants as consts
from fractions import Fraction

L,U,R,D = LEFT, UP, RIGHT, DOWN

class Scene1(Scene):
    def construct(self):
        title = TextMobject("Thanks For Watching",color=YELLOW).move_to(3*U)
        self.wait(.5)
        self.play(Write(title))
        self.wait(1)

        spacing = 1.8

        mnm = TextMobject("Manim").scale(.75).move_to(2*U)
        mnmref = TextMobject("github.com/3b1b/manim",color=BLUE).scale(.5).next_to(mnm,.75*D)
        self.play(Write(mnm),Write(mnmref))

        acblog = TextMobject("AC Blog").scale(.75).next_to(mnmref, spacing*D)
        acblogref = TextMobject("andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/",color=BLUE).scale(.5).next_to(acblog,.75*D)
        self.play(Write(acblog),Write(acblogref))

        jbblog = TextMobject("JB Blog").scale(.75).next_to(acblogref, spacing*D)
        jbblogref = TextMobject("johannes-bauer.com/compsci/ecc/",color=BLUE).scale(.5).next_to(jbblog,.75*D)
        self.play(Write(jbblog),Write(jbblogref))

        iccourse = TextMobject("Imperial Course Material").scale(.75).next_to(jbblogref, spacing*D)
        iccourseref = TextMobject("doc.ic.ac.uk/\\textasciitilde{}mrh/330tutor/",color=BLUE).scale(.5).next_to(iccourse,.75*D)
        self.play(Write(iccourse),Write(iccourseref))

        code = TextMobject("Code").scale(.75).next_to(iccourseref, spacing*D)
        coderef = TextMobject("github.com/x-JP/eccdemo",color=BLUE).scale(.5).next_to(code,.75*D)
        self.play(Write(code),Write(coderef))

        self.wait(2)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(2)
