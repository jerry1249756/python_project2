from vpython import*
import numpy
import alphabet_plus_beta

Ey=0
Ez=0
d=60 #distance from board to screen
L=30 #size of the board
h=15 #distance between the board
e=1.6E-19 
m=9.11E-31
v_init=10
rt=1000  #rate

def get_field(pos_y,pos_z): #return the field(E_y,E_z) needed to project to (pos_y, pos_z)
    return 2*m*v_init**2*pos_y/(e*L*(L+2*d)), 2*m*v_init**2*pos_z/(e*L*(L+2*d))

def word_pos(x,y): #return the position of the character at (x,y)(x=0-9, y=0-2)
    return 6*x+1, 9*y+1

scene = canvas(width = 800, height = 600, forward=vec(-1.5,0,-1))
upboard = box(width=L,length=L, height=0.01, pos=vec(0,h/2,0), color=color.magenta)
downboard = box(width=L,length=L, height=0.01, pos=vec(0,-h/2,0), color=color.magenta)
screen = box(width=88, length=0.01, height=28, pos=vec(h/2+d,0,0), color=color.white, opacity=0.6)
projector = box(width=5,length=18,height=5, pos=vec(-d,0,0))

E_field = arrow(pos=vec(0,0,0), axis=vec(0,Ey,Ez), color=color.green, shaftwidth = 0.8, length=10)

#make 1500 balls
N=1500
balls=[]
for i in range (N):
    ball = sphere(radius=1, pos=vec(-d+1.5,0,0),v=vec(v_init,0,0), color=color.red)
    balls.append(ball)
count=0

t=0
dt=1/rt
alphabet_plus_beta.main()
for i in range (0,23):
    for j in range (0,87):
        if alphabet_plus_beta.screen[i][j]==1:
            while True:
                Ey,Ez=get_field(12-i,44-j) #yz plane :+-12*+-44 , revert(i-14,j-44) 
                t+=dt
                balls[count].pos.x+=balls[count].v.x*dt
                balls[count].pos.y+=balls[count].v.y*dt
                balls[count].pos.z+=balls[count].v.z*dt
                if(balls[count].pos.x>-L/2 and balls[count].pos.x<L/2):
                    balls[count].v.y+=Ey*e/m*dt
                    balls[count].v.z+=Ez*e/m*dt
                if(balls[count].pos.x>=h/2+d):
                    break
            count+=1

