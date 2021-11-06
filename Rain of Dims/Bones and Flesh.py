import turtle
import random
import os

start_m = turtle.Screen()
start_m.setup(800, 600)
start_m.bgcolor("black")
start_m.title("Attack The Base!")
start_m.bgpic("z2.gif")
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
window.title("Attack The Base!")
window.tracer(0)


images = ["ship.gif", "dim.gif", "boss.gif", "missile.gif",
          "red_star.gif", "white_star.gif", "yellow_star.gif"]
for image in images:
    window.register_shape(image)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("green")
        self.width(2)
        self.speed(0)
        self.setheading(0)

    def health_meter(self):
        if ship:
            self.goto(ship.xcor() - 20, ship.ycor() + 15)
            self.pendown()
            self.fd(40 * (ship.health / ship.max_health))
            self.penup()
            self.hideturtle()
        if dims:
            self.goto(dim.xcor() - 15, dim.ycor() + 15)
            self.pendown()
            self.fd(30 * (dim.health / dim.max_health))
            self.penup()
            self.hideturtle()

    def ammo_counter(self):
        ammo = 0
        for missile in missiles:
            if missile.state == "ready":
                ammo += 1
            for x in range(ammo):
                self.goto(300 + 30*x, 280)
                self.shape("missile.gif")
                self.stamp()

    def draw_score(self):
        self.goto(-80, 270)
        self.write(f"Score: {ship.score}  Kills: {ship.kills}", font=("Comic sans", 16, "normal"))


class Ship(turtle.Turtle):
    def __init__(self, shape, x, y):
        turtle.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.dy, self.dx, self.score, self.kills = 0, 0, 0, 0
        self.max_health = 30
        self.health = self.max_health

    def up(self):
        self.dy = 1.75
    def down(self):
        self.dy = -1.75
    def move_left(self):
        self.dx = -1.75
    def move_right(self):
        self.dx = 1.75
    def move(self):
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)
        if self.ycor() > 280:
            self.sety(280)
            self.dy = 0
        elif self.ycor() < -280:
            self.sety(-280)
            self.dy = 0
        if self.xcor() < -380:
            self.setx(-380)
            self.dx = 0
        elif self.xcor() > -180:
            self.setx(-180)
            self.dx = 0


class Missile(turtle.Turtle):
    def __init__(self, shape, x, y):
        turtle.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.dx = 0
        self.state = "ready"

    def fire(self):
        self.state = "firing"
        self.goto(ship.xcor(), ship.ycor())
        self.dx = 2.5

    def move(self):
        if self.state == "firing":
            self.setx(self.xcor() + self.dx)
        if self.xcor() > 400:
            self.state = "ready"
            self.sety(1000)


class Enemy(turtle.Turtle):
    def __init__(self, shape):
        turtle.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)
        self.goto(random.randint(400, 480), random.randint(-280, 280))
        self.dx, self.dy = random.randint(1,5)/-3 , 0
        self.max_health = random.randint(5, 15)
        self.health = self.max_health
        self.type = "dim"

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
        if self.xcor() < -400:
            self.goto(random.randint(400, 480), random.randint(-280, 280))
        if self.ycor() < -280:
            self.sety(-280)
            self.dy *= -1
        elif self.ycor() > 280:
            self.sety(280)
            self.dy *= -1

    def boss_spawn(self):
        self.shape("boss.gif")
        self.max_health = 40
        self.health = self.max_health
        self.dy = random.randint(-5,5)/3

    def enemy_respawn(self):
        self.dy = 0
        self.shape("dim.gif")
        self.max_health = random.randint(5, 15)
        self.health = self.max_health


class Star(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        star_images = ["yellow_star.gif", "red_star.gif", "white_star.gif"]
        self.shape(random.choice(star_images))
        self.penup()
        self.speed(0)
        self.goto(random.randint(-400, 400), random.randint(-290, 290))
        self.dx = random.randint(1,5)/-20

    def move(self):
        self.setx(self.xcor() + self.dx)
        if self.xcor() < -400:
            self.goto(random.randint(400, 480), random.randint(-290, 290))


pen = Pen()
ship = Ship("ship.gif", -350, 0)
missiles = []
for dummy in range(3):
    missiles.append(Missile("missile.gif", 0, 1000))
dims = []
for dummy in range(5):
    dims.append(Enemy("dim.gif"))
stars = []
for dummy in range(30):
    stars.append(Star())


def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.fire()
            os.system("afplay laser.wav&")
            break

def quit_game():
    global running
    running = False

window.listen()
window.onkeypress(quit_game, "q")
window.onkeypress(ship.up, "Up")
window.onkeypress(ship.down, "Down")
window.onkeypress(ship.move_left, "Left")
window.onkeypress(ship.move_right, "Right")
window.onkeypress(fire_missile, "space")


running = True
while running:
    window.update()
    pen.clear()
    ship.move()

    for missile in missiles:
        missile.move()
    for star in stars:
        star.move()
    for dim in dims:
        dim.move()
        pen.health_meter()
        pen.ammo_counter()

        for missile in missiles:
            if dim.distance(missile) < 25:
                os.system("afplay explosion.wav&")
                dim.health -= 5
                if dim.health <= 0:
                    dim.goto(random.randint(400, 480), random.randint(-280, 280))
                    ship.kills += 1
                    if ship.kills % 3 == 0:
                        dim.boss_spawn()
                    else:
                        dim.enemy_respawn()
                else:
                    dim.setx(dim.xcor() + 20)
                missile.dx = 0
                missile.goto(0, 1000)
                missile.state = "ready"
                ship.score += 10

        if dim.distance(ship) < 28:
            os.system("afplay explosion.wav&")
            ship.health -= random.randint(5, 10)
            dim.health -= random.randint(5, 10)
            dim.goto(random.randint(400, 480), random.randint(-280, 280))
            if ship.health <= 0:
                exit()
                break
    if ship.score >= 100:
        running = False
        break
    pen.draw_score()


window.clearscreen()
pn = turtle.Screen()
pn.setup(900, 600)
pn.bgpic("z1.gif")
pn.mainloop()
