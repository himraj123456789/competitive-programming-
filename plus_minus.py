#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    
    arr.sort()
    pos=0
    neg=0
    zero=0
    for i in range(0,len(arr)):
        if(arr[i]>0):
            pos=pos+1
        if(arr[i]<0):
            neg=neg+1
        if(arr[i]==0):
            zero=zero+1
    division_pos = pos/(len(arr))
    division_neg = neg/(len(arr))
    division_zero = zero/(len(arr))
    print(round(division_pos,6))
    print(round(division_neg,6))
    print(round(division_zero,6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
