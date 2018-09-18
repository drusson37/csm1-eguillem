#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


# Fonction f(t,y), second membre d'équations différentielles d'ordre 1
# écrite sous la forme d'un problème de Cauchy, y'(t) = f(t,y(t)) avec
# y(0)=y0

a = -1.
b = 1.



def f_affine(t,y):

    return a*y*y+b


def sol_affine(t,y0,t0):
 
    if y0<1:             
        c=np.log(np.abs((1+y0)/(1-y0)))-2*t0
        return (np.exp(2*t+c) -1) / (np.exp(2*t+c)+1) 
    if y0>1:            
        c=np.log((1+y0)/np.abs((1-y0)))-2*t0
        return (np.exp(2*t+c) -1) / (np.exp(2*t+c)+1) 

    if y0<-1:            
        c=np.log(np.abs((1+y0))/(1-y0))-2*t0
        return (np.exp(2*t+c) -1) / (np.exp(2*t+c)+1) 
    return 1
