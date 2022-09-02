import turtle

k = turtle.Turtle()

turtle.title("circle rainbow infloop")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

while (True):
    for i in range(1000):
        for colors in ["red", "blue", "green", "white", "pink", "yellow"]:
            turtle.color(colors)
            turtle.circle(100)  
            turtle.left(10)

turtle.mainloop()  