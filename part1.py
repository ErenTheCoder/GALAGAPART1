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

enemies.append(actor('bug'))
enemies[-1].x = 10
enemies[-1].y = -100

def displayScore():
    screen.draw,text(str(score),(50,30))

def on_key_down(key):
    if key ==keys.SPACE:
        bullets.append(actor('bullet'))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

def update():
    global score

    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0

    elif keyboard.right:
        ship.x -= speed
        if ship.x >= WIDTH:
            ship.x = WIDTH

for bullet in bullets:
    if bullet.y <= 0 :
            bullets.remove(bullet)
    else:
        bullet.y -= 10
   
            
for enemy in enemies:
     enemy.y +=5
     if enemy.y >= HEIGHT:
          enemy.y = -100
          enemy.x = random.randint(50,WIDTH-50)
        



def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()





pgzrun.go()