from ursina import *

from ursina.prefabs.first_person_controller \
    import FirstPersonController
app = Ursina()
Sky()
player = FirstPersonController()
window.fullscreen = True

arm = Entity(
    parent=camera.ui,
    model="cube",
    # color=color.pink,
    position=(0.1, -0.6),
    rotation=(150,-10.6),
    scale=(0.2, 0.2, 1.5),
    texture = load_texture("лава")
)

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(
            position=(i, 0.5, j),
            highlight_color=color.white,
            color = color.white,
            model="cube",
            texture=load_texture("ТРАВКА3"),
            parent=scene
        )
        boxes.append(box)
# def input(key):
#     if held_keys["escape"]:

def input(key):
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.olive,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("wood"),
                    parent=scene
                )
                boxes.append(newBox)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)


app.run()
