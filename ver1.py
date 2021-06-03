from vpython import*
import numpy

Ey=0
Ez=0
d=100 #distance from board to screen
L=20 #size of the board
h=20 #distance between the board
e=1.6E-19 
m=9.11E-31
v_init=2
rt=1000  #rate

def get_field(pos_y,pos_z): #return the field(E_y,E_z) needed to project to (pos_y, pos_z)
    return 2*m*v_init**2*pos_y/(e*L*(L+2*d)), 2*m*v_init**2*pos_z/(e*L*(L+2*d))

def word_pos(x,y): #return the position of the character at (x,y)(x=0-9, y=0-2)
    return 6*x+1, 9*y+1

scene = canvas(width = 800, height = 600, forward=vec(1,0,-1))
upboard = box(width=L,length=L, height=0.01, pos=vec(0,h/2,0))
downboard = box(width=L,length=L, height=0.01, pos=vec(0,-h/2,0))
screen = box(width=61, length=0.01, height=28, pos=vec(h/2+d,0,0), color=color.white)
projector = box(width=3,length=5,height=3, pos=vec(-d,0,0))

E_field = arrow(pos=vec(0,0,0), axis=1000*vec(0,Ey,Ez), color=color.green)
ball = sphere(radius=1, pos=vec(-d+1.5,0,0),v=vec(v_init,0,0), color=color.red)

t=0
dt=1/rt
while True:
    Ey,Ez=get_field(-14,30) #yz plane :+-14*+-31
    t+=dt
    if(ball.pos.x<=h/2+d):
        ball.pos.x+=ball.v.x*dt
        ball.pos.y+=ball.v.y*dt
        ball.pos.z+=ball.v.z*dt
    if(ball.pos.x>-L/2 and ball.pos.x<L/2):
        ball.v.y+=Ey*e/m*dt
        ball.v.z+=Ez*e/m*dt

