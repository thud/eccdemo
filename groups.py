from manimlib.imports import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.animation.indication import *
from manimlib.animation.transform import *
import math
import manimlib.constants as consts

L,U,R,D = LEFT, UP, RIGHT, DOWN

class Scene1(Scene):
    def construct(self):

        integersgroup = TextMobject("$(\mathbb{Z}, +)$").scale(2)

        self.play(
            Write(integersgroup)
        )

        self.play(
            integersgroup.scale,0.5,
        )
        self.play(
            integersgroup.move_to,3*UR+3*R,
        )

        axioms_t = TextMobject("Axioms",color=YELLOW).scale(1.7).move_to(2.5*U)
        axiom1 = TextMobject("Closure").move_to(1.5*U)
        axiom2 = TextMobject("Associativity").move_to(0.5*U)
        axiom3 = TextMobject("Identity Element").move_to(-0.5*U)
        axiom4 = TextMobject("Inverse Elements").move_to(-1.5*U)

        self.play(Write(axioms_t))
        self.wait(.5)
        self.play(Write(axiom1))


        self.wait(1)

        self.play(
            FadeOut(axioms_t),
            axiom1.move_to,3*U,
            axiom1.scale,2
        )

        
        astarbingroup = TextMobject("$a * b \in G$").move_to(.5*U).scale(1.5)
        astarbingroup2 = TextMobject("$a + b \in \mathbb{Z}$").move_to(.5*U).scale(1.5)
        abingroup = TextMobject("where $a,b \in G$").next_to(astarbingroup,1.5*D)
        abingroup2 = TextMobject("where $a,b \in \mathbb{Z}$").next_to(astarbingroup,1.5*D)

        self.play(Write(astarbingroup))
        self.play(Write(abingroup))

        self.wait(3)
        self.play(
            Transform(
                astarbingroup,
                astarbingroup2
            ),
            Transform(
                abingroup,
                abingroup2,
            ),
            Indicate(
                integersgroup
            )
        )

        self.wait(2)

        self.play(
            FadeOut(astarbingroup),
            FadeOut(abingroup),
            FadeIn(axioms_t),
            axiom1.move_to, 1.5*U,
            axiom1.scale,.5
        )

        self.wait(.5)

        self.play(Write(axiom2))

        self.wait(1)

        self.play(
            FadeOut(axioms_t),
            FadeOut(axiom1),
            axiom2.move_to,3*U,
            axiom2.scale,2
        )

        astarbstarc = TextMobject("$(a * b) * c = d$").move_to(.5*U).scale(1.5)
        astarbstarc2 = TextMobject("$a * (b * c) = d$").move_to(.5*U).scale(1.5)
        astarbstarc3 = TextMobject("$a + (b + c) = d$").move_to(.5*U).scale(1.5)
        astarbstarc4 = TextMobject("$(a + b) + c = d$").move_to(.5*U).scale(1.5)
        abcingroup = TextMobject("where $a,b,c \in G$").next_to(astarbingroup,1.5*D)
        abcingroup2 = TextMobject("where $a,b,c \in \mathbb{Z}$").next_to(astarbingroup,1.5*D)

        self.play(Write(astarbstarc))
        self.play(Write(abcingroup))

        self.wait(2)
        self.play(
            Transform(
                astarbstarc,
                astarbstarc2
            )
        )

        self.wait(2)
        self.play(
            Transform(
                astarbstarc,
                astarbstarc3
            ),
            Indicate(
                integersgroup
            ),
            Transform(
                abcingroup,
                abcingroup2
            )
        )
        self.wait(.5)
        self.play(
            Transform(
                astarbstarc,
                astarbstarc4
            )
        )
        self.wait(1)

        self.play(
            FadeOut(astarbstarc),
            FadeOut(abcingroup),
            FadeIn(axioms_t),
            FadeIn(axiom1),
            axiom2.move_to, .5*U,
            axiom2.scale, .5
        )

        self.wait(1)

        self.play(Write(axiom3))

        self.wait(1)

        self.play(
            FadeOut(axioms_t),
            FadeOut(axiom1),
            FadeOut(axiom2),
            axiom3.move_to,3*U,
            axiom3.scale,2
        )

        mateq = TextMobject("$AI = A$").scale(1.5)

        self.play(Write(mateq))
        self.wait(1)
        self.play(FadeOut(mateq))

        astarid = TextMobject("$a * I = a$").scale(1.5)
        astarid2 = TextMobject("$a + I = a$").scale(1.5)
        astarid3 = TextMobject("$a + 0 = a$").scale(1.5)

        self.play(
            Write(astarid)
        )
        self.wait(1)
        self.play(
            Transform(
                astarid,
                astarid2
            ),
        )
        self.wait(.5)
        self.play(
            Transform(
                astarid,
                astarid3
            ),
            Indicate(integersgroup)
        )

        self.wait(1)

        self.play(
            FadeOut(astarid),
            FadeIn(axioms_t),
            FadeIn(axiom1),
            FadeIn(axiom2),
            axiom3.move_to, -.5*U,
            axiom3.scale, .5
        )

        self.wait(1)

        self.play(Write(axiom4))
       
        self.wait(1)

        self.play(
            FadeOut(axioms_t),
            FadeOut(axiom1),
            FadeOut(axiom2),
            FadeOut(axiom3),
            axiom4.move_to,3*U,
            axiom4.scale,2
        )

        existsinv = TextMobject("$a * a^{-1} = I$").scale(1.5)
        existsinv2 = TextMobject("$a + (-a) = 0$").scale(1.5).move_to(.1*D)
        
        self.play(Write(existsinv))
        self.wait(2)
        self.play(
            Transform(
                existsinv,
                existsinv2
            ),
            Indicate(
                integersgroup
            )
        )

        self.wait(1)

        self.play(
            FadeOut(existsinv),
            FadeIn(axioms_t),
            FadeIn(axiom1),
            FadeIn(axiom2),
            FadeIn(axiom3),
            axiom4.move_to, -1.5*U,
            axiom4.scale, .5
        )

        self.play(FadeOut(integersgroup))

        self.wait(2)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])

        comm = TextMobject("Commutativity").move_to(3*U).scale(2)

        self.play(FadeInFrom(comm, direction=UP))

        astarbstarceqd = TextMobject("$a * b * c = d$").scale(1.5)
        astarbstarceqd2 = TextMobject("$a * c * b \\not= d$").scale(1.5)
        astarbstarceqd3 = TextMobject("$c * a * b \\not= d$").scale(1.5)

        self.play(Write(astarbstarceqd))
        self.wait(1)
        self.play(
            Transform(
                astarbstarceqd,
                astarbstarceqd2,
            )
        )

        self.wait(.25)

        self.play(
            Transform(
                astarbstarceqd,
                astarbstarceqd3,
            )
        )
        self.wait(1)
        self.play(FadeOutAndShiftDown(astarbstarceqd))
        
        abelian = TextMobject("Abelian Groups", color=YELLOW).scale(2)

        self.play(Write(abelian))


        self.wait(2)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(2)

class Scene2(Scene):
    def construct(self):

        self.wait(1)

        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])

