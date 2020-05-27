# Uses python3

def fast_gcd_calc(a,b):

    if b==0:
        return a
    aprime=a%b
    return  fast_gcd_calc(b,aprime)     #gcd(a,b) == gcd  (b,a)   since a=aprime+1(mod b)



def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

if __name__ == "__main__":
    a,b=[int(x) for x in input().split()]
    print(int((a*b)/fast_gcd_calc(a, b)))
