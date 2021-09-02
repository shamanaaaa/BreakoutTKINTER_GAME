import random
import tkinter as tk
from tkinter import messagebox
import time


# single rectangle class
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
game_objects = 104

# create gui
gui = tk.Tk()
gui.title("BREAKOUT RETRO GAME")
canvas_width, canvas_height = 1064, 720
canvas = tk.Canvas(gui, width=canvas_width, height=canvas_height, bg='lightblue')

# score label
score_text = tk.StringVar()
score_label = tk.Label(canvas, textvariable=score_text, fg='white', bg='black')
score = canvas.create_window(60, 21, window=score_label)

# lives label
lives_text = tk.StringVar()
lives_label = tk.Label(canvas, textvariable=lives_text, fg='white', bg='black')
lives = canvas.create_window(150, 21, window=lives_label)

canvas.pack()

# creating wall rectangles
top_wall = canvas.create_rectangle(0, 0, 1064, 39, fill='black')
left_wall = canvas.create_rectangle(0, 0, 11, 720, fill='black')
right_wall = canvas.create_rectangle(1054, 0, 1064, 720, fill='black')
bottom_wall = canvas.create_rectangle(0, 710, 1064, 720, fill='black')

# create bottom moving rectangle object
x1, y1 = canvas_width / 2 - 100, canvas_height - 20
c1 = canvas.create_rectangle(x1, y1, x1 + 200, y1 + 20, fill='violet')


# c1 = canvas.create_rectangle(0, 700, 1064, 720, fill='violet')


# fill rectangles list with main rectangles
def create_all_rectangles():
    rectangles = []
    x_step = 13
    for rectangle1 in range(13):
        rectangles.append(MainRectangle(x_step, 40))
        x_step += 80
    x_step = 13
    for rectangle2 in range(13):
        rectangles.append(MainRectangle(x_step, 80))
        x_step += 80
    x_step = 13
    for rectangle3 in range(13):
        rectangles.append(MainRectangle(x_step, 120))
        x_step += 80
    x_step = 13
    for rectangle4 in range(13):
        rectangles.append(MainRectangle(x_step, 160))
        x_step += 80
    return rectangles


# draw rectangles on board
all_rectangles = create_all_rectangles()
for rectangle in all_rectangles:
    rectangle.draw_rectangle()


# moving keys for bottom rectangle and WASD keys for testing
def keypress(event):
    x, y = 0, 0
    if event.keysym == "Left":
        if not canvas.coords(c1)[0] == 2:
            x = -30
    elif event.keysym == "Right":
        if not canvas.coords(c1)[0] == 842:
            x = 30
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
    return canvas.create_oval(x, y, x + 20, y + 20, fill="red")


ball = create_ball()


# ball movement
def move_ball(x, y):
    return canvas.move(ball, x * 3, y * 3)


def wall_collision():
    q1, q2, q3, q4 = canvas.coords(ball)
    objects_in_collision = (canvas.find_overlapping(q1, q2, q3, q4))
    if 4 in objects_in_collision:
        return "left_wall"
    if 6 in objects_in_collision:
        return "bottom_wall"
    if 3 in objects_in_collision:
        return "top_wall"
    if 5 in objects_in_collision:
        return "right_wall"


def rectangle_collision():
    q1, q2, q3, q4 = canvas.coords(ball)
    objects_in_collision = (canvas.find_overlapping(q1, q2, q3, q4))
    for n in range(8, 60):
        if n in objects_in_collision:
            return n


def pad_bounce():
    q1, q2, q3, q4 = canvas.coords(ball)
    objects_in_collision = (canvas.find_overlapping(q1, q2, q3, q4))
    if 7 in objects_in_collision:
        return True


def game_over():
    messagebox.showinfo(title="GAME OVER", message=f"Your score is: {score}")
    canvas.destroy()


ball_x = -1
ball_y = -1
score = 0
lives = 3

while game_on:
    score_text.set(f"SCORE: {score}")
    lives_text.set(f"LIVES: {lives}")
    wall_side = wall_collision()
    rectangle_to_delete = rectangle_collision()
    if pad_bounce():
        if ball_x == 1 and ball_y == 1:
            ball_x = 1
            ball_y = -1
        if ball_x == -1 and ball_y == 1:
            ball_x = -1
            ball_y = -1

    if rectangle_collision():
        score += 5
        canvas.delete(rectangle_to_delete)
        if ball_x == -1 and ball_y == -1:
            ball_x = -1
            ball_y = 1
        if ball_x == 1 and ball_y == -1:
            ball_x = 1
            ball_y = 1
    if wall_collision():
        if wall_side == "left_wall" and ball_x == -1 and ball_y == -1:
            ball_x = 1
            ball_y = -1
        if wall_side == "left_wall" and ball_x == -1 and ball_y == 1:
            ball_x = 1
            ball_y = 1
        if wall_side == "top_wall" and ball_x == 1 and ball_y == -1:
            ball_x = 1
            ball_y = 1
        if wall_side == "bottom_wall" and ball_x == 1 and ball_y == 1:
            lives -= 1
            if lives == 0:
                game_over()
            time.sleep(3)
            canvas.moveto(ball, 500, 640)
            ball_x = -1
            ball_y = -1
        if wall_side == "right_wall" and ball_x == 1 and ball_y == -1:
            ball_x = -1
            ball_y = -1
        if wall_side == "top_wall" and ball_x == -1 and ball_y == -1:
            ball_x = -1
            ball_y = 1
        if wall_side == "right_wall" and ball_x == 1 and ball_y == 1:
            ball_x = -1
            ball_y = 1
        if wall_side == "bottom_wall" and ball_x == -1 and ball_y == 1:
            lives -= 1
            if lives == 0:
                game_over()
            time.sleep(3)
            canvas.moveto(ball, 500, 640)
            ball_x = -1
            ball_y = -1

    time.sleep(0.005)
    move_ball(ball_x, ball_y)
    canvas.update()
    gui.bind("<Left>", keypress)
    gui.bind("<Right>", keypress)
    gui.bind("<w>", keypress)
    gui.bind("<a>", keypress)
    gui.bind("<s>", keypress)
    gui.bind("<d>", keypress)


gui.mainloop()
