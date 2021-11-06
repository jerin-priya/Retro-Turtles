import turtle
import random

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Attack The Base!")
wn.tracer(0)

agent = turtle.Turtle()
agent.speed(0)
agent.penup()


class Player():
    def __init__(self, color, x, y, shape):
        self.color = color
        self.x, self.y = x, y
        self.shape = shape
        self.dy = 0
        self.dx = 0

    def up(self):
        self.dy = 0.4
    def down(self):
        self.dy = -0.4
    def left(self):
        self.dx = -0.4
    def right(self):
        self.dx = 0.4

    def move(self):
        self.y = self.y + self.dy
        self.x = self.x + self.dx
        if self.y > 280:
            self.y, self.dy = 280, 0
        elif self.y < -280:
            self.y, self.dy= -280, 0
        if self.x < -390:
            self.x, self.dx = -390, 0
        elif self.x > -190:
            self.x, self.dx = -190, 0

    def distance(self, other):
        return ( (self.x-other.x)**2 + (self.y-other.y)** 2 ) ** 0.5

    def render(self, agent):
        agent.goto(self.x, self.y)
        agent.shape(self.shape)
        agent.color(self.color)
        agent.shapesize(1, 1, 0)
        agent.stamp()


class Missile():
    def __init__(self, color, x, y, shape):
        self.color, self.shape = color, shape
        self.x, self.y = x, y
        self.size = 0.3
        self.dx = 0

    def fire(self):
        self.x = player.x
        self.y = player.y
        self.dx = 1

    def move(self):
        self.x = self.x + self.dx

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self, agent):
        agent.goto(self.x, self.y)
        agent.shape(self.shape)
        agent.color(self.color)
        agent.shapesize(0.3, 0.3, 0)
        agent.stamp()


class Enemy():
    def __init__(self):
        colors = ["yellow", "purple", "blue", "white", "gray"]
        self.color = random.choice(colors)
        self.x = 400
        self.y = random.randint(-290, 290)
        self.shape = "square"
        self.dx = random.randint(1, 5) / -10

    def move(self):
        self.x = self.x + self.dx
        if self.x < -400:
            self.x = random.randint(400, 480)
            self.y = random.randint(-350, 350)
            self.dx *= 1.1

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self, agent):
        agent.goto(self.x, self.y)
        agent.shape(self.shape)
        agent.color(self.color)
        agent.shapesize(1, 1, 0)
        agent.stamp()




player = Player("green", -350, 0, "triangle")
missile = Missile("red", 0, 1000, "circle")
enemies = []
for _ in range(5):
    enemies.append(Enemy())


# Keyboard binding
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.left, "Left")
wn.onkeypress(player.right, "Right")
wn.onkeypress(missile.fire, "space")


while True:
    wn.update()
    agent.clear()

    player.move()
    missile.move()
    player.render(agent)
    missile.render(agent)

    for enemy in enemies:
        enemy.move()

        if enemy.distance(missile) < 13:
            enemy.x, enemy.y = 400, random.randint(-350, 350)
            enemy.dx *= 0.8
            missile.dx, missile.x, missile.y = 0, 0, 1000
        if enemy.distance(player) < 20:
            print("Game over!")
            exit()

        enemy.render(agent)


