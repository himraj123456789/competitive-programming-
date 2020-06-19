#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    arr.sort()
    i=0
    j=1
    sum1=0
    res=0
    while(j!=len(arr)):
    
        if(arr[i]==arr[j]):
            sum1=sum1+1
        
            j=j+1
        else:
            i=i+1
            j=j+1
        if(sum1>res):
            res=sum1
    return len(arr)-(res+1)
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
