import time

inicio = time.time()

def productoria(n):
    p = 1
    for i in range(1, n+1):
        producto = i**3
        p = p * producto
    print(p)

productoria(int(input()))

fin = time.time()
print (fin-inicio)

""" PRODUCTORIAS
i factorial !
2*i-1 producto de los nros impares
2*i producto de los nros pares
2**i producto de las potencias de 2
i**2 producto de los cuadrados
i**3 producto de los cubos
(-1)**i * i**2 producto de los cuadrados alternados
(-1)**i * i**3 producto de los cubos alternados

"""