from manimlib.imports import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.animation.indication import *
from manimlib.animation.transform import *
from manimlib.utils.space_ops import angle_of_vector
import math
import manimlib.constants as consts
from fractions import Fraction

L,U,R,D = LEFT, UP, RIGHT, DOWN

class MoveAlongPathPiece(Animation):
    def __init__(self, mobject, mobject2, path, t_min, t_max, t_min2, t_max2, **kwargs):
        self.mobject = mobject
        self.mobject2 = mobject2
        self.path = path
        self.t_min = t_min
        self.t_max = t_max
        self.t_min2 = t_min2
        self.t_max2 = t_max2
        self.label = kwargs["label"]
        self.labelp = kwargs["labelp"]
        self.label2 = kwargs["label2"]
        self.labelp2 = kwargs["labelp2"]
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.point = self.path.get_point_from_function(self.t_min+alpha*(self.t_max-self.t_min))
        self.point2 = self.path.get_point_from_function(self.t_min2+alpha*(self.t_max2-self.t_min2))
        self.mobject.move_to(self.point)
        self.label.next_to(self.point,self.labelp)
        self.mobject2.move_to(self.point2)
        self.label2.next_to(self.point2,self.labelp2)

class MovePointsWithLine(MoveAlongPathPiece):
    def __init__(self, line, *args, **kwargs):
        self.line = line
        super().__init__(*args, **kwargs)

    def interpolate_mobject(self, alpha):
        super().interpolate_mobject(alpha)
        self.line.set_angle(angle_of_vector(self.point2-self.point))
        self.line.move_to(self.point)

class MovePointsWithLineAndThirdPoint(MovePointsWithLine):
    def __init__(self, c2p, p2c, mobject3, *args, **kwargs):
        self.mobject3 = mobject3
        self.c2p = c2p
        self.p2c = p2c
        self.label3 = kwargs["label3"]
        self.labelp3 = kwargs["labelp3"]
        super().__init__(*args, **kwargs)

    def interpolate_mobject(self, alpha):
        super().interpolate_mobject(alpha)
        if self.point[0] == self.point2[0]:
            print("not yet implemented Jasper!!")
            raise Exception("fuck!")
        c1,c2 = self.p2c(self.point), self.p2c(self.point2)
        m = (c2[1]-c1[1])/(c2[0]-c1[0])
        self.point3 = [m**2-c1[0]-c2[0]]
        self.point3.append(c1[1]+m*(self.point3[0]-c1[0]))
        self.mobject3.move_to(self.c2p(self.point3[0], self.point3[1]))
        self.label3.next_to(self.c2p(self.point3[0], self.point3[1]),self.labelp3)

