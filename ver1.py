from vpython import*
import numpy

Ey=0.003
Ez=0.006
d=5 #distance from board to screen
L=4 #size of the board
h=3 #distance between the board
q=1.6E-19 
m=9.11E-31
v_init=0.05
rt=1000  #rate

def get_field(pos):
    return 2*m*v^2*pos/(e*L*(L+2*d))

scene = canvas(width = 800, height = 600)
upboard = box(width=L,length=L, height=0.01, pos=vec(0,h/2,0))
downboard = box(width=L,length=L, height=0.01, pos=vec(0,-h/2,0))
screen = box(width=L, length=0.01, height=L, pos=vec(h/2+d,0,0), color=color.white)
projector = box(width=0.4,length=3,height=0.4, pos=vec(-d,0,0))

E_field = arrow(pos=vec(0,0,0), axis=500*vec(0,Ey,Ez), color=color.green)
ball = sphere(radius=0.2, pos=vec(-d+1.5,0,0),v=vec(v_init,0,0))



t=0
dt=1/rt
while True:
    t+=dt
    if(ball.pos.x<h/2+d):
        ball.pos.x+=ball.v.x*dt
        ball.pos.y+=ball.v.y*dt
        ball.pos.z+=ball.v.z*dt
    if(ball.pos.x>-L/2 and ball.pos.x<L/2):
        ball.v.y+=Ey/10*dt
        ball.v.z+=Ez/10*dt

