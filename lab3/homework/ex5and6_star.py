from turtle import *

shape("turtle")

def draw_star(x,y,length):
    setposition(x,y)
    for i in range(5):
        right(144)
        forward(length)

# draw_star(4,5,100)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()    