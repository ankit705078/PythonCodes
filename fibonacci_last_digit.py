# Uses python3

def pisano(m=10):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        a,b=0,1
        c=0

        for i in range(m*m):
            c=(a+b)%m
            a=b
            b=c

            if(a==0 and b==1):      # beacuse pisano sequence starts with 01 always hence it is also start of new hence return
                return i+1


def fast_fib_calc(n):

    n=n%pisano(10)                  # pisano lenth for 10 bcz for last digit need sequence of all single digits (0-9)
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        fib=[0]*(n+1)
        fib[0]=0
        fib[1]=1

        for i in range(2,n+1):
            fib[i]=(fib[i-1]%10+fib[i-2]%10)%10
        return fib[n]     # / return fib[-1]

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(fast_fib_calc(n))
