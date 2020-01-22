
nofiter=int(input())


elem = [ int(v) for v in input().split() ]

subarr=[]

for i in range (len(elem)):
    
    for j in range (i+1):
        subarr.append(elem[j:i+1])
    
print(subarr)
    
