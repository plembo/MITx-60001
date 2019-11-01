#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:44:32 2019
@author: Phil Lembo

Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""
import numpy as np

x = int(input('Enter number for x: '))
y = int(input('Enter number for y: '))
print('x**y = {}'.format(x**y))
print('log(x) = {}'.format(np.log(x)))
