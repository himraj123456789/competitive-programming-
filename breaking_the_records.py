import os
import sys
import random
import math
def binary_find(t,r):
    l1=0
    r1=len(r)-1
    while(l1<=r1):
        mid=int((l1+r1)/2)
        if(r[mid]==t):
            return mid+1
            break
        if(r[mid]<t):
            if(r[mid-1]>t):
                return(mid+1)
                break
            else:
                r1=mid-1
                l1=l1
        if(r[mid]>t):
            if(r[mid+1]<t):
                return mid+2
                break
            else:
                l1=mid+1
                r1=r1

def climbingLeaderboard(x12,t12):
    
    l=[]
    i=0
    j=1
    while True:
    
        if(x12[i]>x12[j]):
            l.append(x12[i])
            j=j+1
            i=j-1
        if(j==len(x12)):
            break
        if(x12[i]==x12[j]):
            j=j+1
            p=j
        if(j==len(x12)):
            break
    l.append(x12[len(x12)-1])
    
    n=0
    while(n!=len(t12)):
        select=t12[n]
        if(select>=l[0]):
            print(1)
        
        elif(select<l[len(l)-1]):
            print(len(l)+1)
        elif(select==l[len(l)-1]):
            print(len(l))
        else:
        
            result=binary_find(select,l)
            print(result)
        n=n+1
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    x11 = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    t11= list(map(int, input().rstrip().split()))
    #x11=[100,90,90,80,75,60]
    #t11=[50,65,77,90,102]
    climbingLeaderboard(x11,t11)
    #fptr.close()
