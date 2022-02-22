"""Run file for trialling the typing test."""
import tkinter as tk
import random
f = open('words.txt', 'r')
words_list = f.readlines()
f.close()
for word in words_list:
    words_list[words_list.index(word)] = word[:-1]

main_window = tk.Tk()
main_window.geometry("1000x700+150+0")
typing_box = tk.Entry(main_window, bd=5, textvariable="StringVar", width=50)
test_words_display1 = tk.Label(main_window, font='Ariel 30', justify='center',
                               width=60)
test_time_display = tk.Label(main_window, font='Helvetica 50', text="Time:30")

test_words_display1.configure(text=random.sample(words_list, 5))
test_time_display.place(anchor='ne', x=1000, y=0)
test_words_display1.place(anchor='center', relx=0.5, y=350)
typing_box.place(anchor="center", relx=0.5, y=700 - 150)
main_window.mainloop()
