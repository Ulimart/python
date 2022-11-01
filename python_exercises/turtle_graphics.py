import turtle

#turtle.shape("turtle")
#for i in range(0,5):
#    turtle.forward(100)
#    turtle.right(72)
#turtle.exitonclick()

turtle.shape("circle")  ### Esto es para que sea una figurita la que hace el shape, puede ser una tortuga, cuadrado, etc
scr=turtle.Screen()  ## aun tengo DUDAS
#scr.bgcolor("yellow")
#turtle.penup()
turtle.pendown()
turtle.pensize(5)
turtle.showturtle()
turtle.color("black","red")
#turtle.begin_fill()
for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)
turtle.exitonclick()
#turtle.end_fill()
