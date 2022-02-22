"""
Testing file for creating moving items on canvas
"""

import tkinter as tk
import random

# constants
CANVAS_WIDTH = 590
CANVAS_HEIGHT = 590


# Functions
def object_create(event):
    canvas.create_oval(event.x-10, event.y-10, event.x+10, event.y+10,
                       tag=["object", str(random.randint(1, 10))], fill="Blue")


def object_move():
    canvas.move("object", 5, 0)
    for i in canvas.find_withtag("object"):
        overlapping = list(canvas.find_overlapping(*canvas.coords(i)))
        if i not in canvas.find_overlapping(0, 0, CANVAS_WIDTH-20, CANVAS_HEIGHT-20):
            print(canvas.gettags(i)[1])
            canvas.delete(i)
        if len(overlapping) > 1:
            overlap_func(overlapping)
    main_window.after(10, object_move)


def create_target():
    y = random.randint(0, 590)
    x = random.randint(0, 590)
    canvas.create_oval(x, y, x+10,  y+10, tag="hp2", fill="Red")


def overlap_func(objects):
    for i in objects:
        if canvas.itemcget(i, "tag") == "hp2":
            print('ok')


# Main window
main_window = tk.Tk()

canvas = tk.Canvas(main_window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                   background="BlanchedAlmond")

canvas.bind("<Button-1>", object_create)
canvas.bind("<Button-2>", create_target())
canvas.pack()
canvas.focus_set()

object_move()

main_window.mainloop()
