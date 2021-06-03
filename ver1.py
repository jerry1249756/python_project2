from vpython import*
import numpy

Ex=0.003
Ey=0.006
d=5 #distance from board to screen
L=4 #size of the board
h=3 #distance between the board
v_init=0.05
rt=1000  #rate

scene = canvas(width = 800, height = 600)
upboard = box(width=L,length=L, height=0.01, pos=vec(0,h/2,0))
downboard = box(width=L,length=L, height=0.01, pos=vec(0,-h/2,0))
screen = box(width=L, length=0.01, height=L, pos=vec(h/2+d,0,0), color=color.white)
projector = box(width=0.4,length=3,height=0.4, pos=vec(-d,0,0))


ball = sphere(radius=0.2, pos=vec(-d+1.5,0,0),v=vec(v_init,0,0))

t=0
dt=1/rt
while True:
    t+=dt
    ball.pos.y+=ball.v.y*dt
    ball.pos.x+=ball.v.x*dt
    if(ball.pos.x>-L/2 and ball.pos.x<L/2):
        ball.v.y+=Ey/10*dt
        ball.v.x+=Ex/10*dt

