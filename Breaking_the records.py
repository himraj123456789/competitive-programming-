#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high=scores[0]
    low=scores[0]
    hi=0
    li=0
    x=[]
    for i in range(0,len(scores)):
        if(high>scores[i]):
            high=scores[i]
            hi=hi+1
        if(low<scores[i]):
            low=scores[i]
            li=li+1
    x.append(li)
    x.append(hi)
    return x
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
