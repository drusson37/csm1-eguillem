#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def RK(t0,h,N, y0,f):
    """Méthode de Runge Kutta """

    t = np.linspace(t0,t0+N*h,N+1)
    y = np.zeros((N+1))
    y[0] = y0

    for k in np.arange(N): 
        y[k+1] = y[k] + h*f(t[k]+0.5*h,y[k]+0.5*h*f(t[k],y[k]))

    return [t,y]
