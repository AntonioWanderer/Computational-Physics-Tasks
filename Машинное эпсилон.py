import numpy as np
import math
i=0
e=1
while (1+e/2>1):
    e=e/2
    i=i+1
print("Machine epsilon = ", e, "\nbinary degree = -", i)

if 1+e+e/2>1+e:
    print("more")
else:
    print("equal")

i=1
m = [np.float32(1.0)]
while m[0]-1+m[0]<math.inf:
    m[0]=m[0]*2
    i=i+1
print("Max number=",m[0]*(2-e)," rzrd_max = ", i)

#because mantissa of e, e/2 is 0 and different degree
#but mantissa of e+e/2 is 10000... more than 0000... with same degree
