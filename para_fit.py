import numpy as np
import scipy as sp
import pylab as pl
from scipy.optimize import leastsq as lq

def para(x,p0,p1,p2):
    return (p0/(x-p1))+p2

def error(p,y,x):
    return y-para(x,p[0],p[1],p[2])

x=[]
y=[]

with open('/home/renxiong/Magfit/test1.txt','r') as f0:
    for i in f0:
        tmp=i.split()
        x.append(float(tmp[1]))
        y.append(float(tmp[2]))
        
p=[0,0,0]
result=lq(error,p,args=(y,x))

print "fitting data",result[0][0],result[0][1],result[0][2]


x_result=np.linspace(0,300,300)           
y_result=para(x_result,result[0][0],result[0][1],result[0][2])
pl.plot(x,y,'ro',label='sample point')
pl.plot(x_result,y_result,label='fit model y=%s')
pl.xlabel('Temperature(K)')
pl.ylabel('Susceptibility')
pl.legend()
pl.show()
