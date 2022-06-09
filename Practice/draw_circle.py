import turtle
import random

wn=turtle.Screen()
wn.setup(600,604)
#wn.bgcolor(“white”)
s=turtle.Turtle()

r=10
for i in range(22):
    s.circle(r+i,46)
    j=random.random()
    k=random.random()
    l=random.random()
    s.pencolor((j,k,l))
s.penup()
s.home()
s.pendown()

m=20
for i in range(201):
    s.circle(m+i,45)
    j=random.random()
    k=random.random()
    l=random.random()
    s.pencolor((j,k,l))
s.penup()
s.home()
s.pendown()

n=30
for i in range(200):
    s.circle(n+i,45)
    j=random.random()
    k=random.random()
    l=random.random()
    s.pencolor((j,k,l))    

turtle.done()