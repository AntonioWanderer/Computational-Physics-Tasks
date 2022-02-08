import math as m
import numpy as np
import matplotlib.pyplot as plt

def Gen(n):
    val=np.zeros(n+1)
    x=np.zeros(n+1)
    for k in range(0,n+1):
        x[k]=1+k/n
        val[k]=m.log(x[k])
    return x, val
    
    
def Mon(n,k):
    (x,y)=Gen(n)
    pol=np.zeros(n+2)
    pol[0]=1
    l=1
    z=1
    for i in range(0,n+1):
        if i!=k:
            z=z*(x[k]-x[i])
    for i in range(0,n+1):
        if i!=k:
            for j in range(0,l+1):
                pol[l-j+1]=pol[l-j]
            pol[0]=0
            for j in range(0,l+1):
                pol[j]=pol[j]-x[i]*pol[j+1]
            l=l+1
    for i in range(0,l+1):
        pol[i]=pol[i]/z
    return pol
    
def Lag(n):
    (x,y)=Gen(n)
    p=np.zeros(n+2)
    for k in range(0,n+1):
        p=p+y[k]*Mon(n,k)
    return(p)

def NumLag(n, x0):
    p=Lag(n)
    s=0
    for i in range (0,n+2):
        s=s+x0**i*p[i]
    return(s)

#############################
prec=100
for n in range (4,17):
    (x,y)=Gen(n)
    y1=np.zeros(n+1)
    p=Lag(n)
    for i in range(0,n+1):
        y1[i]=NumLag(n,x[i])
        #plt.scatter(x[i],y[i])

    arg=np.zeros(prec)
    f=np.zeros(prec)
    s=np.zeros(prec)
    diff=np.zeros(prec)
    for i in range(0,prec):
        arg[i]=1+i/prec
        f[i]=m.log(arg[i])
        for j in range (0,n+2):
            s[i]=s[i]+arg[i]**j*p[j]
        diff[i]=s[i]-f[i]
    plt.plot(arg,diff)
    plt.show()
#plt.plot(arg,f)
#plt.plot(arg,s)
#plt.show()