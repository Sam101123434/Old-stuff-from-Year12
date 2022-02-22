import tkinter as tk
from PIL import Image, ImageTk

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
nav = "00"

main_window = tk.Tk()
main_window.title("waste of code")
main_window.geometry("{}x{}+50+50".format(WINDOW_WIDTH, WINDOW_HEIGHT))
nav_bar = tk.Label(main_window, text="{}".format(nav))

bg_img = ImageTk.PhotoImage(Image.open("background.jpg"))
panel = tk.Label(main_window, image = bg_img)
title_img = ImageTk.PhotoImage(Image.open("title.png"))
title = tk.Label(main_window, image = title_img)
train_button = tk.Button(main_window, text="Train", width=20, height=4)

nav_bar.pack()
title.pack()
train_button.pack(side="bottom")
panel.pack(side = "bottom", fill = "both", expand = "yes")

main_window.mainloop()
