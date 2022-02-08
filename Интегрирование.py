import matplotlib.pyplot as plt
import math as m

def Func1(x):
    f=1./(1+x**2)
    return f
#-1 1
def Func2(x):
    f=x**(1/3)*m.exp(m.sin(x))
    return f
#0 1
#trapeze
prec=8
disp1T=[0]*prec
disp2T=[0]*prec
disp1S=[0]*prec
disp2S=[0]*prec
for n in range(1,prec+1):
    s1t=0
    s2t=0
    s1s=0
    s2s=0
    k=2**n
    dx=1/k
    for i in range(0,k):
        s1t=s1t+(Func1(i*dx)+Func1((i+1)*dx))*dx/2
        s2t=s2t+(Func2(i*dx)+Func2((i+1)*dx))*dx/2
        s1s=s1s+(Func1(i*dx)+Func1((i+1)*dx)+4*Func1((i+0.5)*dx))*dx/6*2
        s2s=s2s+(Func2(i*dx)+Func2((i+1)*dx)+4*Func2((i+0.5)*dx))*dx/6
    disp1T[n-1]=s1t
    disp2T[n-1]=s2t
    disp1S[n-1]=s1s  
    disp2S[n-1]=s2s
    print(k,":", 2*s1t, s2t, s1s, s2s)
d1t=[0]*prec
d2t=[0]*prec
d1s=[0]*prec
d2s=[0]*prec
for n in range(1,prec):
    d1t[n-1]=m.log(abs(disp1T[prec-1]-disp1T[n-1]),2)
    d2t[n-1]=m.log(abs(disp2T[prec-1]-disp2T[n-1]),2)
    d1s[n-1]=m.log(abs(disp1S[prec-1]-disp1S[n-1]),2)
    d2s[n-1]=m.log(abs(disp2S[prec-1]-disp2S[n-1]),2)

for n in range(1,prec):
    plt.plot([n,n],[0,d1t[n-1]])
    plt.plot([n+0.1,n+0.1],[0,d1s[n-1]])
plt.plot([1,prec-1],[d1t[0],d1t[prec-2]])
plt.plot([1+0.1,prec-1+0.1],[d1s[0],d1s[prec-2]])
plt.show()
ang1t=(d1t[prec-2]-d1t[0])/(prec-2)
print("Trapeze 1 error decreases as 2^(",ang1t,"*n)")
ang1s=(d1s[prec-2]-d1s[0])/(prec-2)
print("Simpson 1 error decreases as 2^(",ang1s,"*n)")

for n in range(1,prec):
    plt.plot([n,n],[0,d2t[n-1]])
    plt.plot([n+0.1,n+0.1],[0,d2s[n-1]])
plt.plot([1,prec-1],[d2t[0],d2t[prec-2]])
plt.plot([1+0.1,prec-1+0.1],[d2s[0],d2s[prec-2]])
plt.show()
ang2t=(d2t[prec-2]-d2t[0])/(prec-2)
print("Trapeze 1 error decreases as 2^(",ang2t,"*n)")
ang2s=(d2s[prec-2]-d2s[0])/(prec-2)
print("Simpson 1 error decreases as 2^(",ang2s,"*n)")