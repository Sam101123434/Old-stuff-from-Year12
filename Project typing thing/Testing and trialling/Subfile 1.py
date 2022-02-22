"""
Testing some part of my code
"""


import tkinter as tk
from PIL import Image

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

main_window = tk.Tk()

file = 'spinning_ball.gif'

info = Image.open(file)
frames = info.n_frames
print(frames)

#  canvas = tk.Canvas(main_window, width="{}".format(WINDOW_WIDTH), height="{}".format(WINDOW_HEIGHT - 300), bg="white")

img = [tk.PhotoImage(file=file, format=f'gif -index{i}') for i in range(frames)]
#  pinning_ball_gif = tk.PhotoImage(file=file, format=f'gif -index{0}')

#  canvas.create_image(50, 50, image=spinning_ball_gif, anchor="center")

#  canvas.pack()
main_window.mainloop()
