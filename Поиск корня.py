import math as m

a=5
u=10
prec=0.00001
c=2*a**2*u

def Func(x):
    f=1/m.tan(m.sqrt(c*(1-x)))-m.sqrt(1/x-1)
    return f

def Fder(x):
    f=(1+1/(m.tan(m.sqrt(c*(1-x))))**2)*c/(2*m.sqrt(c*(1-x)))+1/(2*x**2*m.sqrt(1/x-1))
    return f

x=1-4*(m.pi)**2/c
if x<0:
    x=0
print(x)

i=0
l1=x+prec
l2=1-prec
f1=Func(l1)
f2=Func(l2)
while l2-l1>prec:
    i=i+1
    l3=(l1+l2)/2
    f3=Func(l3)
    if f1*f3<0:
        l2=l3
        f2=f3
    else:
        l1=l3
        f1=f3
    #print(l1, l2)
l1=-l1*u
l2=-l2*u
print("Dichotomy interval of energy: ", l1, l2,"//", i," steps")

i=0
z=x+prec
t=(x+1)/2
while abs(Func(t)-Func(z))>=prec:
    i=i+1
    z=t
    t=z-Func(z)/Fder(z)
    #print(t)
z=-z*u
t=-t*u
print("Newton's energy interval: ", z, t,"//", i," steps")

i=0
z=x+prec
t=(x+1)/2
while abs(Func(t)-Func(z))>=prec:
    i=i+1
    z=t
    der=(Func(z+prec)-Func(z))/(prec)
    t=z-Func(z)/der
    #print(t)
z=-z*u
t=-t*u
print("Iterations energy interval: ", z, t,"//", i," steps")