import turtle

def negyszog (x, y):
    # a = 5
    # b = 4
    ker = 2 * x + 2 * y
    ter = x * y
    if x == y:
        alakzat = "négyzet"
    else:
        alakzat = "teglalap"
    return ker, ter, alakzat

def negyzet():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(5)

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def pont(x, y):
        turtle.goto(x, y)
        turtle.dot(10, "black")

def dobas():
    import random
    turtle.clear()
    turtle.hideturtle()
    negyzet()
    szam = random.randint(1, 6)
    turtle.penup()

    if szam == 1:
        pont(0, 0)
    elif szam == 2:
        pont(-30, 30)
        pont(30, -30)
    elif szam == 3:
        pont(-30, 30)
        pont(0, 0)
        pont(30, -30)
    elif szam == 4:
        pont(-30, 30)
        pont(30, 30)
        pont(30, -30)
        pont(-30, -30)
    elif szam == 5:
        pont(-30, 30)
        pont(30, 30)
        pont(0,  0)
        pont(30, -30)
        pont(-30, -30)
    elif szam == 6:
        pont(-30, 30)
        pont(30, 30)
        pont(30, -30)
        pont(-30, -30)
        pont(-30, 0)
        pont(30, 0)




#app
ablak = turtle.Screen()

turtle.listen()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye,"Escape")
turtle.mainloop()





if __name__ == '__main__':
    a = 10
    b = 26

    eredmeny = negyszog(a, b)
    print (f"A {eredmeny[2]} kerület =", eredmeny[0])
    print (f"A {eredmeny[2]} terület =", eredmeny[1])
    print("saját hívás")







