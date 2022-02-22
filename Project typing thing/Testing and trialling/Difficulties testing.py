"""
Testing document for difficulties
"""
speed = 60

f = open("words1.txt", 'r')
easy_words = f.readlines()
f.close()
f = open("words2.txt", 'r')
medium_words = f.readlines()
f.close()
f = open("words3.txt", 'r')
hard_words = f.readlines()
f.close()


def spin_the_fish():
    global training, fish, angle, rpm, spinfish, type_delay
    angle += rpm
    training.forget()
    training.delete(fish)
    fish = training.create_image(200, 200, image=spinfish, tag="bal")
    training.pack()
    if rpm > 10:
        rpm = 10
    if rpm > 0:
        type_delay -= 1
        if type_delay <= 0:
            rpm -= 0.2
        else:
            rpm -= 0.023
    else:
        rpm = 0


for word in easy_words:
    if word[0] == "a":
        easy_words.remove(word)

f = open("words2.txt", 'w')
for word in easy_words:
    f.write(word)
f.close()
