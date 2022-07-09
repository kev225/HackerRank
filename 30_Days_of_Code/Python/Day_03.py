'''
Task

Given an integer, n, perform the following conditional actions:

- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5, print Not Weird
- If n is even and in the inclusive range of 6 to 20, print Weird
- If n is even and greater than 20, print Not Weird

Complete the stub code provided in your editor to print whether or not n is weird.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def weird(N):
    if N  % 2 == 0:
        if 2 <= N <= 5:
            return 'Not Weird'
        elif 6 <= N <= 20:
            return 'Weird'
        elif N > 20:
            return 'Not Weird'
    return 'Weird'
    

if __name__ == '__main__':
    N = int(input())
    w = weird(N)
    print(w)
