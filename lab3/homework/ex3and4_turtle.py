from turtle import * 

def draw_square (length,colors):    
    for i in range(4):
        color(colors)
        forward(length)
        left(90)
        
shape("turtle")
# drawing_turtle(200,"yellow")

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()