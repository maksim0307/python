import ursina

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

ground = Entity(model="plane",
                texure="grass",
                collider="mesh",
                scale=(100,10,100)
                )

window.fullscreen = True

for i in range(10):
    randomNumber = random.uniform(-0,0)
    block = Entity(model="cube",
                   color=color.white10,
                   collider="box",
                   texture="withe_cube",
                   position=(randomNumber,i+1,3+i*1,),
                   scale=(3,1,3)
                   )

def input(key):
    if key == "escape":
        quit()

player = FirstPersonController()
# player.jump_height = 15
Sky()
app.run()

