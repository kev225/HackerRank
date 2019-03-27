'''
Task

Given the meal price (base cost of a meal), tip percent (the
percentage of the meal price being added as tip), and tax percent (the
percentage of the meal price being added as tax) for a meal, find and
print the meal's total cost.
'''


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal = round(meal_cost)
    tip = float(12 * (tip_percent/100))
    tax = float(12 * (tax_percent/100))
    totalCost = meal + tip + tax 
    print(round(totalCost))

    
if __name__ == '__main__':
   
    meal_cost = float(input())
       

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
