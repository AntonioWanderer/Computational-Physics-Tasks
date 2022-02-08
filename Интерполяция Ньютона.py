import math as m
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y=m.log(x)
    return y

def dat1(n,a,b):
    z=np.zeros(n)
    x=np.zeros(n)
    dx=(b-a)/(n-1)
    for i in range(0,n):
        x[i]=a+dx*i
        z[i]=func(x[i])
    return dx, x, z

def datZ(x,n,a,dx,num):
    s=0
    q=(x-a)/dx
    for i in range(0,n):
        s=s+num[i]*q**i
    return s

###########################################
n=15
a=1
b=10
(dx,x,y)=dat1(n,a,b)
plt.scatter(x,y)

num=np.zeros(n+2)
num[0]=y[0]
for i in range(1,n):
    f=1
    for j in range(1,n):
        y[n-j]=y[n-j]-y[n-j-1]
    dy=y[i]
    kk=np.zeros(n+2)
    kk[0]=1
    l=1
    for j in range(0,i):
        f=f*(j+1)
        for k in range(0,l+1):
            kk[l-k+1]=kk[l-k]
        kk[0]=0
        print(kk)
        for k in range(0,l+1):
            kk[k]=kk[k]-j*kk[k+1]
        l=l+1
        print(kk)
    print("________")
    num=num+kk*dy/f

print(num)

y0=np.zeros(n)
for i in range(0,n):
    y0[i]=datZ(x[i],n,a,dx,num)

plt.plot(x,y0)
print(y0)
plt.show()

prec=100
x1=np.zeros(prec)
yi=np.zeros(prec)
yr=np.zeros(prec)
dx1=(b-a)/(prec-1)
print(dx)
for i in range(0,prec):
    x1[i]=a+dx1*i
    yi[i]=datZ(x1[i],n,a,dx,num)
    yr[i]=func(x1[i])
plt.plot(x1,yi)
plt.plot(x1,yr)
plt.show()

plt.plot(x1,yr-yi)
plt.show()