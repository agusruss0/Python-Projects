import time

inicio = time.time()

def sumatoria (n):
    s=0
    for i in range(1,n+1): # 1=indice de sumacion 
        serie = (-1)**i * i**2
        s = s + serie
    print(s)

sumatoria(int(input()))

fin = time.time()
print(fin-inicio)

""" SERIES 
1/i 
2*i-1 suma de nros impares
2*i suma de nros pares
2**i suma de las potencias de 2
i**2 suma de los cuadrados
i**3 suma de los cubos
(-1)**i * i**2 suma de los cuadrados alternados
(-1)**i * i**3 suma de los cubos alternados
(2*i-1)**2 suma de los cuadrados impares
(2*i)**2 suma de los cuadrados pares


"""

