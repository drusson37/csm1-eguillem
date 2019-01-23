#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def euler_explicite(t0,h,N, y0,f):
    """Méthode d'Euler pour la résolution d'un problème de Cauchy.

    Resolution de y'(t) = f(t,y(t)) avec y(t0) = y0 par la méthode d'Euler
    explicite avec un pas de temps h>0 et pour t = k*h, k=0..N.

    """

    # Construit un tableau des temps: t = t0 + [0,h,2h,...ih,...Nh]
    t = np.linspace(t0,t0+N*h,N+1) # N+1 temps de t0 à t0+N*h

    # Alloue un tableau de la taille de t, initialisé à 0. Il servira à
    # stocker la solution aux instants t0+i*h.
    y = 0.*t

    # Donnée initiale, la valeur [0] du tableau y
    y[0] = y0

    # On doit faire N itérations en temps
    for k in np.arange(N): # Boucle de 0 à N-1
        y[k+1] = y[k] + h*f(t[k],y[k]) # Formule de la méthode d'Euler

    return [t,y]


def RK(t0,h,N, y0,f):

    t = np.linspace(t0,t0+N*h,N+1)
    y = np.zeros((N+1))
    y[0] = y0

    for k in np.arange(N): 
        y[k+1] = y[k] + h*f(t[k]+0.5*h,y[k]+0.5*h*f(t[k],y[k]))

    return [t,y]

def pointmilieu(t0,h,N,y0,f):

    t = np.linspace(t0,t0+N*h,N+1) 
    y = np.zeros((N+1))
    y[0] = y0
    y[1] = y[0] + h*f(t[0]+0.5*h,y[0]+0.5*h*f(t[0],y[0])) 

    for k in np.arange(1,N): 

      y[k+1] = y[k-1] + 2*h*f(t[k],y[k])

    return [t,y]

def trapeze(t0,h,N,y0,f):

  t = np.linspace(t0,t0+N*h,N+1) 
  y = np.zeros((N+1))
  y[0] = y0

  for k in np.arange(N): 
    yy = y[k] + h*f(t[k],y[k]) #prédiction
    y[k+1] = y[k] + 0.5*h*(f(t[k],y[k])+f(t[k+1],yy)) #correction

  return [t,y]


