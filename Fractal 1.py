import turtle as t
import random

b=int(input("Inserte un parametro de 1 a 3"))

t.Screen().bgcolor("black")
t.shape("turtle")
t.speed(100)
t.pensize(1)

for i in range(0,900,3):
    a=random.randint(0,1)
    t.left(0.2)
    if a==0:
        t.color("white")
    else:
        t.color("lightcyan")
    for j in range(0,b):
        t.forward(10+i)
        t.left(135)
        t.forward(11)
        
