"""
canvas gif testing
"""

import tkinter as tk
from PIL import Image

root = tk.Tk()
file= "spinning_ball.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
img = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global animate
    img2 = img[count]

    gif_label.configure(image=img2)
    count += 1
    if count == frames:
        count = 0
    animate = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(animate)

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="start",command=lambda :animation(count))
start.pack()

stop = tk.Button(root,text="stop",command=stop_animation)
stop.pack()

root.mainloop()