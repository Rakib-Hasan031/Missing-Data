# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 00:43:39 2018

@author: Rakib Hasan
"""

#Data processing

#importing the libraries
import numpy as np  #numpy:it contains mathmatical tool & it needs to any mahmatical improve in our code 
import matplotlib.pyplot as plt  #matplotlib.pyplot:to plot something 
import pandas as pd  #pandas:To import data set & manage data set

#importing dataset
dataset = pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

#Find out missing Data
from sklearn.preprocessing import Imputer
imputer=Imputer (missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3]).values