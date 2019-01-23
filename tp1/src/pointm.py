#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def pointmilieu(t0,h,N,y0,f):


  t = np.linspace(t0,t0+N*h,N+1) 
  y = np.zeros((N+1))
  y[0] = y0
  y[1] = y[0] + h*f(t[0]+0.5*h,y[0]+0.5*h*f(t[0],y[0])) 

  for k in np.arange(1,N): 

    y[k+1] = y[k-1] + 2*h*f(t[k],y[k])

  return [t,y]

