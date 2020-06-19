#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    extra_add=0
    lower=round(math.sqrt(a))
    upper=round(math.sqrt(b))


#if lower and upper both are square roots
    if(lower*lower ==a and upper*upper==b):
    
        total=upper-lower+1
        return total  
    if(lower*lower>a and upper*upper==b):
        total=upper-lower+1
        return total
    if(lower*lower<a and upper*upper==b):
        lower=lower+1
        total=upper-lower+1
        return total 
    if(lower*lower==a and upper*upper>b):
        upper=upper-1
        total=upper-lower+1
        return total
    if(lower*lower ==a and upper*upper<b):
        total=upper-lower+1
        return total 
    if(lower*lower!=a and upper*upper!=b):
        
        if(lower*lower>a and upper*upper>b):
            upper=upper-1
            total=(upper-lower)+1
            return total
        if(lower*lower<a and upper*upper>b):
        
            lower=lower+1
            upper=upper-1
            total=upper-lower+1
            return total 
        if(lower*lower>a and upper*upper<b):
            return upper-lower+1
        if(lower*lower<a and upper*upper<b):
            lower=lower+1
            return upper-lower+1
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
