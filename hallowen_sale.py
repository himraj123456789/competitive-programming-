#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(start, d, min1, last):
    n   = int(((min1-start)/-d)+1)
    if(start>last):
        return 0
    tn1 = start+(n-1)*-d
    sum1=((start+tn1)*n)/2
    if(sum1>last):
        return 1
    rem=last-sum1
    n1=int(rem/min1)
    return n1+n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
