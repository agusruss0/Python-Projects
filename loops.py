mas_grande=-1
cuenta=0
suma=0
print('antes',mas_grande)
# Cuantos nros hay, la suma de todos, el mas grande, los nros
for numeros in [3,88,56,94,2,3,6,754,1000,1,-11]:
    if numeros>mas_grande:
        mas_grande=numeros
    cuenta=cuenta+1
    suma=suma+numeros 
    print(cuenta,suma,numeros)
print('mas grande', mas_grande)        
# Total de nros, Suma, Promedio
print(cuenta,suma,suma/cuenta)
