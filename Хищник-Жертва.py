import math as m
import numpy as np
import matplotlib.pyplot as plt

a=10
b=2
c=2
d=10
#a/b
#d/c
def Dx(x,y):
    dx=a*x-b*x*y
    return(dx)

def Dy(x,y):
    dy=c*x*y-d*y
    return(dy)

prec=150
dt0=0.05

t=np.zeros(prec)
t1=np.zeros(prec)
x=np.zeros(prec)
x1=np.zeros(prec)
y=np.zeros(prec)
y1=np.zeros(prec)

l=20
for p in range(3,4):
    for q in range(3,4):
        t[0]=0
        t1[0]=0
        x[0]=p
        x1[0]=p
        y[0]=q
        y1[0]=q
        dx=0
        dx1=0
        dy=0
        dy1=0
        dt=dt0
        dt1=-dt0
        for i in range(1,prec):
            if (abs(x[i-1])>l) or (abs(y[i-1])>l):
                dt=0
            t[i]=t[i-1]+dt
            dx=dt*Dx(x[i-1]+dx/2,y[i-1]+dy/2)
            x[i]=x[i-1]+dx
            dy=dt*Dy(x[i-1]+dx/2,y[i-1]+dy/2)
            y[i]=y[i-1]+dy
            if (abs(x1[i-1])>l) or (abs(y1[i-1])>l):
                dt1=0
            t1[i]=t1[i-1]+dt1
            dx1=dt1*Dx(x1[i-1]+dx1/2,y1[i-1]+dy1/2)
            x1[i]=x1[i-1]+dx1
            dy1=dt1*Dy(x1[i-1]+dx1/2,y1[i-1]+dy1/2)
            y1[i]=y1[i-1]+dy1
        plt.plot(x,y)
        plt.plot(x1,y1)
plt.show()