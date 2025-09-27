'''Rajzol egy 150 pontos egyenlő szárú háromszöget a képernyő közepére
A színe legyen piros,
a rajzolás induljon az a betűre,
 a kilépés q betűre'''

import turtle

import turtle

ablak = turtle.Screen()
turtle.color("red")

def haromszog():
    turtle.hideturtle()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    for _ in range(3):
        turtle.forward(150)
        turtle.left(120)

def kilep():
    turtle.bye()

turtle.listen()
turtle.onkey(haromszog, "a")
turtle.onkey(kilep, "q")
turtle.mainloop()

