#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math as math
import matplotlib.pyplot as plt
import random


#reads in data files
traindf = pd.read_csv("DataToCluster.csv")

#uses centroid text file to read in k value, initial centroid coords into nested array
k = 2


centroid = np.empty([2,2])

centroid[0][0] = random.randint(66,78)
centroid[0][1] = random.randint(167,267)


centroid[1][0] = random.randint(66,78)
centroid[1][1] =random.randint(167,267)

print("initial centroid: ")
print(centroid)
#extracts x1,x2 arrays from dataframe
x1 = (traindf["x1"]).to_numpy()
x2= (traindf["x2"]).to_numpy()

#initializes arrays for holding closest centroid (1 or 2) and corresponding coords for that centroid
centroidlabel = np.zeros(len(x1))
centroidlabelcoords = np.array([0,0])
centroidlabelcoords = np.empty([len(x1),2])

#defines initial centroid plot values
centroid1 = plt.scatter(centroid[0][0],centroid[0][1],marker = "x", color = "Red")
centroid2 = plt.scatter(centroid[1][0],centroid[1][1],marker = "x", color = "Blue")

#Determines number of iterations algorithm runs for
iterations = 5

#plots initial centroid values
def plotcentroid(centroid,centroid1, centroid2):
    centroid1.remove()
    centroid2.remove()
    centroid1 = plt.scatter(centroid[0][0],centroid[0][1],marker = "x", color = "Red")
    centroid2 = plt.scatter(centroid[1][0],centroid[1][1],marker = "x", color = "Blue")
    return centroid1,centroid2
#plots the points color-coded based on closest centroid
#assigns
def distcalc(centroid,x1,x2,centroidlabel, centroidlabelcoords,centroid1, centroid2):
    centroid1,centroid2 = plotcentroid(centroid,centroid1, centroid2)
    for i in range(0,len(x1)):
        distcent1x1 = (x1[i]-centroid[0][0])**2
        distcent1x2 = (x2[i]-centroid[0][1])**2
        distcent1 = (distcent1x1+distcent1x2)**0.5
    
        distcent2x1 = (x1[i]-centroid[1][0])**2
        distcent2x2 = (x2[i]-centroid[1][1])**2
        distcent2 = (distcent2x1+distcent2x2)**0.5
        
        if distcent1>distcent2:
            centroidlabel[i] = 2
            centroidlabelcoords[i][0], centroidlabelcoords[i][1] = centroid[1][0],centroid[1][1]
            plt.scatter(x1[i],x2[i],marker = "o", color = "Blue")
        
        elif distcent1<distcent2:
            centroidlabel[i] = 1
            centroidlabelcoords[i][0], centroidlabelcoords[i][1] = centroid[0][0],centroid[0][1]
            plt.scatter(x1[i],x2[i],marker = "o", color = "Red")
    return centroid1,centroid2,centroidlabel
        
def redefineCentroids(centroid,centroidlabel,centroidlabelcoords,x1,x2,centroid1, centroid2):
    sum1x1 = 0
    sum1x2 = 0
    sum2x1 = 0
    sum2x2 = 0
    count1 = 0
    count2 = 0
    
    for i in range(0,len(centroidlabel)):
        if centroidlabel[i] == 1:
            sum1x1 = sum1x1+ x1[i]
            sum1x2 = sum1x2+ x2[i]
            count1 += 1
        elif centroidlabel[i] == 2:
            sum2x1 = sum2x1+ x1[i]
            sum2x2 = sum2x2+ x2[i]
            count2 += 1
    
    centroid[0][0] = (sum1x1/count1)
    centroid[0][1] = (sum1x2/count1)
    centroid[1][0] = (sum2x1/count2)
    centroid[1][1] = (sum2x2/count2)
    
    centroid1,centroid2 = plotcentroid(centroid,centroid1, centroid2)
    return centroid, centroid1,centroid2

def Jterm(centroid,x1,x2,centroidlabel,centroidlabelcoords):
    mysum = 0
    for i in range (0,len(x1)):
        if centroidlabel[i] == 1:
            distx1 = (x1[i]-centroidlabelcoords[i][0])**2
            distx2 = (x2[i]-centroidlabelcoords[i][1])**2
            dist = (distx1+distx2)
            mysum += (dist**2)**0.5
        elif centroidlabel[i] == 2:
            distx1 = (x1[i]-centroidlabelcoords[i][0])**2
            distx2 = (x2[i]-centroidlabelcoords[i][1])**2
            dist = (distx1+distx2)
            mysum += (dist**2)**0.5
    return (1/len(x1))*mysum
        

prev = -1
J = 0
while J!= prev:
    prev = J
    centroid1,centroid2,centroidlabel = distcalc(centroid,x1,x2,centroidlabel, centroidlabelcoords,centroid1, centroid2)
    J = Jterm(centroid,x1,x2,centroidlabel,centroidlabelcoords)
    centroid,centroid1,centroid2 = redefineCentroids(centroid,centroidlabel,centroidlabelcoords,x1,x2,centroid1, centroid2)
    print(J)
    print(centroid)
    
    
    

'''
for i in range (0,iterations):
    centroid1, centroid2 = redefineCentroids(centroid,centroidlabel,centroidlabelcoords,x1,x2,centroid1, centroid2)
    centroid1, centroid2 = distcalc(centroid,x1,x2,centroidlabel, centroidlabelcoords,centroid1, centroid2)
    print(Jterm(centroid,x1,x2,centroidlabel,centroidlabelcoords))
'''