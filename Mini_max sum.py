#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    select=arr[0]
    select1=arr[len(arr)-1]
    sum=0
    for i in range(0,len(arr)):
        sum=arr[i]+sum
    min=sum-select1
    max=sum-select
    print(min,max)
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
