# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:48:17 2019

@author: jean grondin


"""
from math import *
from turtle import *

def table2moduloN(n):
    X=[]
    Y=[]
    for i in range(n):
        X.append(cos(2*i*pi/n))
        Y.append(sin(2*i*pi/n))
        # print("( ",X[i]," ; ",Y[i]," )")
        print(X,Y)
    #return(X,Y)

table2moduloN(10)
"""

for i in range(n):
    color("blue")
    forward(256)
    left(120)
    for i in range(1,3,5):
        color("red")
        forward(128)
        left(120)

exitonclick()

"""   

