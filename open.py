archivo=open('Miles-Davis.txt')
# Cantidad de lineas
cuenta=0
for renglon in archivo:
    cuenta=cuenta+1
# Lineas donde aparece una palabra
    lineas=renglon.rstrip()
    if lineas.startswith('Miles'):
        print(lineas)
print(cuenta)
