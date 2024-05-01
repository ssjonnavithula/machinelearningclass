#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:13:10 2023

@author: seshajonnavithula
"""
import json

filename = input("What is the path to the train file: ")

file = open(filename, "r", encoding = "unicode-escape")

line = file.readline()

spamcount = 0
hamcount = 0
counted = dict()

#cleans up text
def cleantext(line):
    line= line.lower()
    line= line.strip()
    
    for letter in line:
        if letter in """[]!.,"-!—@;':#$%^&*()+/?""":
            line = line.replace(letter,'')
    return line

#adds count of occurences in spam or ham of each word to dict
def countwords(words,counted,spam):
    for word in words:
        if word in counted:
            if spam == 1:
                counted[word][1] += 1
            else:
                counted[word][0] += 1
        else:
            if spam == 1:
                counted[word] = [0,1]
            else:
                counted[word] = [1,0]
    return counted

#calculates percentage of existence in spam or ham for each word and adds to dict
def make_percent_list(k,counted, spamcount, hamcount):
    for key in counted:
        counted[key][0] = (counted[key][0]+k)/(2*k+hamcount)
        counted[key][1] = (counted[key][1]+k)/(2*k+spamcount)
        
    return counted

#goes through all lines of file and appends to dict in to get total occurences dict for all words
while line != "":
    spam = int(line[:1])
    if spam == 1:
        spamcount +=1
    else:
        hamcount +=1
        
    line = cleantext(line[1:])
    words = set(line.split())
    
    counted = countwords(words,counted,spam)
    
    line = file.readline()
    

#print(counted)

#applies percentage function to dict to get percentage of existence
counted = make_percent_list(1,counted,spamcount,hamcount)
#print(counted)


stopfile = open("Data/StopWords.txt", "r")

stop = stopfile.read()

stop = stop.split("\n")

for word in stop:
    if word in counted:
        del counted[word]

file.close()
stopfile.close()
print(counted)
#write dict to a text file using json
with open('P4Dictionary.txt', 'w') as convert_file:
     convert_file.write(json.dumps(counted))
convert_file.close()

#write hamcount and spamcount to a text file
with open('P4HSCount.txt', 'w') as myfile:
     mystring = str(hamcount) + " " + str(spamcount)
     myfile.write(mystring)
myfile.close()

    

