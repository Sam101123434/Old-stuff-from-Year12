"""
Shows random colours in tkinter canvas
and prints the colour hex
"""

import tkinter as tk
import random
import time


def getorigin(eventorigin):
      x_origin = eventorigin.x
      y_origin = eventorigin.y
      draw_blob(x_origin, y_origin)


def draw_blob(x_start, y_start):
    x = x_start
    y = y_start
    last = 10
    global blob_colour
    blob_colour = random_color()
    blob = game.create_oval(x - 50, y - 50, x + 50, y + 50, fill=blob_colour, outline = "")
    move_blob(last, blob)


def move_blob(amount, item):
    count = 0
    GRAVITY = 0.1
    speed_x = 50#random.randrange(-10, 10)
    speed_y = 50#random.randrange(-10, 10)
    for i in range(amount):
        count += 1
        game.move(item, speed_x, speed_y)
        speed_y -= GRAVITY
        time.sleep(1)
        position = game.coords(item)
        print(position)


def random_color():
    """
    generates and returns a random colour hex
    """
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    return hex_number


main_window = tk.Tk()
main_window.title("waste of code")
main_window.geometry("800x500+50+50")


game = tk.Canvas(main_window, width="800", height="500", bg="white")
game.bind('<Button-1>', getorigin)
game.pack()


blob_colour = "white"


main_window.mainloop()
