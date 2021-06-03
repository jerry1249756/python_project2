from vpython import*
import numpy

Ex=1
Ey=2
d=5 #distance from board to screen
L=4 #size of the board
h=5 #distance between the board
v_init=5

scene = canvas(width = 800, height = 600)
upboard = box(width=L,length=L, height=0.01, pos=vec(0,h/2,0))
downboard = box(width=L,length=L, height=0.01, pos=vec(0,-h/2,0))
screen = box(width=L, length=0.01, height=L, pos=vec(h/2+d,0,0), color=color.white)

