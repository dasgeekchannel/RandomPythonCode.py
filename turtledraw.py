#!/usr/bin/python
#Written by DasGeek
#Using Turtle to draw
import turtle
mertle = turtle.Turtle()
moves = 1
# while true loop
while True:
    mertle.shape('turtle')
    mertle.color('red') #color turtle red
    mertle.forward(100)
    mertle.left(90)
    moves = moves + 1
    if moves == 4:
        break;
# for in loop
for i in range (4):
    mertle.color('green') #color turtle green
    mertle.forward(100)
    mertle.left(90)
print(i)
