#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 08:45:16 2023

@author: seshajonnavithula
"""

import numpy as np
import pandas as pd
import math as math
import matplotlib.pyplot as plt

### change to input
filename = input("filename: ")
traindf = pd.read_csv(filename)
x = traindf.drop(columns = "Genuine=1")
x = x.drop(columns = "Unnamed: 0")
y = (traindf["Genuine=1"]).to_numpy()


w0 = 0
w1 = 0
w2 = 0
w3 = 0
w4 = 0
a = 0.23
m = len(x)
iterations = 900
x0 = np.ones(m)
x1 = traindf["Variance"]
x2 = traindf["Skewness"]
x3 = traindf["Curtosis"]
x4 = traindf["Entropy"]

x = np.array([x0,x1,x2,x3,x4]).T

y = np.array([y]).T

w = np.array([[w0],[w1],[w2],[w3],[w4]])

O = np.ones((1,m))

'''
print("w")
print(w)


print("O")
print(O)

print("x")
print(x)


print("y")
print(y)
'''


def H(x, w):
    a = 1 + (math.e)**(-np.dot(x,w))
    return 1/a

def J(y, h, m, ones):
    cost = -(y*np.log(h)) - ((1-y)*np.log(1-h))
    j = (1/m) * np.dot(ones, cost)
    return j

def W(w, alpha, m, h, y, x):
    return w -((alpha/m)*np.dot((h-y).T,x)).T

h = H(x,w)
j = J(y,h,m,O)


for i in range(iterations):
    
    h = H(x,w)
    j = J(y,h,m,O)
    w = W(w,a,m,h,y,x)
    jterm = J(y,h,m,O)
    
    plt.scatter(i, jterm)
    plt.xlabel("Number of iterations")
    plt.ylabel("Error (J)")

#print(iterations, "iterations produced: w0 = ", w[0][0], "w1 =", w[1][0], "w2 = ", w[2][0], "J=", jterm[0][0])

file = open("weights.txt", "w")
file.write(str(w[0])+ "\n")
file.write(str(w[1])+ "\n")
file.write(str(w[2])+ "\n")
file.write(str(w[3])+ "\n")
file.write(str(w[4])+ "\n")
file.close()

    