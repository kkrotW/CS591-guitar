#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:21:28 2017

@author: root
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:49:59 2016

@author: JINRAN TIAN
         WENYU WANG
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi
from math import*
from threading import Thread
import time
from cs591Utilities import *

n = readWaveFile("BluesGuitar.wav")
#Make the repeat part  
def chorus(n):
    m = []
    for i in range(len(n)):
        m.append(0.8*n[i])     
    return m
    displaySignal(n)
    time.sleep(0.2)
    displaySignal(m)

for i in range(len(n)):
    t = Thread(target = chorus, args = ([],))
    t.start()
    
def distortion(A):
    
    B=[]
    B+=[x/MAX_AMP for x in A]
    for i in range(len(A)):
        if A[i] > 0:
            B[i] = (1 - np.exp(-B[i]))*MAX_AMP
        else:
            B[i] = (-1 + np.exp(B[i]))*MAX_AMP
    
    return B

def clipdistortion(A,X):
    """clip distrotion where all signals cant to go pass a certain threshold X(relative)."""
    X = X * MAX_AMP
    B=[]
    B += [x for x in A]
    for i in range(len(A)):
        if B[i] > 0:
            B[i] = min(B[i],X)
        else:
            B[i] = max(B[i],(-X))
    return B

def simpledistortion(A,X):
    """Simple distortion that cuts off every peaks to the value X away both sides from the peak."""
    B=[]
    B += [x for x in A]

    for i in range(X,len(A)-X):
        if (A[i] > 0) and (A[i] > A[i-1]) and (A[i] > A[i+1]):
            B[i-X:i+X+1]=[A[i-X]]*(2*X+1)

        elif (A[i] < 0) and (A[i] < A[i-1]) and (A[i] < A[i+1]):

            B[i-X:i+X+1]=[A[i-X]]*(2*X+1)
    return B

