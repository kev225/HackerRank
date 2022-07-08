'''
Task

Given a base-10 integer, n, convert it to binary (base-2). Then
find and print the base- integer denoting the maximum number of
consecutive 1's in n's binary representation.
'''


#!/bin/python3

import math
import os
import random
import re
import sys


def binary(n):
    b = bin(n)
    b = b[2:]
   
    longest = 0
    new  = 0
    for i in range(len(b)):   
        if b[i] == '1':
            new += 1 
            if new > longest:
                longest = new
        else:
            new = 0
    return longest

if __name__ == '__main__':
    n = int(input())
    print(binary(n))
    
