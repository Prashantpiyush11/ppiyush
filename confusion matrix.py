# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2  2018

@author: Sreenivas.J
"""
#Classification accuracy can hide the detail you need to diagnose the performance of your model. 
#But we can tease apart this detail by using a confusion matrix.

# Example of a confusion matrix in Python
from sklearn.metrics import confusion_matrix
#Binomial classification
expected =  [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
predicted = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
results = confusion_matrix(expected, predicted)
print(results)

#Multinomial classification
expected =  ['C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3']
predicted = ['C1', 'C1', 'C3', 'C1', 'C3', 'C2', 'C1', 'C1', 'C3']

results = confusion_matrix(expected, predicted)
print(results)
#Accuracy = ((True +Ve) + (True -Ve))/Total no. of records
