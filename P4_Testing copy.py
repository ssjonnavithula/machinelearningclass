#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:35:57 2023

@author: seshajonnavithula
"""
import json
import numpy as np
with open("P4Dictionary.txt") as dictfile:
     counted = json.loads(dictfile.read())

dictfile.close()
     
with open("P4HSCount.txt", "r") as dictfile:
     
     line = dictfile.read().split()
     hamcount  = int(line[0])
     spamcount = int(line[1])

def cleantext(line):
    line= line.lower()
    line= line.strip()
    
    for letter in line:
        if letter in """[]!.,"-!—@;':#$%^&*()+/?""":
            line = line.replace(letter,'')
    return line

def calculation(test):
    hamspam = int(test[0:1])
    test = test[1:]
    test = cleantext(test)
    
    test = test.split()
    
    test = set(test)
    
    condhamprob = 1
    condspamprob = 1
    for word in counted:
        if word in test:
            condhamprob += np.log(counted[word][0])
            condspamprob += np.log(counted[word][1])
        else:
            condhamprob += np.log((1-counted[word][0]))
            condspamprob += np.log((1-counted[word][1]))
            
    condhamprob = np.e ** condhamprob
    condspamprob = np.e ** condspamprob
    
    spam = condspamprob * probspam
    
    ham = condhamprob * probnotspam
    
    spam1 = spam/(spam+ham)
    
    
    return spam1, hamspam

filename = input("What is the path to the test file: ")

myfile = open(filename, "r", encoding = "unicode-escape")
probspam = spamcount/(spamcount+hamcount)
probnotspam = 1-probspam

tp = 0
tn = 0
fp = 0
fn = 0

test = myfile.readline()
while test != '':
    
    spam1, hamspam = calculation(test)

    if spam1 >= 0.5:
        prediction = 1
    elif spam1 < 0.5:
        prediction = 0
    
    if prediction == hamspam:
        if prediction == 1:
            tp = tp+1
        elif prediction == 0:
            tn = tn+1
    else:
        if prediction == 1:
            fp = fp+1
        elif prediction == 0:
            fn = fn+1
            
    test = myfile.readline()

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
    

