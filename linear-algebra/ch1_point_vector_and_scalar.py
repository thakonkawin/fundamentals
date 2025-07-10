from manim import *
from enum import Enum 

"""
Chapter 1: Point, Vector, and Scalar

A point is a location in space, and we describe its position using a coordinate system.
A coordinate system is defined by:
An origin — the starting point (0,0)
Axes — lines that show direction (like X, Y, Z). The number of axes depends on the number of dimensions (e.g., 2D has 2 axes, 3D has 3).
Usually, these axes are perpendicular to each other (at 90-degree angles).
"""

class Content(Enum):
    ct1 = 'A point is a location in space, \nwe describe its position using a coordinate system'
    ct2 = 'A point is a boder and size use for reference a position in a coordinate system'


class Point(Scene):
    def construct(self):
        text1 = Text(Content.ct1.value, t2c={"point": YELLOW}).scale(0.7).to_edge(UP)      
        dot = Dot(ORIGIN, stroke_width=12, color=YELLOW)
        bg_rect = BackgroundRectangle(text1, color=WHITE, fill_opacity=0.15)

        # Scene1 
        self.add(bg_rect, text1)
        self.play(Write(dot), run_time=3)
        self.wait()
        self.play(FadeOut(text1), FadeOut(dot), FadeOut(bg_rect))
        
        # Scene2
        plane = NumberPlane().add_coordinates() 
        origin_dot = Dot(ORIGIN)
        point = Dot(np.array([4, 3, 0]), stroke_width=12, color=YELLOW)
        origin_text = Text('(0, 0)').next_to(origin_dot, DOWN)
        tip_text = Text('(4, 3)').next_to(point.get_end(), RIGHT)
        
        x_label = Text("x").next_to(plane.c2p(6, -0.5), RIGHT)
        y_label = Text("y").next_to(plane.c2p(-0.5, 3), UP)
        
        l1 = DashedLine(np.array([4, 0, 0]), point.get_center(), dashed_ratio=0.8, dash_length=0.3)
        l2 = DashedLine(np.array([0, 3, 0]), point.get_center(), dashed_ratio=0.8, dash_length=0.3)
        
        l2.set_color(YELLOW)
        l1.set_color(YELLOW) 
        
        self.add(plane, origin_dot, origin_text, x_label, y_label)
        self.play(Write(point), run_time=4)
        self.wait()
        self.add(tip_text)
        self.play(Write(l1), Write(l2), run_time=5)
        self.wait()
        self.play(
            *[FadeOut(mobj) for mobj in [
                plane, origin_dot, origin_text,
                x_label, y_label, point, tip_text, l1, l2
            ]]
        )
        
class Vector(Scene):
    def construct(self):
        text2 = Text(Content.cts.value, t2c={"point": RED}).scale(0.7).to_edge(UP)
        self.add(text2)