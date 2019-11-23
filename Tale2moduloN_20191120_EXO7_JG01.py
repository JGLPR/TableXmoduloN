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

speed("fastest")

n = 10
b = 0
r = 100

setup()  #Initialise la fenêtre 
print(heading())  #Affiche 0.0 : le crayon pointe vers le point bleu : Est

up()
goto(0,-r)
down()
color("red")
circle(r)

color("blue")

for i in range(n):
    up()
    goto(r*cos(2*i*pi/n),r*sin(2*i*pi/n))
    down()
    j = (b*i) % n
    goto(r*cos(2*j*pi/n),r*sin(2*j*pi/n))

exitonclick()

