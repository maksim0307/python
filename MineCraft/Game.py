from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
app = Ursina()
Sky = texture="травка00"

player = FirstPersonController()
window.fullscreen = True

boxes = []

for i in range(25):
    for k in range(20):
        box=Button(
            position=(i,0,k),
            color = color.white,
            hightlight_color =color.white10,
            model="cube",
            parent=scene,
            texture=load_texture("травка"),
        )
        boxes.append(box)
def input(key):
    if key == "escape":
        quit()
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                # boxes.remove(box)
                destroy(box)
            if key == "right mouse down":
                newBox = Button(
                    position = box.position + mouse.normal,
                    color = color.white,
                    model = "ball",
                    hilight_color = color.white10,
                    parent = scene,
                    texture =load_texture("травка01")
                )
                boxes.append(newBox)
            if key == "1":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    parent=scene,
                    texture=load_texture("травка02")
                )
                boxes.append(newBox)
            if key == "2":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    parent=scene,
                    texture=load_texture("травка03")
                )
                boxes.append(newBox)
            if key == "3":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    parent=scene,
                    texture=load_texture("травка04")
                )
                boxes.append(newBox)

app.run()



