# Instructions for this exercise are here https://realpython.com/beginners-guide-python-turtle/

print("Me TURTLE")

import turtle

s = turtle.getscreen
t = turtle.Turtle()
turtle.bgcolor("Blue")
turtle.title("Me Turtle")
t.fillcolor("red")
t.shape("turtle")

# First Square
t.begin_fill()
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.end_fill()
t.clear()

# Second Square
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.clear()

# First Trapezoid
t.lt(45)
t.fd(143)
t.lt(135)
t.fd(300)
t.lt(135)
t.fd(143)
t.lt(45)
t.fd(100)
t.clear()

# Second Trapezoid
t.rt(135)
t.fd(143)
t.lt(135)
t.fd(300)
t.lt(135)
t.fd(143)
t.lt(45)
t.fd(100)
t.clear()

c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(90)
t.circle(80)
c.circle(70)
t.circle(60)
c.circle(50)
t.circle(40)
c.circle(30)
t.circle(20)
c.circle(10)

c = t.clone()
t.color("magenta")
c.color("red")
t.circle(-100)
c.circle(-90)
t.circle(-80)
c.circle(-70)
t.circle(-60)
c.circle(-50)
t.circle(-40)
c.circle(-30)
t.circle(-20)
c.circle(-10)



turtle.mainloop()



