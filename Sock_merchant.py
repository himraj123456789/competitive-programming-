#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pair=0
    i=0
    while(i<len(ar)-1):
        count=1
        select=ar[i]
        j=i+1
        while(select==ar[j]):
            count=count+1
            j=j+1
            if(j==len(ar)):
                break
        x=int(count/2)
        pair=pair+x
        i=j
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
