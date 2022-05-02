from tkinter import CENTER
from turtle import *

speed(10)
color("green")
bgcolor("black")
b = 200
pos = (5,5)

while b > 0:
    left(b)
    forward(b *3)
    b = b -1

done()