# Uses python3
def fast_fib_calc(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        fib=[0]*(n+1)
        fib[0]=0
        fib[1]=1

        for i in range(2,n+1):
            fib[i]=fib[i-1]+fib[i-2]
        return fib[n]     # / return fib[-1]

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(fast_fib_calc(n))
