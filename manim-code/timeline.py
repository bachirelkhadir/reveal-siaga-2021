#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
np.random.seed(0)


class Timeline(Scene):
    def construct(self):

        title = Text("Convex but not SOS?").to_edge(UP)
        self.add(title)

        arrow = Vector().scale(10).shift(LEFT)
        lab_nvar = Text(r"# variables")
        lab_nvar.next_to(arrow, UR).shift(LEFT)
        self.add(arrow, lab_nvar)

        # hilbert bound


        hilbert_tick = Tex("]").move_to(arrow).shift(5*LEFT)
        hilbert_lab = Tex("3").next_to(hilbert_tick, UP)
        hilbert = Group(hilbert_tick, hilbert_lab)
        self.play(hilbert.animate.shift(RIGHT))
        self.wait()

        # blekherman bound

        blek_tick = Tex("|").move_to(arrow).shift(10*RIGHT)
        blek_lab = Tex("n").next_to(blek_tick, UP)
        blek = Group(blek_tick, blek_lab)
        self.play(blek.animate.shift(8*LEFT))
        self.wait()

        blekh_lab_explicit = Tex(r"\sim 10^{10}").move_to(blek_lab)
        self.play(Transform(blek_lab, blekh_lab_explicit))
        self.wait()


        # james bound

        james_tick = Tex("|").move_to(arrow)
        james_lab = Tex("272").next_to(james_tick, UP)
        james = Group(james_tick, james_lab)
        self.play(FadeIn(james))
        self.wait()


        # bachir
        bachir_tick = Tex("|").move_to(arrow).shift(2*LEFT)
        bachir_lab = Tex("5").next_to(bachir_tick, UP)
        bachir = Group(bachir_tick, bachir_lab)
        self.play(FadeIn(bachir))
        self.wait()
        return

        #today

        tick = Line().rotate(PI/2).scale(.2)
        n3 = tick.copy().shift(3*LEFT)
        n4 = n3.copy().shift(RIGHT)
        nhigh = n3.copy().shift(6*RIGHT)

        n3_lab = Tex("3")
        always(n3_lab.next_to, n3, UP)

        n4_lab = Tex("4")
        always(n4_lab.next_to, n4, UP)

        nhigh_lab = Text("high")
        always(nhigh_lab.next_to, nhigh, UP)

        self.add(n3, n4, nhigh)
        self.add(n3_lab, n4_lab, nhigh_lab)
        self.wait()
