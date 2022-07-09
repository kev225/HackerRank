'''
    Task:
    Calculate the hourglass sum for every hourglass in A,
    then print the maximum hourglass sum.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def find_big(a):
    biggest = float('-inf')
    for row in range(len(arr)-2):
        for col in range(len(arr[0])-2):
            glass = sum(arr[row][col:col+3]) + arr[row+1][col+1] + sum(arr[row+2][col:col+3])
            if glass > biggest:
                biggest = glass
    return biggest

if __name__ == '__main__':
    arr = []
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    a = find_big(arr)
    print(a)
                
