from turtle import *
from random import *

speed(50)
bgcolor("black")
for i in range(300):
    colormode(255)
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    fd(50+i)
    rt(91)
    pencolor(r,g,b)