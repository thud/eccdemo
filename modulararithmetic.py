from manimlib.imports import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.animation.indication import *
from manimlib.animation.transform import *
import math
import manimlib.constants as consts

L,U,R,D = LEFT, UP, RIGHT, DOWN

def modtxt(a,n,m=-1):
    if m == -1: m = a%n
    return TextMobject("$"+str(a)+" \equiv "+str(m)+" \ (\mathrm{mod}\ "+str(n)+")$")


class Scene2(Scene):
    def construct(self):
        gm = lambda n: "\ (\mathrm{mod}\ "+str(n)+")"

        da = TextMobject("$a$").scale(2)
        dainv = TextMobject("$a^{-1}$").scale(2)
        
        self.play(
            Write(da)
        )

        self.play(
            Transform(
                da,
                dainv
            )
        )

        self.wait(3)

        self.play(
            FadeOutAndShiftDown(da)
        )

        nisprime = TextMobject("$n = p$").scale(2)

        self.play(
            Write(nisprime),
        )
        
        self.wait(1)

        self.play(
            FadeOutAndShiftDown(nisprime)
        )

        adivb = TextMobject("$\\frac{a}{b}$").scale(1.5)
        amulbinv = TextMobject("$a \cdot b^{-1}$").scale(1.5).move_to(LEFT)
        adivbmod = TextMobject("$" + gm("n") + "$").scale(1.5).next_to(adivb, 2*RIGHT)

        self.play(
            Write(adivb),
            Write(adivbmod)
        )

        self.play(
            Transform(
                adivb,
                amulbinv
            )
        )

        self.wait(7)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(2)

class Scene1(Scene):
    def construct(self):
        fivemodthree = modtxt(5,3)
        self.play(Write(fivemodthree))
        self.wait(1)

        a = 6
        for n in range(4,6):
            for i in range(2):
                self.play(Transform(
                    fivemodthree,
                    modtxt(a,n)
                    )
                )
                self.wait(0.4)
                a+=1

        self.play(Transform(
                fivemodthree,
                modtxt("a", "n", m="r(a/n)")
            )
        )

        self.play(fivemodthree.shift,UP)

        naturalnumbers = copy.deepcopy(fivemodthree)

        self.wait(1)

        self.play(
                Transform(
                    naturalnumbers,
                    modtxt("\mathbb{N}", "n", m="\{ 0,1,2,...,n-2,n-1 \}")
            )
        )

        self.wait(2)

        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])

        self.wait(1)

        ttwo = TextMobject("$2$")
        tplus = TextMobject("$+$").next_to(ttwo, LEFT)
        tfive = TextMobject("$5$").next_to(tplus, LEFT)
        teq = TextMobject("$=$").next_to(ttwo, RIGHT)
        tsev = TextMobject("$7$").next_to(teq, RIGHT)
        summ = VGroup(tfive,tplus,ttwo,teq,tsev)
        self.play(Write(summ))

        mequiv = TextMobject("$\equiv$").move_to(DOWN)
        mres = TextMobject("$2$").next_to(mequiv, RIGHT)
        mres2 = copy.deepcopy(mres)
        mres3 = TextMobject("$1$").next_to(mequiv, RIGHT)
        mmod = TextMobject("$\ (\mathrm{mod}\ 3)$").next_to(mres, RIGHT)
        mequation = VGroup(mequiv,mmod)

        self.play(
            Write(mequation),
            tfive.next_to,mequiv,LEFT,
            Write(mres)
        )


        self.play(
            mres.next_to,tplus,LEFT
        )

        self.play(
            FadeOutAndShiftDown(tfive)
        )


        self.play(
            ttwo.next_to,mequiv,LEFT,
            Write(mres2)
        )

        self.play(
            mres2.next_to,teq,LEFT
        )

        self.play(
            FadeOutAndShiftDown(ttwo)
        )


        self.play(
            tsev.next_to,mequiv,LEFT,
            Write(mres3)
        )

        self.play(
            mres3.next_to,teq,RIGHT
        )

        self.play(
            Write(copy.deepcopy(mmod).next_to(mres3,RIGHT)),
            *[FadeOutAndShiftDown(x) for x in [tsev, mequation]]
        )

        self.wait(1)

        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(1)

