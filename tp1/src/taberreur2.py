#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import methodes
import equations2

from pylab import *

#nous avons copié collé des bouts de programme, en changeant le pas à chaque fois, puis nous avons affiché chaque pas et l'erreur associée par un print

t0,y0 = 0.,2.
T = 1.

N,h1 = 50,0.2
[t,y1] = methodes.euler_explicite(t0,h1,N,y0,equations2.f_affine)
# Solution exacte aux mêmes instants
z1 = equations2.sol_affine(t,y0,t0)
# Calcul de l'erreur maximum relative
e1 = np.max(np.abs((z1[1:]-y1[1:])/z1[1:]))


N,h2 = 50,0.1
[t,y1] = methodes.euler_explicite(t0,h2,N,y0,equations2.f_affine)
# Solution exacte aux mêmes instants
z1 = equations2.sol_affine(t,y0,t0)
# Calcul de l'erreur maximum relative
e2 = np.max(np.abs((z1[1:]-y1[1:])/z1[1:]))

N,h3 = 50,0.05
[t,y1] = methodes.euler_explicite(t0,h3,N,y0,equations2.f_affine)
# Solution exacte aux mêmes instants
z1 = equations2.sol_affine(t,y0,t0)
# Calcul de l'erreur maximum relative
e3 = np.max(np.abs((z1[1:]-y1[1:])/z1[1:]))

N,h4 = 50,0.025
[t,y1] = methodes.euler_explicite(t0,h4,N,y0,equations2.f_affine)
# Solution exacte aux mêmes instants
z1 = equations2.sol_affine(t,y0,t0)
# Calcul de l'erreur maximum relative
e4= np.max(np.abs((z1[1:]-y1[1:])/z1[1:]))

N,h5 = 50,0.0125
[t,y1] = methodes.euler_explicite(t0,h5,N,y0,equations2.f_affine)
# Solution exacte aux mêmes instants
z1 = equations2.sol_affine(t,y0,t0)
# Calcul de l'erreur maximum relative
e5 = np.max(np.abs((z1[1:]-y1[1:])/z1[1:]))

N,h6 = 50,0.00625
[t,y1] = methodes.euler_explicite(t0,h6,N,y0,equations2.f_affine)
# Solution exacte aux mêmes instants
z1 = equations2.sol_affine(t,y0,t0)
# Calcul de l'erreur maximum relative
e6 = np.max(np.abs((z1[1:]-y1[1:])/z1[1:]))


# Écriture de l'erreur en fonction de h

print("{0} | {1}\n".format(h1,e1))
print("{0} | {1}\n".format(h2,e2))
print("{0} | {1}\n".format(h3,e3))
print("{0} | {1}\n".format(h4,e4))
print("{0} | {1}\n".format(h5,e5))
print("{0} | {1}\n".format(h6,e6))


#Graphe de l'erreur en fonction de h 

plt.xscale('log') 
plt.yscale('log')     

y = np.array([e1, e2, e3, e4,e5,e6])
x = np.array([h1, h2, h3, h4,h5,h6])
title ("Graph de l'erreur en fonction de h ")
xlabel("erreur")
ylabel("pas h")
plt.plot(x, y,"b:o")

plt.show() # affiche la figure a l'ecran
