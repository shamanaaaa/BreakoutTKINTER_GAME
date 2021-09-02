import random
import tkinter as tk
import time


# bottom rectangle class


class MainRectangle:
    def __init__(self, x, y):
        self.color = random.choice(["blue", "red", "green", "orange", "yellow"])
        self.height = 40
        self.width = 80
        self.x = x
        self.y = y

    def draw_rectangle(self):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, width=2, fill=self.color)


game_on = True

# create gui
gui = tk.Tk()
gui.title("BREAKOUT RETRO GAME")
canvas_width, canvas_height = 1044, 700
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
        rectangles.append(MainRectangle(x_step, 40))
        x_step += 80
    x_step = 2
    for rectangle2 in range(13):
        rectangles.append(MainRectangle(x_step, 80))
        x_step += 80
    x_step = 2
    for rectangle3 in range(13):
        rectangles.append(MainRectangle(x_step, 120))
        x_step += 80
    x_step = 2
    for rectangle4 in range(13):
        rectangles.append(MainRectangle(x_step, 160))
        x_step += 80
    return rectangles


# draw rectangles on board
all_rectangles = create_all_rectangles()
for rectangle in all_rectangles:
    rectangle.draw_rectangle()


# moving keys for bottom rectangle
def keypress(event):
    x, y = 0, 0
    if event.keysym == "Left":
        if not canvas.coords(c1)[0] == 2:
            x = -10
    elif event.keysym == "Right":
        if not canvas.coords(c1)[0] == 842:
            x = 10
    elif event.keysym == "w":
        move_ball(0, -1)
    elif event.keysym == "a":
        move_ball(-1, 0)
    elif event.keysym == "s":
        move_ball(0, 1)
    elif event.keysym == "d":
        move_ball(1, 0)
    canvas.move(c1, x, y)


# ball
def create_ball():
    x, y = 500, 640
    return canvas.create_oval(x, y, x + 10, y + 10, fill="red")


ball = create_ball()


# ball movement
def move_ball(x, y):
    return canvas.move(ball, x, y)


def get_direction_before_collision():
    global ball_coordinates
    ball_coordinates = ball_coordinates[-5:]
    if ball_coordinates[0][0] > ball_coordinates[4][0] and \
            ball_coordinates[0][1] > ball_coordinates[4][1]:
        direction = "LU"
        return direction
    if ball_coordinates[0][0] < ball_coordinates[4][0] and \
            ball_coordinates[0][1] > ball_coordinates[4][1]:
        direction = "RU"
        return direction
    if ball_coordinates[0][0] < ball_coordinates[4][0] and \
            ball_coordinates[0][1] < ball_coordinates[4][1]:
        direction = "RD"
        return direction
    if ball_coordinates[0][0] > ball_coordinates[4][0] and \
            ball_coordinates[0][1] < ball_coordinates[4][1]:
        direction = "LD"
        return direction


def canvas_collision():
    global side
    if canvas.coords(ball)[0] == 5:
        side = "left"
        return True
    elif canvas.coords(ball)[1] == 5:
        side = "up"
        return True
    elif canvas.coords(ball)[3] == 700:
        side = "down"
        return True
    elif canvas.coords(ball)[2] == 1044:
        side = "right"
        return True


def object_collision():
    q1, q2, q3, q4 = canvas.coords(ball)
    objects_in_collision = (canvas.find_overlapping(q1, q2, q3, q4))
    for n in range(2, 54):
        if n in objects_in_collision:
            canvas.delete(n)
            return True


ball_x = -1
ball_y = -1
ball_coordinates = []
side = ""

while game_on:
    ball_coordinates.append(canvas.coords(ball))
    object_collision()
    if canvas_collision():
        if get_direction_before_collision() == "LU" and side == "left" or get_direction_before_collision() == "LU" and object_collision():
            print("_____IF1______")
            ball_x = 1
            ball_y = -1
        if get_direction_before_collision() == "LU" and side == "up":
            print("_____IF2______")
            ball_x = -1
            ball_y = 1
        if get_direction_before_collision() == "RU" and side == "right":
            print("_____IF3______")
            ball_x = -1
            ball_y = -1
        if get_direction_before_collision() == "RU" and side == "up":
            print("_____IF4______")
            ball_x = 1
            ball_y = 1
        if get_direction_before_collision() == "LD" and side == "left":
            print("_____IF5______")
            ball_x = 1
            ball_y = 1
        if get_direction_before_collision() == "LD" and side == "down":
            print("_____IF8______")
            ball_x = -1
            ball_y = -1
        if get_direction_before_collision() == "RD" and side == "down":
            print("_____IF6______")
            ball_x = 1
            ball_y = -1
        if get_direction_before_collision() == "RD" and side == "right":
            print("_____IF7______")
            ball_x = -1
            ball_y = 1

    time.sleep(0.001)
    side = "left"
    move_ball(ball_x, ball_y)
    canvas.update()
    gui.bind("<Left>", keypress)
    gui.bind("<Right>", keypress)
    gui.bind("<w>", keypress)
    gui.bind("<a>", keypress)
    gui.bind("<s>", keypress)
    gui.bind("<d>", keypress)

gui.mainloop()
