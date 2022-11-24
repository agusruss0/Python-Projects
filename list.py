# 1ra lista
from operator import truediv


x=['hola',2020,[28,2],'mundo']
print(x)
#Listas con loop
for n in [1,2,3,4,5]:
    print(n)
print ('listo')
#2da lista con loop
amigos=['cande','ebi','joaco']
for amigo in amigos:
    print('Feliz año',amigo)
print('listo')
#Llamar a items puntuales
x=[1,39,54,76,23]
print(x[1])
#Y cambiarlos
x[1]=0
print(x)
#Para ver que tan grande es la lista (len())
print('largo:',len(x))
#Funcion range()
r=['hola','buen','dia','?']
print(range(len(r)))

#Operaciones con listas
a=[1,2,3]
b=[4,5,6]
c= a+b
print(c)
#Slice la lista [:]
s=[1,32,43,54,65,76]
print(s[1:4])
#Metodos de lista(append,count,extend,index,insert,pop,remove,rever,sort)
#Append
lista=list()
lista.append('hola')
lista.append(1000)
print(lista)
#Ver si hay algo en la lista (in)
print(1000 in lista)
#Sort: ordenar
desorden=[58,63,12,88,1]
desorden.sort()
print(desorden)
nombre=['lara','cande','agus','ebi']
nombre.sort()
print(nombre)
#Built-in Functions
num=[56,69,78,43,12,38]
print(len(num))
print(min(num))
print(max(num))
print(sum(x))
print(sum(x)/len(x))
#Dos formas de hacer lo mismo
total=0
index=0
while True:
    inp=input('Numero: ',)
    if inp== 'ok': break
    value= float(inp)
    total=total+value
    index=index+1
print(total/index)
#2da forma
nums=list()
while True:
    value=input('numero:',)
    if value=='ok':break
    values=float(value)
    nums.append(values)
print(sum(nums)/len(nums))
#agregar nros y ordenarlos
nros=list()
while True:
    random=input('numero:',)
    if random=='ok': break
    randomnro=float(random)
    nros.append(randomnro)
    nros.sort()
print(nros)
#Listas y Strings
abc='Hola como estas?'
abc2=abc.split()
print(abc2)
#Extraer cierta palabra
miles=open('Miles-Davis.txt')
for lineas in miles:
    lineas=lineas.rstrip()
    if not lineas.startswith('En'):continue
    resumen=lineas.split()
    print(resumen[3])
#Doble split
correo='De andaalaconchadetuhermana@yahoo.com.ar Vie 23 Abril 2023 17:34hs'
correo2=str(correo)
palabras=correo2.split()
mail=palabras[1]
parte=mail.split('@')
print(parte[0])

