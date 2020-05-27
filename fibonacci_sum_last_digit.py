
def pisanoperiod(m):
    a=0
    b=1
    c=0
    for i in range(m*m):
        c=(a+b)%m
        a=b
        b=c
        if(a==0 and b==1):
            return i+1             #+1 because length cannot be 0
        
        

def findfibagain(n,m):
    pisolen=pisanoperiod(m)
    
    nth=n%pisolen
    
    if(nth==0):
        return 0
    elif nth==1:
        return 1
    else:
        fib=[0]*(nth+1)
        fib[0]=0
        fib[1]=1
        for i in range(2,nth+1):
            fib[i]=(fib[i-1]%m+fib[i-2]%m)%m
    return sum(fib)%10


if __name__=='__main__':
    n=int(input())
    print(findfibagain(n,10))
    
