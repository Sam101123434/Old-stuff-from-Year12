"""This code runs the leaderboard for my typing game."""
import tkinter as tk
import json


def take_score(leaderboard):
    """Return the score from list."""
    return leaderboard[0]


main_window = tk.Tk()
main_window.title("Leaderboard")
main_window.configure(bg='sky blue')
main_window.geometry("{}x{}+50+50".format(400, 600))

with open("highscores_file.txt") as f:
    highscores = json.load(f)['scores']
highscores.sort(key=take_score, reverse=True)

empty_label1 = tk.Label(main_window, bg='sky blue')
empty_label1.pack()
title = tk.Label(main_window, text="Hall Of Fame", relief='ridge', bd=10,
                 pady=15, padx=15, font='comicsans', bg='white')
title.pack()
empty_label2 = tk.Label(main_window, bg='sky blue')
empty_label2.pack()
lbl0 = tk.Label(main_window)
lbl1 = tk.Label(main_window)
lbl2 = tk.Label(main_window)
lbl3 = tk.Label(main_window)
lbl4 = tk.Label(main_window)
lbl5 = tk.Label(main_window)
lbl6 = tk.Label(main_window)
lbl7 = tk.Label(main_window)
lbl8 = tk.Label(main_window)
lbl9 = tk.Label(main_window)
labels = [lbl0, lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9]
for row in labels:
    row.configure(anchor='w', width=20, bg='white', pady=5, padx=5, bd=10,
                  relief='ridge')
for i in range(len(labels)):
    labels[i].configure(text="{} : {}".format(highscores[i][0],
                                              highscores[i][1]))
    labels[i].pack()
num0 = tk.Label(main_window)
num1 = tk.Label(main_window)
num2 = tk.Label(main_window)
num3 = tk.Label(main_window)
num4 = tk.Label(main_window)
num5 = tk.Label(main_window)
num6 = tk.Label(main_window)
num7 = tk.Label(main_window)
num8 = tk.Label(main_window)
num9 = tk.Label(main_window)
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
for i in range(len(nums)):
    nums[i].configure(bg='sky blue', text=str(i + 1) + ".", fg='black',
                      font='Helvetica', relief='ridge', anchor='e',
                      pady=2, padx=5)
    if i == 9:
        nums[i].place(x=61, y=(i + 1) * 45 + 75)
    else:
        nums[i].place(x=70, y=(i + 1) * 45 + 75)

main_window.mainloop()
