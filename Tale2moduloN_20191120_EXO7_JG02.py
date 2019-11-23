# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:33:24 2019

@author: Arnaud Bodin
@adaptation : jean grondin
##############################
# Python au lycée (vol.1) - Tortue
# Activité 5 - Table de multiplications
##############################

"""

from turtle import *
from math import *

# speed("fastest")
# speed("normal")
setup()  #Initialise la fenêtre
# print(heading())  #Affiche 0.0 : le crayon pointe vers le point bleu : Est    
colormode(255)
    
# n = 10
# b = 0
# r = 100

phi = (1+sqrt(5))/2

def tableBModulo(n,b,r):
    
    speed("fastest")
    up()
    goto(0,-r)
    down()
    pencolor(255,0,0)
    circle(r)
    
    pencolor(0,0,0)
    # speed("normal")
    speed("fastest")
    for i in range(n):
        cr = abs(floor(255*cos(2*i*pi/n)))
        cv = abs(floor(255*sin(2*i*pi/n)))
        # cb = floor(255*i/n)
        cb = abs(floor(255*(cos(2*i*pi/n)+sin(2*i*pi/n))/2))
        up()
        goto(r*cos(2*i*pi/n),r*sin(2*i*pi/n))
        down()
        pencolor(cr,cv,cb)
        j = (b*i) % n
        goto(r*cos(2*j*pi/n),r*sin(2*j*pi/n))
        
    # exitonclick()
for i in range(10) :
    # tableBModulo(200,i*phi,200)
    tableBModulo(200,i,200)
    clear()

exitonclick()
