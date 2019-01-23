#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def trapeze(t0,h,N,y0,f):

  t = np.linspace(t0,t0+N*h,N+1) 
  y = np.zeros((N+1))
  y[0] = y0

  for k in np.arange(N): 
    yy = y[k] + h*f(t[k],y[k]) #prédiction
    y[k+1] = y[k] + 0.5*h*(f(t[k],y[k])+f(t[k+1],yy)) #correction

  return [t,y]
