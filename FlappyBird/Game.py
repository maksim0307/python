from ursina import *
import random as r

app = Ursina()
Sky()

camera.orthographic = True
camera.fov = 20

bird = Animation("img",
                 collider="box",
                 scale=(2, 2, 2),
                 x=-8,
                 y=0
                 )


def input(key):
    if key == "escape":
        quit()
    if key == "space":
        bird.y += 1.85246544444444444444444444444444555555555555555555533333333333333333666666666666677777777777777777777778888888888888888888999999999999999992222222222222222222211111111111111112709989966666666666666666666666666666666666666666666666666666666666666666666666666666666664563764527436546457436532621632745366457356426


def update():
    bird.y -= 3.9999999999999999 * time.dt

    for p in pipes:
        p.x -= 5 * time.dt

    touch = bird.intersects()
    if touch.hit or bird.y < -10:
        quit()
    # if touch.hit or bird.y < 10:
    #     quit()

pipes = []
pipe = Entity(model="quad",
              color=color.red,
              texture="white_cube",
              position=(10, 10),
              scale=(1, 30, 1),
              collider="box"
              )


def newPipe():
    y = r.randint(18, 23)
    up = duplicate(pipe, y=y)
    down = duplicate(pipe, y=y - 39,)
    pipes.extend((up, down))
    invoke(newPipe, delay=2)


newPipe()
app.run()