class Scene1(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        gsetints = TextMobject("$G = \mathbb{Z} \ (\mathrm{mod}\ p)$").scale(1.5).move_to(.5*U)
        geqset = TextMobject("$= \{ 0, 1, 2, ... , p-2, p-1 \}$").scale(1.5).next_to(gsetints, D)

        self.wait(1)
        self.play(
            Write(gsetints),
        )
        self.play(
            Write(geqset)
        )

        self.wait(3)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(3)

        self.setup_axes(animate=True)

        parex = ParametricFunction(function=self.ec, t_min=-5, t_max=5)
        gp = parex.get_point_from_function

        fnis = TextMobject("$y^2 = x^3 - 2x + 2$").scale(.75).move_to(3*U+4*L)
        empty = TextMobject("x")

        self.play(
            ShowCreation(parex),
            Write(fnis),
        )

        point, point2 = self.point_to_coords(gp(0.1)), self.point_to_coords(gp(2))

        pp = Dot(gp(0.1),color=YELLOW)
        pq = Dot(gp(2),color=YELLOW)
        pr = Dot(color=BLUE)
        pplab = TextMobject("$P$",color=YELLOW).scale(0.75).next_to(gp(0.1), LEFT)
        pqlab = TextMobject("$Q$",color=YELLOW).scale(0.75).next_to(gp(2), 0.707*UR)

        m = (point2[1]-point[1])*(point2[0]-point[0])**-1
        point3 = [m**2-point[0]-point2[0]]
        point3.append(point[1]+m*(point3[0]-point[0]))
        pr.move_to(self.coords_to_point(point3[0], point3[1]))
        prlab = TextMobject("$R$",color=BLUE).scale(0.75).next_to(self.coords_to_point(point3[0], point3[1]), 0.707*DR)

        prneg = Dot(color=RED).move_to(self.coords_to_point(point3[0],-point3[1]))
        prneglab = TextMobject("$-R$",color=RED).scale(.75).next_to(self.coords_to_point(point3[0],-point3[1]), 0.707*UR)
        prnegline = Line(start=pr,end=prneg,color=RED)

        jline = Line()
        jline.set_angle(angle_of_vector(gp(2)-gp(0.1)))
        jline.move_to(gp(0.1))
        jline.set_length(20)
        jline.set_opacity(0.8)

        self.play(ShowCreation(pp),ShowCreation(pq),ShowCreation(pr),ShowCreation(jline),Write(pplab),Write(pqlab), Write(prlab))

        ppqpreqz = TextMobject("$P + Q + R = 0$").scale(1.25).move_to(LEFT*4+D*2)
        ppqpreqz2 = TextMobject("$P + Q = -R$").scale(1.25).move_to(LEFT*4+D*2)

        self.play(Write(ppqpreqz))
        self.wait(1)
        self.play(
            Transform(
                ppqpreqz,
                ppqpreqz2
            ),
            ShowCreation(prnegline)
        )

        self.play(ShowCreation(prneg), Write(prneglab))

        self.wait(3)

        self.wait(3)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(3)
    def c2p(self, x, y):
        return self.coords_to_point(x,y)

    def ec(self,t):
        a,b = -2,2
        c = 1.769
        if t <= 0:
            x = -t - c
            return self.c2p(x, -((x**3 + a*x + b)**.5))
        x = t - c
        return self.c2p(x, (x**3 + a*x + b)**.5)

class Scene2(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 36,
        "x_tick_frequency": 5,
        "x_labeled_nums": [0,5,10,15,20,25,30,35],
        "y_min": 0,
        "y_max": 36,
        "y_tick_frequency": 5,
        "y_labeled_nums": [0,5,10,15,20,25,30,35],
        "y_min": 0,
        "graph_origin": 2.5 * D + 2.5 * L,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        self.setup_axes(animate=True)
        self.wait(1)

        p = 37

        ppp = [6,24]
        pp = Dot(self.coords_to_point(*ppp),color=YELLOW)
        pqp = [13,8]
        pq = Dot(self.coords_to_point(*pqp),color=YELLOW)
        pplab = TextMobject("$P$",color=YELLOW).scale(.75).next_to(self.coords_to_point(*ppp), .707*UL)
        pqlab = TextMobject("$Q$",color=YELLOW).scale(.75).next_to(self.coords_to_point(*pqp), .707*UL)

        points = []
        for x in range(p):
            for y in range(p):
                if (x == ppp[0] and y == ppp[1]) or (x == pqp[0] and y == pqp[1]):
                    continue
                if y**2 % p == (x**3 -2*x +2)%p:
                    points.append(self.coords_to_point(x,y))
                    points.append(self.coords_to_point(x,p-y))
        
        dots = [Dot(x) for x in points]
        self.play(
            *[ShowCreation(x) for x in dots],
            ShowCreation(pp),
            ShowCreation(pq),
            Write(pplab),
            Write(pqlab),
        )
        
        self.wait(1)



        mlfn, disc = self.modline(p,ppp,pqp)
        ml = ParametricFunction(function=mlfn, t_min=0, t_max=36, discontinuities=disc)

        self.play(ShowCreation(ml))
        self.wait(1)

        prp = [27,13]
        pr = Dot(self.coords_to_point(*prp),color=BLUE)
        prlab = TextMobject("$R$",color=BLUE).scale(.75).next_to(self.coords_to_point(*prp), .707*UL)

        prpn = [27,p-13]
        prn = Dot(self.coords_to_point(*prpn),color=RED)
        prnlab = TextMobject("$-R$",color=RED).scale(.75).next_to(self.coords_to_point(*prpn), .707*UL)
        jl = Line(start=pr, end=prn, color=RED)

        ppqpreqz2 = TextMobject("$P + Q = -R$").scale(1.25).move_to(LEFT*4+D*2)


        self.play(
            ShowCreation(pr),
            Write(prlab)
        )

        self.play(
            ShowCreation(jl)
        )

        self.play(
            ShowCreation(prn),
            Write(prnlab)
        )

        m_t = TextMobject("$m = \\frac{\Delta y}{\Delta x} = \\frac{y_P-y_Q}{x_P-x_Q}$").scale(.75).move_to(3*U+5*L)
        m_t2 = TextMobject("\\begin{align*}m &= \Delta y (\Delta x)^{-1} \\\\ &= (y_P-y_Q)(x_P-x_Q)^{-1}\\end{align*}").scale(.7).move_to(3*U+5*L)

        self.play(
            Write(m_t)
        )
        self.wait(.5)
        self.play(
            Transform(
                m_t,
                m_t2
            )
        )
        self.wait(2)

        closure_t = TextMobject("1. Closure",color=YELLOW).move_to(2*U+5*L)
        assoc_t = TextMobject("2. Associativity",color=YELLOW).next_to(closure_t, D)
        ident_t = TextMobject("3. Identity Element",color=YELLOW).scale(.75).next_to(assoc_t, D)
        inverse_t = TextMobject("4. Inverse Elements",color=YELLOW).scale(.75).next_to(ident_t, D)

        self.play(Write(closure_t))
        self.wait(.5)

        ppp2 = [6,13]
        pp2 = Dot(self.coords_to_point(*ppp2),color=YELLOW)
        pqp2 = [11,4]
        pq2 = Dot(self.coords_to_point(*pqp2),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp,pq,pr,prn,ml,jl,prlab,prnlab]],
            *[ShowCreation(x) for x in [pp2,pq2]],
            pplab.next_to,self.coords_to_point(*ppp2),.707*UL,
            pqlab.next_to,self.coords_to_point(*pqp2),.707*UL
        )



        mlfn, disc = self.modline(p,ppp2,pqp2)
        ml = ParametricFunction(function=mlfn, t_min=0, t_max=36, discontinuities=disc)

        prp2 = [4,p-13]
        pr2 = Dot(self.coords_to_point(*prp2),color=BLUE)

        prpn2 = [4,13]
        prn2 = Dot(self.coords_to_point(*prpn2),color=RED)
        jl2 = Line(start=pr2, end=prn2, color=RED)

        prlab.next_to(self.coords_to_point(*prp2),.707*UL)
        prnlab.next_to(self.coords_to_point(*prpn2),.707*UL)
        self.play(
            ShowCreation(ml),
            ShowCreation(pr2),
            Write(prlab),
        )
        self.play(
            ShowCreation(jl2),
            ShowCreation(prn2),
            Write(prnlab)
        )

        self.wait(1)






        ppp3 = [4,13]
        pp3 = Dot(self.coords_to_point(*ppp3),color=YELLOW)
        pqp3 = [4,13]
        pq3 = Dot(self.coords_to_point(*pqp3),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp2,pq2,pr2,prn2,ml,jl2,prlab,prnlab]],
            *[ShowCreation(x) for x in [pp3,pq3]],
            pplab.next_to,self.coords_to_point(*ppp3),.707*UL,
            pqlab.next_to,self.coords_to_point(*pqp3),.707*UR
        )


        mlfn, disc = self.modline(p,ppp3,pqp3)
        ml = ParametricFunction(function=mlfn, t_min=0, t_max=36, discontinuities=disc)

        prp3 = [26,p-5]
        pr3 = Dot(self.coords_to_point(*prp3),color=BLUE)

        prpn3 = [26,5]
        prn3 = Dot(self.coords_to_point(*prpn3),color=RED)
        jl3 = Line(start=pr3, end=prn3, color=RED)

        prlab.next_to(self.coords_to_point(*prp3),.707*UL)
        prnlab.next_to(self.coords_to_point(*prpn3),.707*UL)
        self.play(
            ShowCreation(ml),
            ShowCreation(pr3),
            Write(prlab),
        )
        self.play(
            ShowCreation(jl3),
            ShowCreation(prn3),
            Write(prnlab)
        )

        self.wait(2)



        ppp4 = [6,24]
        pp4 = Dot(self.coords_to_point(*ppp4),color=YELLOW)
        pqp4 = [13,8]
        pq4 = Dot(self.coords_to_point(*pqp4),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp3,pq3,pr3,prn3,ml,jl3,prlab,prnlab]],
            *[ShowCreation(x) for x in [pp4,pq4]],
            pplab.next_to,self.coords_to_point(*ppp4),.707*UL,
            pqlab.next_to,self.coords_to_point(*pqp4),.707*UL
        )



        mlfn, disc = self.modline(p,ppp4,pqp4)
        ml = ParametricFunction(function=mlfn, t_min=0, t_max=36, discontinuities=disc)

        prp4 = [27,13]
        pr4 = Dot(self.coords_to_point(*prp4),color=BLUE)

        prpn4 = [27,p-13]
        prn4 = Dot(self.coords_to_point(*prpn4),color=RED)
        jl4 = Line(start=pr4, end=prn4, color=RED)

        prlab.next_to(self.coords_to_point(*prp4),.707*UL)
        prnlab.next_to(self.coords_to_point(*prpn4),.707*UL)
        self.play(
            ShowCreation(ml),
            ShowCreation(pr4),
            Write(prlab),
        )
        self.play(
            ShowCreation(jl4),
            ShowCreation(prn4),
            Write(prnlab)
        )

        self.wait(1)

        self.play(
            FadeToColor(
                closure_t,
                GREEN
            )
        )

        self.wait(2)
        self.play(
            Write(assoc_t)
        )

        self.play(
            FadeOut(prn4),
            FadeOut(prnlab),
            FadeOut(jl4)
        )

        self.play(
            pr4.move_to,self.coords_to_point(*ppp4),
            prlab.next_to,self.coords_to_point(*ppp4),.707*UL,
            pp4.move_to,self.coords_to_point(*pqp4),
            pplab.next_to,self.coords_to_point(*pqp4),.707*UL,
            pq4.move_to,self.coords_to_point(*prp4),
            pqlab.next_to,self.coords_to_point(*prp4),.707*UL,
        )


        self.wait(2)
        self.play(
            FadeToColor(
                assoc_t,
                GREEN
            )
        )
        self.wait(1)

        self.play(
            Write(ident_t)
        )

        self.wait(1)

        ppp5 = [6,24]
        pp5 = Dot(self.coords_to_point(*ppp5),color=YELLOW)
        pqp5 = [6,p-24]
        pq5 = Dot(self.coords_to_point(*pqp5),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp4,pq4,pr4,prn4,ml,jl4,prlab,prnlab]],
            *[ShowCreation(x) for x in [pp5,pq5]],
            pplab.next_to,self.coords_to_point(*ppp5),.707*UL,
            pqlab.next_to,self.coords_to_point(*pqp5),.707*UL
        )


        ml = Line(start=self.coords_to_point(ppp5[0],0), end=self.coords_to_point(ppp5[0],p-1))

        self.play(
            ShowCreation(ml),
        )

        infarrow = Arrow(
                start=U*4+.75*L+DR,
                end=UP*4+.75*L,
                color=RED
            )
        pointatinfinity_t = TextMobject("``The Point at Infinity''", color=RED).scale(.75).next_to(infarrow, DR)

        self.play(
            ShowCreation(infarrow),
            Write(pointatinfinity_t)
        )

        self.wait(2)
        self.play(
            FadeToColor(
                ident_t,
                GREEN
            )
        )
        self.wait(2)

        self.play(
            Write(inverse_t)
        )
        self.play(
            Transform(
                pqlab,
                TextMobject("$-P$",color=GREEN).scale(.75).next_to(self.coords_to_point(*pqp5), 0.707*UL)
            ),
            FadeToColor(
                pq5,
                GREEN
            )
        )

        self.wait(2)
        self.play(
            FadeToColor(
                inverse_t,
                GREEN
            )
        )

        self.wait(5)
        self.play(
            *[FadeOutAndShiftDown(x) for x in [closure_t, assoc_t, ident_t, inverse_t]]
        )

        self.wait(.5)

        mmulp = TextMobject("$kP=\\underbrace{P+P+P+\\ldots+P}_{k\\text{-times}}$").scale(.5).next_to(U+7*L)

        self.play(
            Write(mmulp)
        )

        self.wait(1)



        ppp6 = [4,13]
        pp6 = Dot(self.coords_to_point(*ppp6),color=YELLOW)
        pqp6 = [4,13]
        pq6 = Dot(self.coords_to_point(*pqp6),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp5,pq5,ml,pqlab,infarrow,pointatinfinity_t]],
            *[ShowCreation(x) for x in [pp6,pq6]],
            pplab.next_to,self.coords_to_point(*ppp6),.707*UL
        )


        mlfn, disc = self.modline(p,ppp6,pqp6)
        ml = ParametricFunction(function=mlfn, t_min=0, t_max=36, discontinuities=disc)

        prp6 = [26,p-5]
        pr6 = Dot(self.coords_to_point(*prp6),color=BLUE)

        prpn6 = [26,5]
        prn6 = Dot(self.coords_to_point(*prpn6),color=RED)
        jl6 = Line(start=pr6, end=prn6, color=RED)

        prlab.next_to(self.coords_to_point(*prp6),.707*UL)
        prnlab = TextMobject("$2P$",color=RED).scale(.75).next_to(self.coords_to_point(*prpn6),.707*UL)
        self.play(
            ShowCreation(ml),
            ShowCreation(pr6),
        )
        self.play(
            ShowCreation(jl6),
            ShowCreation(prn6),
            Write(prnlab)
        )

        self.wait(2)


        ppp7 = [4,13]
        pp7 = Dot(self.coords_to_point(*ppp7),color=YELLOW)
        pqp7 = [26,5]
        pq7 = Dot(self.coords_to_point(*pqp7),color=YELLOW)

        pqlab = TextMobject("$2P$",color=RED).scale(.75).next_to(self.coords_to_point(*prpn6),.707*UL)

        self.play(
            *[FadeOut(x) for x in [pp6,pq6,pr6,jl6,ml,pqlab]],
            *[ShowCreation(x) for x in [pp7,pq7]],
            FadeIn(pqlab)
        )


        mlfn, disc = self.modline(p,ppp7,pqp7)
        ml = ParametricFunction(function=mlfn, t_min=0, t_max=36, discontinuities=disc)

        prp7 = [16,p-25]
        pr7 = Dot(self.coords_to_point(*prp7),color=BLUE)

        prpn7 = [16,25]
        prn7 = Dot(self.coords_to_point(*prpn7),color=RED)
        jl7 = Line(start=pr7, end=prn7, color=RED)

        prlab.next_to(self.coords_to_point(*prp7),.707*UL)
        prnlab7 = TextMobject("$3P$",color=RED).scale(.75).next_to(self.coords_to_point(*prpn7),.707*UL)
        self.play(
            ShowCreation(ml),
            ShowCreation(pr7),
        )
        self.play(
            ShowCreation(jl7),
            ShowCreation(prn7),
            Write(prnlab7)
        )

        self.wait(2)




        ppp8 = [4,13]
        pp8 = Dot(self.coords_to_point(*ppp8),color=YELLOW)
        pqp8 = [16,25]
        pq8 = Dot(self.coords_to_point(*pqp8),color=YELLOW)

        pqlab = TextMobject("$3P$",color=RED).scale(.75).next_to(self.coords_to_point(*prpn6),.707*UL)

        self.play(
            *[FadeOut(x) for x in [pp7,pq7,pr7,jl7,ml,pqlab]],
            *[ShowCreation(x) for x in [pp8,pq8]],
            FadeIn(pqlab)
        )


        mlfn, disc = self.modline(p,ppp8,pqp8)
        ml = ParametricFunction(function=mlfn, t_min=0, t_max=36, discontinuities=disc)

        prp8 = [18,p-10]
        pr8 = Dot(self.coords_to_point(*prp8),color=BLUE)

        prpn8 = [18,10]
        prn8 = Dot(self.coords_to_point(*prpn8),color=RED)
        jl8 = Line(start=pr8, end=prn8, color=RED)

        prlab.next_to(self.coords_to_point(*prp8),.707*UL)
        prnlab8 = TextMobject("$4P$",color=RED).scale(.75).next_to(self.coords_to_point(*prpn8),L)
        self.play(
            ShowCreation(ml),
            ShowCreation(pr8)
        )
        self.play(
            ShowCreation(jl8),
            ShowCreation(prn8),
            Write(prnlab8)
        )

        self.wait(3)

        self.play(
            Transform(
                prnlab8,
                TextMobject("$dP=H$",color=RED).scale(.75).next_to(self.coords_to_point(*prpn8),L)
            ),
            Transform(
                prnlab7,
                TextMobject("$(d-1)P$",color=YELLOW).scale(.75).next_to(self.coords_to_point(*prpn7),.707*UL)
            ),
            *[FadeOut(x) for x in [pqlab,prn6,prnlab]]
        )

        dpeqh = TextMobject("$dP=H$",color=RED).scale(.75).move_to(5*L+D)
        self.play(
            Write(dpeqh)
        )

        self.wait(10)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(2)

    def modline(self, p, ppp, pqp):
        m = 0
        if (ppp[0] == pqp[0]) and (ppp[1] == pqp[1]):
            denom = pow(2*ppp[1], p-2, p)
            m = ((3*ppp[0]**2-2)*denom)%p
        else:
            denom = pow(pqp[0]-ppp[0], p-2, p)
            m = ((pqp[1]-ppp[1])*denom)%p

        disc = []
        x = 0
        i = -10

        while x < p:
            x = ((i*p-ppp[1])/m) + ppp[0]
            disc.append(x)
            i+=1

        def modlinefn(t):
            return self.coords_to_point(t, (ppp[1] + m*(t-ppp[0]))%p)
        return (modlinefn, disc)


