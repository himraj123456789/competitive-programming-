#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(0,len(a)):
        if(a[i]>b[i]):
            alice=alice+1
        elif(a[i]<b[i]):
            bob=bob+1
        else:
            alice=alice
            bob=bob
    return (alice,bob)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
