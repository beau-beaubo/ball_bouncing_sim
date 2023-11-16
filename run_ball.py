"""Run"""
import turtle
import ball


class Numball:
    """Class"""
    def __init__(self, num_ball):
        self.num_balls = num_ball

    def setting(self):
        """setting"""
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]
        ball_radius = 0.05 * canvas_width
        turtle.colormode(255)
        xpos = []
        ypos = []
        vx = []
        vy = []
        ball_color = []
        default = ball.Ball(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls)
        default.initilizing()
        while True:
            turtle.clear()
            for i in range(num_balls):
                default.draw_circle(i)
                default.move_circle(i)
            turtle.update()
    turtle.done()

# hold the window; close it by clicking the window close 'x' mark


num_balls = int(input("Number of balls to simulate: "))
Numball(num_balls).setting()