class Scene3(Scene):
    def construct(self):
        apos = LEFT*4.25
        bpos = RIGHT*4.5

        alice = TextMobject("Alice",color=YELLOW)
        alice.move_to(apos)
        self.play(Write(alice))
        
        bob = TextMobject("Bob")
        bob.move_to(bpos)
        self.play(Write(bob))

        arrow = ArcBetweenPoints(apos, bpos)
        arrow.add_tip(tip_length=.2)
        arrow.shift(DOWN*0.5)
        self.play(ShowCreation(arrow))

        h_a = TextMobject("$H_a$",color=YELLOW).scale(0.5).next_to(apos,UP*1.5+3*L)
        h_a_inf = TextMobject("(Alice's public key point)",color=YELLOW).scale(.5).next_to(h_a, R)
        d_a = TextMobject("$d_a$",color=YELLOW).scale(0.5).next_to(h_a,UP)
        d_a_inf = TextMobject("(Alice's private key)",color=YELLOW).scale(.5).next_to(d_a, R)
        h_b = TextMobject("$H_b$").scale(0.5).next_to(bpos,UP*1.5+3*L)
        h_b_inf = TextMobject("(Bob's public key point)").scale(.5).next_to(h_b, R)
        d_b = TextMobject("$d_b$").scale(0.5).next_to(h_b, U)
        d_b_inf = TextMobject("(Bob's private key)").scale(.5).next_to(d_b, R)
        self.play(*[Write(x) for x in [h_a,h_a_inf,d_a,d_a_inf,h_b,h_b_inf,d_b,d_b_inf]])

        self.wait(3)

        self.play(
            h_a.next_to,bpos,UP*1.5+3*L,
            h_a_inf.next_to,h_b,R,
            h_b.next_to,apos,UP*1.5+3*L,
            h_b_inf.next_to,h_a,R
        )

        self.wait(2)

        self.play(
            *[FadeOutAndShiftDown(x) for x in [h_a_inf,h_b_inf,d_a_inf,d_b_inf]],
            h_a.scale,2,
            h_b.scale,2,
            d_a.scale,2,
            d_b.scale,2,
        )

        self.play(
            h_a.shift,R,
            h_b.shift,R,
        )
        
        self.wait(.5)

        self.play(
            d_a.next_to,h_b,.5*L,
            d_b.next_to,h_a,.5*L,
        )

        self.wait(.5)

        h_a2 = TextMobject("$(d_a P)$").next_to(h_a,0)
        h_b2 = TextMobject("$(d_b P)$").next_to(h_b,0)
        h_a3 = TextMobject("$d_a P$").next_to(h_a,0)
        h_b3 = TextMobject("$d_b P$").next_to(h_b,0)

        self.play(
            Transform(
                h_a,
                h_a2
            ),
            Transform(
                h_b,
                h_b2
            ),
            d_a.shift,.1*L,
            d_b.shift,.1*L,
        )

        self.play(
            FadeToColor(d_a,WHITE),
            Transform(
                h_a,
                h_a3
            ),
            Transform(
                h_b,
                h_b3
            )
        )

        self.wait(.5)

        mid = UP*2
        eq = TextMobject("$=$").move_to(mid)

        lhs = VGroup(h_b,d_a)
        rhs = VGroup(h_a,d_b)

        self.play(
            Write(eq),
            lhs.next_to,mid,1.2*L,
            rhs.next_to,mid,1.2*R,
        )

        self.wait(2)

        eve = TextMobject("Eve",color=RED)
        self.play(Write(eve))
        self.play(CircleIndicate(eve,color=RED))
        
        ecdlh = TextMobject("Elliptic Curve Discrete Logarithm Problem",color=YELLOW).move_to(UP)
        self.play(Write(ecdlh))

        self.wait(2)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(2)
