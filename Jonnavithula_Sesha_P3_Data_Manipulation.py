#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:41:29 2023

@author: seshajonnavithula
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df100 = pd.read_csv("banknote_data.csv")



train = df100.sample(frac = 0.8,random_state=7)
test = df100.drop(train.index)


train.to_csv("banknote_train.csv")
test.to_csv("banknote_test.csv")
