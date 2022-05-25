from ursina import *
from ursina import curve

app = Ursina()
player = Animation(
    "img\\d",
    collider="box",
    x=-15,
    y=5)

camera.orthographic = True
camera.fov = 20

boom = Animation(
    "img\\boom",
    model="cube",
    texture="img\\boom",
    scale=3,
    x=25,
    y=25
)

Entity(
    model="quad",
    texture="img\\background",
    scale=36,
    z=1
)

monster = Entity(
    model="cube",
    texture="img\\monster",
    collider="box",
    scale=3,
    x=20,
    y=-10
)

monsters = []


def createMonster():
    newMonster = duplicate(monster,
                 y=-5 + (10124 * time.dt) % 15)
    monsters.append(newMonster)
    invoke(createMonster, delay=1)


createMonster()

def update():
    player.y += held_keys["w"] * 6 * time.dt
    player.y -= held_keys["s"] * 6 * time.dt

    for m in monsters:
        m.x -= 4 * time.dt
        touch = m.intersects()
        if touch.hit:
            boom.x = m.x
            boom.y = m.y
            monsters.remove(m)
            destroy(m)

        touch1 = player.intersects()
        if touch1.hit:
            invoke(destroy, player)
            quit()



def input(key):
    if key == "q":
        quit()
    if key == "enter":
        bullet = Entity(
            "img//bullet",
            texture="img\\bullet",
            collider="cube",
            model="cube",
            x=player.x+2,
            y=player.y
        )
        bullet.animate_x(
            30, duration=2,
            curve=curve.linear
        )
        invoke(destroy, bullet, delay=1)

app.run()
