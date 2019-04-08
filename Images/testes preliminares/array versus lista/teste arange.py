from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

dt = 0.1
t = arange(0,1,dt)
print t

w = arange(-len(t)/2 , len(t)/2, dt)
print w
