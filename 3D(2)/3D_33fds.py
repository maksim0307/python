# импортируем Ursina
from ursina import *
# импорт 3D камера
from ursina.prefabs.first_person_controller import FirstPersonController
# создать экземпляр класса Ursina
app = Ursina()
# создаем класс Voxel
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            color=color.random_color(),
            highlight_color=color.random_color()
        )
  # создать методы строить и разрушить
    def input(self, key):
        if(self.hovered):
            if(key == "left mouse down"):
                destroy(self)
            if(key == "right mouse down"):
                voxel = Voxel(position=self.position + mouse.normal)
# постоить x * x Voxel площадку
for x in range(10):
    for z in range (10):
        voxel = Voxel(position=(x,0,z))
# создать игрока
player = FirstPersonController()
app.run()











