import tkinter
from tkinter import colorchooser, HORIZONTAL

window = tkinter.Tk()
window.title("Paint от ТаДжИкОвЪ(при поддержке евреев)")

brush_size = 3
brush_color = "black"

def buttonColorHandler():
    global brush_color
    brush_color = colorchooser.askcolor()[1]

def buttonSizeHandler():
    global brush_size
    brush_size = button_scale.get()

def buttonClearHandler():
    canvas.delete("all")

def draw(event):
    global brush_size
    global brush_size
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    canvas.create_oval(x1,y1,x2,y2,
                       fill=brush_color,
                       outline = brush_color)
#                            outline = brush_color  без   3д   ефекта
#                                                   outline = brush_color
canvas = tkinter.Canvas(window,
                        width=800,
                        height=600,
                        bg="white")

canvas.grid(row=2, column=0, columnspan=7)
canvas.bind("<B1-Motion>",draw)

button_color = tkinter.Button(window,
                              text="Цвет",
                              font=("Arial", 18),
                              command=buttonColorHandler
                              )
button_scale = tkinter.Scale(window,
                             from_=0,
                             to=70,
                             orient=HORIZONTAL
                             )

button_size = tkinter.Button(window,
                             text="Настроить размер",
                             bg="silver",
                             fg="black",
                             font=("Arial", 18),
                             command=buttonSizeHandler
                             )

button_delete = tkinter.Button(window,
                               text="Отчистить все",
                               bg="red",
                               fg="white",
                               font=("Arial", 18),
                               command=buttonClearHandler
                               )
button_color.grid(row=0, column=1)
button_scale.grid(row=0, column=2)
button_size.grid(row=0, column=3)
button_delete.grid(row=0,column=4)

tkinter.mainloop()
