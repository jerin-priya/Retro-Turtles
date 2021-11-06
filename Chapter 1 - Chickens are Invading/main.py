import turtle
import os
import math
import random

start_m = turtle.Screen()
start_m.setup(800, 600)
start_m.bgcolor("black")
start_m.title("Chickens are Invading!")
start_m.bgpic("Startpic.gif")
start_m.tracer(0)

global starting
starting = True
def Lets_start():
    global starting
    starting = False
start_m.listen()
start_m.onkey(Lets_start, "s")

while starting:
    start_m.update()
start_m.clearscreen()

window = turtle.Screen()
window.setup(800, 600)
window.bgcolor("black")
window.title("Chickens are Invading!")
window.tracer(0)

window.register_shape("invader.gif")
window.register_shape("player.gif")
window.register_shape("red_star.gif")
window.register_shape("white_star.gif")
window.register_shape("yellow_star.gif")

class Star(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        star_images = ["yellow_star.gif", "red_star.gif", "white_star.gif"]
        self.shape(random.choice(star_images))
        self.penup()
        self.speed(0)
        self.goto(random.randint(-480, 400), random.randint(-370, 290))
        self.dy = random.randint(1, 5) / -20

    def move(self):
        self.sety(self.ycor() + self.dy)
        if self.ycor() < - 290:
            self.goto(random.randint(400, 480), random.randint(-290, 290))

stars = []
for black_hole in range(40):
    stars.append(Star())


# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 40

number_of_chickens = 15
chickens = []

for i in range(number_of_chickens):
    chickens.append(turtle.Turtle())
for chicken in chickens:
    chicken.color("red")
    chicken.shape("invader.gif")
    chicken.penup()
    chicken.speed(0)
    chicken.setposition(random.randint(-350, 350), random.randint(100, 250))
chickenspeed = 0.5


# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("Red")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.3, 0.50)
bullet.hideturtle()
bulletspeed = 30
bulletstate = "ready"


def move_left():
    x = player.xcor() - playerspeed
    if x < -380:
        x = - 380
    player.setx(x)

def move_right():
    x = player.xcor() + playerspeed
    if x > 380:
        x = 380
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay laser.wav&")
        bulletstate = "fire"
        bullet.setposition(player.xcor(), player.ycor() + 25)
        bullet.showturtle()


def isCollision(obj1, obj2):
    distance = math.sqrt(math.pow(obj1.xcor() - obj2.xcor(), 2) + math.pow(obj1.ycor() - obj2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


window.listen()
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
window.onkey(fire_bullet, "space")

running = True
while running:
    window.update()
    for star in stars:
        star.move()
    for chicken in chickens:
        x = chicken.xcor()
        x += chickenspeed
        chicken.setx(x)

        if chicken.xcor() > 380:
            for c in chickens:
                c.sety(c.ycor() - 35)
            chickenspeed *= -1.03
        if chicken.xcor() < -380:
            for c in chickens:
                c.sety(c.ycor() - 35)
            chickenspeed *= -1.03

        if chicken.ycor() < -300:
            running = False
            break

        if isCollision(player, chicken):
            os.system("afplay explosion.wav&")
            player.hideturtle()
            chicken.hideturtle()
            running = False
            break

        if isCollision(bullet, chicken):
            os.system("afplay explosion.wav&")
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            chicken.setposition(random.randint(-350, 350), random.randint(100, 250))

    if bulletstate == "fire":
        bullet.sety(bullet.ycor() + bulletspeed)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


window.clearscreen()

# Game Over Screen.
pn = turtle.Screen()
pn.setup(900, 600)
pn.bgpic("GO.gif")
pn.mainloop()
