#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    i=0
    step=0
    while(i!=len(c)-1):
        if(len(c)==2):
            step=step+1
            break
        if(c[i+1]==0):
            if(c[i+2]==0):
                i=i+2
                step=step+1
                if(i==len(c)-2):
                    step=step+1
                    break
               
            else:
                i=i+1
                step=step+1
                if(i==len(c)-2):
                    step=step+1
                    break
                
        if(c[i+1]==1):
            i=i+2
            step=step+1
            if(i==len(c)-2):
                    step=step+1
                    break
    return step

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
