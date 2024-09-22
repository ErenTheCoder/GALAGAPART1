import pgzrun
import random

WIDTH = 1200
HEIGHT = 600 

WHITE = (255,255,255)
BLUE = (0,0,200)

ship = Actor("galaga.png")
bug = Actor("bug.png")

ship.pos = (WIDTH//2,HEIGHT-60)

speed = 5

bullets = []

enemies = []

enemies.append(Actor('bug'))

enemies[-1].x = 10

enemies[-1].y = -100

SCORE = 0

def displayScore():
    screen.draw,text(str(score),(50,30))


def draw():
    screen.clear()
    screen.fill(BLUE)




pgzrun.go()