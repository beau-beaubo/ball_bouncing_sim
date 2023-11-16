"""Crate Ball Object In OOP"""
import turtle
import random


class Ball:
    """Create a Ball run with turtle"""

    def __init__(self, xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.ball_radius = ball_radius
        self.ball_color = ball_color
        self.num_balls = num_balls
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy

    def draw_circle(self, i):
        """draw a circle of radius equals to size at x, y coordinates and paint it with color"""
        turtle.penup()
        turtle.color(self.ball_color[i])
        turtle.fillcolor(self.ball_color[i])
        turtle.goto(self.xpos[i], self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

    def move_circle(self, i):
        """update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components"""
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]

    def initilizing(self):
        """create random number of balls, num_balls, located at random positions within the canvas;
         each ball has a random velocity value in the x and y direction and is painted with a random color"""
        for i in range(self.num_balls):
            self.xpos.append(random.randint(-1 * self.canvas_width + self.ball_radius,
                                            self.canvas_width - self.ball_radius))
            self.ypos.append(random.randint(-1 * self.canvas_height + self.ball_radius,
                                            self.canvas_height - self.ball_radius))
            self.vx.append(random.randint(1, 0.01 * self.canvas_width))
            self.vy.append(random.randint(1, 0.01 * self.canvas_height))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
