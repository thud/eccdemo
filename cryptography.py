from manimlib.imports import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.animation.indication import *
from manimlib.animation.transform import *
import math
import manimlib.constants as consts

L,U,R,D = LEFT, UP, RIGHT, DOWN

class Scene1(Scene):
    def construct(self):

        apos = LEFT*4.25
        bpos = RIGHT*4.5


        alice = TextMobject("Alice",color=YELLOW)
        alice.move_to(apos)
        self.play(Write(alice))
        
        bob = TextMobject("Bob")
        bob.move_to(bpos)
        self.play(Write(bob))

        self.wait(5)
        
        arrow = ArcBetweenPoints(apos, bpos)
        arrow.add_tip(tip_length=.2)
        arrow.shift(DOWN*0.5)
        self.play(ShowCreation(arrow))

        apubk_t = TextMobject("Public key (Alice)",color=YELLOW).scale(0.5)
        bpubk_t = TextMobject("Public key (Bob)").scale(0.5)
        aprvk_t = TextMobject("Private key (Alice)",color=YELLOW).scale(0.5)
        bprvk_t = TextMobject("Private key (Bob)").scale(0.5)
        apubk_t.next_to(alice, UP + LEFT*0.25)
        aprvk_t.next_to(apubk_t, UP)
        bpubk_t.next_to(bob, UP + RIGHT*0.25)
        bprvk_t.next_to(bpubk_t, UP)
        self.play(*[Write(x) for x in [apubk_t, aprvk_t, bpubk_t, bprvk_t]])

        self.wait(3)

        self.play(apubk_t.next_to,bob, UP+RIGHT*0.25,
                bpubk_t.next_to,alice, UP+LEFT*0.25
            )

        ### Transmitting "Hello"
        fn1 = TextMobject("$f$")
        fn1box = Square(side_length=.8)
        fn1box.next_to(aprvk_t, DOWN*2.5)
        fn1.move_to(fn1box)

        fn2 = TextMobject("$f$")
        fn2box = Square(side_length=.8)
        fn2box.next_to(bprvk_t, DOWN*2.5)
        fn2.move_to(fn2box)

        self.play(Write(fn1), ShowCreation(fn1box))

        self.play(
            bpubk_t.move_to,fn1box,
            FadeOutAndShiftDown(bpubk_t),
        )
        self.play(
            aprvk_t.move_to,fn1box,
            FadeOutAndShiftDown(aprvk_t),
        )

        self.wait(1)
        
        ss1 = TextMobject("SECRET").scale(0.6).next_to(fn1box, 2*DOWN)
        ss2 = TextMobject("SECRET").scale(0.6).next_to(fn2box, 2*DOWN)

        self.play(
            FadeInFrom(ss1, direction=UP)
        )

        self.play(Write(fn2), ShowCreation(fn2box))


        self.play(
            apubk_t.move_to,fn2box,
            FadeOutAndShiftDown(apubk_t),
        )
        self.play(
            bprvk_t.move_to,fn2box,
            FadeOutAndShiftDown(bprvk_t),
        )

        self.play(
            FadeInFrom(ss2, direction=UP)
        )

        diffhell_t = TextMobject("Diffie-Hellman key exchange",color=YELLOW).move_to(UP*2)
        self.play(Write(diffhell_t))
        self.wait(0.25)
        self.play(FadeOut(diffhell_t))

        self.wait(.2)

        elliptic_curves_t = TextMobject("$f=$Elliptic Curve Algorithm").scale(1.2).move_to(UP*2)
        self.play(Write(elliptic_curves_t))

        self.wait(1)

        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(1)
