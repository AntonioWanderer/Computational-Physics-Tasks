import math as m
import numpy as np
import matplotlib.pyplot as plt

def fx(t,x):
    f=-x
    return f

plt.yscale('log')
plt.xscale('log')

e=100
t0=np.zeros(e)
d0=np.zeros(e)
d1=np.zeros(e)
d2=np.zeros(e)
et0=np.zeros(e)
et1=np.zeros(e)
et2=np.zeros(e)

for num in range(0,e):
    prec=5+num
    t0[num]=prec
    et0[num]=1/prec
    et1[num]=1/prec**2
    et2[num]=1/prec**4
    x=np.zeros(prec)
    t=np.zeros(prec)
    t[0]=0
    x[0]=1
    dt=3/prec
    for i in range(1,prec):
        dx=fx(t[i-1],x[i-1])*dt
        t[i]=i*dt
        x[i]=x[i-1]+dx
    #plt.plot(t,x)

    x1=np.zeros(prec)
    x1[0]=1
    for i in range(1,prec):
        dx=dt*fx(0,x1[i-1]+dx/2)
        x1[i]=x1[i-1]+dx
    #plt.plot(t,x1)

    x2=np.zeros(prec)
    x2[0]=1
    for i in range(1,prec):
        k1=dt/2*fx(t[i-1],x2[i-1])
        k2=dt/2*fx(t[i-1]+dt/2,x2[i-1]+k1)
        k3=dt*fx(t[i-1]+dt/2,x2[i-1]+k2)
        k4=dt*fx(t[i-1]+dt,x2[i-1]+k3)
        x2[i]=x2[i-1]+1/3*(k1+2*k2+k3+k4/2)
    
    #plt.plot(t,x2)

    x0=np.zeros(prec)
    x0[0]=1
    for i in range(1,prec):
        x0[i]=m.exp(-dt*i)
    #plt.plot(t,x0)
    #plt.show()

    for i in range(0,prec):
        if abs(x0[i]-x[i])>d0[num]:
            d0[num]=abs(x0[i]-x[i])
        if abs(x0[i]-x1[i])>d1[num]:
            d1[num]=abs(x0[i]-x1[i])
        if abs(x0[i]-x2[i])>d2[num]:
            d2[num]=abs(x0[i]-x2[i])
            print(num, d2[num])
plt.plot(t0,d0)
plt.plot(t0,d1)
plt.plot(t0,d2)
plt.plot(t0,et0)
plt.plot(t0,et1)
plt.plot(t0,et2)
plt.show()

plt.plot(t0,abs(d0/et0))
plt.plot(t0,abs(d1/et1))
plt.plot(t0,abs(d2/et2))

plt.show()