total=10
primos=[]
n=2
cuenta=0
while cuenta<total:
    j=0
    while j<len(primos) and n%primos[j]!=0:
        j=j+1
    if j==len(primos):
         primos.append(n)
         cuenta=cuenta+1
    n=n+1
print(primos)
    
