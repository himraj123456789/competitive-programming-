#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    x=s
    repeat=n
    t=repeat%len(x)
    t1=int(repeat/len(x))
    
    count=0
    count1=0
    for j in range(0,len(x)):
        if(x[j]=='a'):
            count1=count1+1
        else:
            pass
    
    for i in range(0,t):
        if(x[i]=='a'):
            count=count+1
        else:
            pass

    total=count1*t1+count
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
