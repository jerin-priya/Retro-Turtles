import turtle
import random

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Sidescrolling Shooter")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()


class Player():
    def __init__(self, color, x, y, shape):
        self.color = color
        self.x = x
        self.y = y
        self.shape = shape

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.shapesize(1, 1, 0)
        pen.stamp()


player = Player("pink", 0,0, "triangle")
e1 = Player("red", 100,-100, "triangle")
e2 = Player("blue", -100, 100, "triangle")
e3 = Player("yellow", -200,70, "triangle")


while True:
    wn.update()
    pen.clear()
    player.render(pen)
    e1.render(pen)
    e2.render(pen)
    e3.render(pen)

