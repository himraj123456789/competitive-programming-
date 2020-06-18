
def count_valleys(n,t):
    
    t=str(t)
    i=0
    sum1=0
    valley=0
    while(i!=len(t)):

        x=t[i]
        
        if(x=='U'):
            temp=sum1
            sum1=sum1+1
        
            if(sum1==0 and temp ==-1):
                valley=valley+1
        if(x=='D'):
            temp=sum1
            sum1=sum1-1
        
            if(sum1==0 and temp == -1):
                valley=valley+1
        i=i+1

    return valley


n = int(input().strip())
steps = input().strip()
result = count_valleys(n, steps)
print(result)
