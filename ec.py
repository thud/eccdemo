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
        eq = TextMobject("$y^2 = x^3 + ax + b$").scale(1.5)

        self.wait(1)
        self.play(Write(eq))
        self.wait(.3)
        self.play(FadeOutAndShiftDown(eq))


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

class Scene2(GraphScene):
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
        self.setup_axes(animate=True)

        parex = ParametricFunction(function=self.ec1, t_min=-5, t_max=5)
        parex2 = ParametricFunction(function=self.ec2, t_min=-5, t_max=5)
        parex3 = ParametricFunction(function=self.ec3, t_min=-5, t_max=5)
        parex4 = ParametricFunction(function=self.ec4, t_min=-5, t_max=5)

        ais = TextMobject("$a = -1$").scale(.75).move_to(3*UL+2*L)
        bis = TextMobject("$b = 5$").scale(.75).next_to(ais, DOWN)
        fnis = TextMobject("$y^2 = x^3 - x + 5$").scale(.75).next_to(bis, DOWN)
        ais2 = TextMobject("$a = 0$").scale(.75).move_to(3*UL+2*L)
        bis2 = TextMobject("$b = 0$").scale(.75).next_to(ais, DOWN)
        fnis2 = TextMobject("$y^2 = x^3$").scale(.75).next_to(bis, DOWN)
        ais3 = TextMobject("$a = -3$").scale(.75).move_to(3*UL+2*L)
        bis3 = TextMobject("$b = 2$").scale(.75).next_to(ais, DOWN)
        fnis3 = TextMobject("$y^2 = x^3 -3x + 2$").scale(.75).next_to(bis, DOWN)
        ais4 = TextMobject("$a = -2$").scale(.75).move_to(3*UL+2*L)
        bis4 = TextMobject("$b = 2$").scale(.75).next_to(ais, DOWN)
        fnis4 = TextMobject("$y^2 = x^3 - 2x + 2$").scale(.75).next_to(bis, DOWN)
        empty = TextMobject("x")

        self.play(
            ShowCreation(parex),
            Write(ais),
            Write(bis),
            Write(fnis),
        )

        self.wait(1)
        self.play(
            Transform(
                parex,
                parex2
            ),
            *[Transform(*x) for x in [[ais,ais2],[bis,bis2],[fnis,fnis2]]]
        )
        self.wait(1)
        self.play(
            CircleIndicate(empty)
        )
        self.wait(1)
        self.play(
            Transform(
                parex,
                parex3
            ),
            *[Transform(*x) for x in [[ais,ais3],[bis,bis3],[fnis,fnis3]]]
        )
        self.wait(1)
        empty.move_to(self.c2p(1,0))
        self.play(
            CircleIndicate(empty)
        )
        self.wait(4)
        self.play(
            Transform(
                parex,
                parex4
            ),
            *[Transform(*x) for x in [[ais,ais4],[bis,bis4],[fnis,fnis4]]]
        )
        self.wait(1)

        gp = parex4.get_point_from_function

        pp = Dot(gp(0.1),color=YELLOW)
        pq = Dot(gp(2),color=YELLOW)
        pplab = TextMobject("$P$",color=YELLOW).scale(0.75).next_to(gp(0.1), LEFT)
        pqlab = TextMobject("$Q$",color=YELLOW).scale(0.75).next_to(gp(2), 0.707*UR)

        self.play(ShowCreation(pp),ShowCreation(pq),Write(pplab),Write(pqlab))
        self.play(
            MoveAlongPathPiece(
                pp,
                pq,
                parex4,
                0.1,1.5,
                2,2.75,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR
            )
        )
        self.play(
            MoveAlongPathPiece(
                pp,
                pq,
                parex4,
                1.5,0.1,
                2.75,2.3,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR
            )
        )
        self.wait(1)
        jline = Line()
        jline.set_angle(angle_of_vector(gp(2.3)-gp(0.1)))
        jline.move_to(gp(0.1))
        jline.set_length(20)
        jline.set_opacity(0.8)

        self.play(
            ShowCreation(jline)
        )
        self.play(
            MovePointsWithLine(
                jline,
                pp,
                pq,
                parex4,
                0.1,0.2,
                2.3,2.1,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR
            )
        )
        point, point2 = self.point_to_coords(gp(0.2)), self.point_to_coords(gp(2.1))

        self.wait(1)

        pr = Dot(color=BLUE)
        m = (point2[1]-point[1])*(point2[0]-point[0])**-1
        point3 = [m**2-point[0]-point2[0]]
        point3.append(point[1]+m*(point3[0]-point[0]))
        pr.move_to(self.coords_to_point(point3[0], point3[1]))
        prlab = TextMobject("$R$",color=BLUE).scale(0.75).next_to(self.coords_to_point(point3[0], point3[1]), 0.707*DR)

        self.play(
            ShowCreation(pr),
            Write(prlab)
        )

        self.play(
            MovePointsWithLineAndThirdPoint(
                self.coords_to_point,
                self.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                0.2,-0.3,
                2.1,2.4,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        self.wait(1)

        self.play(
            MovePointsWithLineAndThirdPoint(
                self.coords_to_point,
                self.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                -0.3,-0.3,
                2.4,0.301,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )
        self.wait(1)
        self.play(
            MovePointsWithLineAndThirdPoint(
                self.coords_to_point,
                self.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                -0.3,-0.3,
                0.301,2.4,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )
        
        self.wait(1)

        m_t = TextMobject("$m = \\frac{\Delta y}{\Delta x} = \\frac{y_p-y_q}{x_p-x_q}$").scale(.75).move_to(D+5*R)
        lineeq_t = TextMobject(
                """\\begin{align*}
                y-y_P &= m(x-x_P)\\\\
                \implies y &= y_P + m(x-x_P)
                \\end{align*}
                """).scale(.75).next_to(m_t, 1.25*DOWN)

        self.play(Write(m_t), Write(lineeq_t))

        self.wait(3)

        intersectedline_t = TextMobject("\\begin{align*}\pm \sqrt{x^3+ax+b} \\\\ = y_P + m(x-x_P) \\end{align*}").scale(.75).next_to(m_t, 1.25*DOWN)
        self.play(
            Transform(
                lineeq_t,
                intersectedline_t
            )
        )
        self.wait(1)

        rxry_t = TextMobject(
                """\\begin{align*}
                x_R=m^2-x_P-x_Q\\\\
                y_R=y_P+m(x_R-x_P)
                \\end{align*}
                """).scale(.75).next_to(m_t, 1.25*DOWN)

        self.play(
            Transform(
                lineeq_t,
                rxry_t
            )
        )

        self.play(
            MovePointsWithLineAndThirdPoint(
                self.coords_to_point,
                self.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                -0.3,0.1,
                2.4,0.6001,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        self.wait(1)
        self.play(
            MovePointsWithLineAndThirdPoint(
                self.coords_to_point,
                self.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                0.1,0.6,
                0.6001,0.6001,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        self.wait(1)

        mtaneq_t = TextMobject("$m_{\\textrm{tan}} = $").scale(.75).move_to(U+3*R)
        mtanrhs = TextMobject("$\\frac{\mathrm{d}}{\mathrm{d}x} \left( \pm \sqrt{x^3+ax+b} \\right)$").scale(.75).next_to(mtaneq_t, RIGHT)
        mtanrhs2 = TextMobject("$\pm \\frac{3x_P^2+a}{2\sqrt{x_P^3+ax+b}}$").scale(.75).next_to(mtaneq_t, RIGHT)
        mtanrhs3 = TextMobject("$\\frac{3x_P^2+a}{2y_P}$").scale(.75).next_to(mtaneq_t, RIGHT)

        self.play(Write(mtaneq_t),Write(mtanrhs))

        self.wait(.5)
        self.play(
            Transform(
                mtanrhs,
                mtanrhs2
            )
        )
        self.wait(.5)
        self.play(
            Transform(
                mtanrhs,
                mtanrhs3
            )
        )
        self.wait(.25)
        self.play(
            mtaneq_t.shift,1.25*R,
            mtanrhs.shift,1.25*R
        )

        self.wait(1)
        self.play(
            MovePointsWithLineAndThirdPoint(
                self.coords_to_point,
                self.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                0.6,-0.6,
                0.6001,0.6001,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        infarrow = Arrow(
                start=U*4+L*1.5+DL,
                end=UP*4+L*1.5,
                color=YELLOW
            )
        pointatinfinity_t = TextMobject("``The Point at Infinity''", color=YELLOW).scale(.75).next_to(infarrow, DL)

        self.play(
            ShowCreation(infarrow),
            Write(pointatinfinity_t),
            ais.shift,1.5*D,
            bis.shift,1.5*D,
            fnis.shift,1.5*D,

        )

        self.wait(4)
        self.play(*[FadeOutAndShiftDown(x) for x in self.get_mobjects()])
        self.wait(1)

    def c2p(self,x,y):
        return self.coords_to_point(x,y)

    def ec1(self,t):
        a,b = -1,5
        c = 1.90416
        if t <= 0:
            x = -t - c
            return self.c2p(x, -((x**3 +a*x + b)**.5))
        x = t - c
        return self.c2p(x, (x**3 +a*x +b)**.5)

    def ec2(self,t):
        a,b = 0,0
        c = 0
        if t <= 0:
            x = -t - c
            return self.c2p(x, -((x**3 + a*x + b)**.5))
        x = t - c
        return self.c2p(x, (x**3 + a*x + b)**.5)

    def ec3(self,t):
        a,b = -3,2
        c = 2
        if t <= 0:
            x = -t - c
            return self.c2p(x, -((x**3 + a*x + b)**.5))
        x = t - c
        return self.c2p(x, (x**3 + a*x + b)**.5)

    def ec4(self,t):
        a,b = -2,2
        c = 1.769
        if t <= 0:
            x = -t - c
            return self.c2p(x, -((x**3 + a*x + b)**.5))
        x = t - c
        return self.c2p(x, (x**3 + a*x + b)**.5)

