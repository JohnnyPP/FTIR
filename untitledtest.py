# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 17:28:39 2014

@author: klocek
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\klocek\.spyder2\.temp.py
"""
import numpy as np
import matplotlib.pyplot as plt
import pylab


def load_data(file_name, file_path):
   """
   Loads data from the EDX csv file
   :param file_name:
   :param file_path:
   :return: x_column, y_column raw data
   """

   file_name_and_path = file_path + file_name

   x_column, y_column = np.loadtxt(file_name_and_path, dtype=float, 
                                   delimiter=',', skiprows=0,
                                   usecols=(0, 1), unpack=True)
   return x_column, y_column

def file_name_without_extension(file_name):
   dot_position = file_name.find('.')
   return file_name[0:dot_position]

def image_name(file_name):
   return file_name_without_extension(file_name) + '.png'

###############################################################################


import os
file_path = 'D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data\\'
for name in os.listdir (file_path):
    if name.endswith ('.dpt'):
        print (name)
        
a=[name for name in os.listdir('D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data') if name.endswith ('.dpt')]
file_name = a[0]    

x, y = load_data(file_name, file_path)


fig= plt.figure (x, y)