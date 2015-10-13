__author__ = 'Alex'

from math import pi

diam = 45, 338, 19
square1 = pi*((diam[0]/2)**2)
square2 = pi*((diam[1]/2)**2)
square3 = pi*((diam[2]/2)**2)
res = (square1 + square2) - square3
print(res)

