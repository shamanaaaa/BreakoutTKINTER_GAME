import tkinter as tk
import random


class MainRectangle:
    def __init__(self, x, y):
        self.color = random.choice(["blue", "red", "green", "orange", "yellow"])
        self.height = 40
        self.width = 80
        self.x = x
        self.y = y

    def draw_rectangle(self):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, width=2, fill=self.color)


# create gui
gui = tk.Tk()
gui.title("BREAKOUT RETRO GAME")
canvas_width, canvas_height = 1044, 768
canvas = tk.Canvas(gui, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

# create bottom moving rectangle object
x1, y1 = canvas_width / 2 - 100, canvas_height - 20
c1 = canvas.create_rectangle(x1, y1, x1 + 200, y1 + 20, fill='violet')


# fill rectangles list with main rectangles
def create_all_rectangles():
    rectangles = []
    x_step = 2
    for rectangle1 in range(13):
        rectangles.append(MainRectangle(x_step, 200))
        x_step += 80
    x_step = 2
    for rectangle2 in range(13):
        rectangles.append(MainRectangle(x_step, 240))
        x_step += 80
    x_step = 2
    for rectangle3 in range(13):
        rectangles.append(MainRectangle(x_step, 280))
        x_step += 80
    x_step = 2
    for rectangle4 in range(13):
        rectangles.append(MainRectangle(x_step, 320))
        x_step += 80
    return rectangles


# draw rectangles on board
all_rectangles = create_all_rectangles()
for rectangle in all_rectangles:
    rectangle.draw_rectangle()


# moving keys to bottom rectangle
def keypress(event):
    x, y = 0, 0
    if event.keysym == "Left":
        if not canvas.coords(c1)[0] == 2:
            x = -10
    elif event.keysym == "Right":
        if not canvas.coords(c1)[0] == 842:
            x = 10
    canvas.move(c1, x, y)


gui.bind("<Left>", keypress)
gui.bind("<Right>", keypress)

gui.mainloop()
