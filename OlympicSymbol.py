import turtle

turtle.color("blue")  #顏色藍色
turtle.penup()         #舉起筆
turtle.goto(-110, -25)  
turtle.pendown()       #放下筆
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

turtle.done()  #結束