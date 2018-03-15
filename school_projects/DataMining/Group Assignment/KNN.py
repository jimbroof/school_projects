# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:08:46 2017

@author: ivanm
"""
from DataCleaning import Data 
import math
import operator


class calculations:  
    def calculate_distance(self, test, training):
        distance = 0
        
        if test['Developer'] != training['Developer']:
            distance = distance + 1
            
        if test['Publisher'] != training['Publisher']:
            distance = distance + 1
        
        if test['Platform'] != training['Platform']:
            distance = distance + 1
        
        if test['Rating'] != training['Rating']:
            distance = distance + 1
            
        distance = distance + math.sqrt(pow(test['Global_Sales'] - training['Global_Sales'], 2))
        
        return distance

training_set_percent = 0.66
k_nearest = 10

calc = calculations()

# Load all of the data
dataset = Data.get_data

training_set = []
test_set = []

for x in range(0, int(len(dataset) * training_set_percent)):
    training_set.append(dataset.iloc[x])

for y in range(int(len(dataset) * training_set_percent) + 1, len(dataset) - 1):
    test_set.append(dataset.iloc[y])
    
for z in test_set:
    neighbors = []
    
    for ypsilon in training_set:
        distance = calc.calculate_distance(z, ypsilon)
        neighbors.append((ypsilon, distance))
        
    neighbors.sort(key = operator.itemgetter(1))
    
    final_list = []
    
    for i in range(k_nearest):
        final_list.append(neighbors[i][0])

print(final_list)
