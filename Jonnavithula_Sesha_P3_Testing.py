#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:59:34 2023

@author: seshajonnavithula
"""

import numpy as np
import pandas as pd
import math as math
import matplotlib.pyplot as plt


filename = input("Filename of weights file: ")
file = open(filename, "r")
filename = input("Filename of test file: ")
testdf = pd.read_csv(filename)
w0 = file.readline()
w0 = w0.replace("[",'')
w0 = w0.replace("]",'')
w0 = float(w0)

w1 = file.readline()
w1 = w1.replace("[",'')
w1 = w1.replace("]",'')
w1 = float(w1.strip())
w1 = float(w1)

w2 = file.readline()
w2 = w2.replace("[",'')
w2 = w2.replace("]",'')
w2 = float(w2.strip())
w2 = float(w2)

w3 = file.readline()
w3 = w3.replace("[",'')
w3 = w3.replace("]",'')
w3 = float(w3.strip())
w3 = float(w3)

w4 = file.readline()
w4 = w4.replace("[",'')
w4 = w4.replace("]",'')
w4 = float(w4.strip())
w4 = float(w4)

def hwX(w,x):
    return 1/(1+np.exp(-np.dot(x,w)))

w = np.array([[w0],[w1],[w2],[w3],[w4]])

m = len(testdf.index)

x0 = np.ones((m))
x1 = testdf["Variance"]
x2 = testdf["Skewness"]
x3 = testdf["Curtosis"]
x4 = testdf["Entropy"]

x = np.array([x0,x1,x2,x3,x4]).T

yi = testdf["Genuine=1"].to_numpy()
y = (np.array([yi])).T

p = hwX(w,x)

tp = 0
tn = 0
fp = 0
fn = 0

for i in range(m):
    if p[i]<0.5 and y[i] == 0:
        tn = tn+1
    elif p[i]<0.5 and y[i] == 1:
        fn = fn+1
    elif p[i]>=0.5 and y[i] == 0:
        fp = fp+1
    elif p[i]>=0.5 and y[i] == 1:
        tp = tp+1
        
        
print("FP: " + str(fp))
print("FN: " + str(fn))
print("TP: " + str(tp))
print("TN: " + str(tn))
acc = (tp+tn)/(tp+tn+fp+fn)
prec = tp/(tp+fp)
rec = tp/(tp+fn)
f1 = 2*(1/((1/prec)+(1/rec)))


print("Accuracy: " + str(acc))
print("Precision: " + str(prec))
print("Recall: " + str(rec))
print("f1 Score: " + str(f1))
