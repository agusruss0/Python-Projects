#Primer Diccionario
bosque=dict()
bosque['Arbol']=100
bosque['Hojas']=10000
bosque['Animales']=500
print(bosque)

#Cambiar valores dentro
bosque['Hojas']=bosque['Hojas']+500
print(bosque)

#Diccionarios Constantes
dic2={'Nombre': 'Agustin', 'Apellido': 'Russo'}
print(dic2)

#Histogramas (cuantas veces aparece algo)
cuenta=dict()
nombres=['Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari','Agus','Ebi','Cande','Lari',]
for nombre in nombres:
    if nombre not in cuenta:
        cuenta[nombre]=1
    else:
        cuenta[nombre]=cuenta[nombre]+1
print(cuenta)

#Metodo get
cue=dict()
palabras=['Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales','Arbol','Agua','Animales']
for palabra in palabras:
    cue[palabra]=cue.get(palabra,0)+1
print(cue)

#Ver cual es la palabra mas repetida
cuentas=dict()
lineas='Frédéric Chopin nació en la aldea de Żelazowa Wola, a 60 kilómetros de Varsovia, en una pequeña finca propiedad del conde Skarbek, que formaba parte del Gran Ducado de Varsovia (voivodato de Mazovia, Polonia). Recibió el nombre de Fryderyk Franciszek Chopin. ​La fecha de su nacimiento es incierta: el propio compositor (y su familia) declaraba haber nacido el 1 de marzo de 1810 y siempre celebró su cumpleaños en aquella fecha. Pero en su partida bautismal figura como nacido el 22 de febrero.'
words=lineas.split()
print('Words:',len(words))
print('contando...')
for word in words:
    cuentas[word]=cuentas.get(word,0)+1
print('TOTAL:',cuentas)

#Ir pasando por las key y viendo los valores
bag={'remeras':1,'pantalones':2, 'calzones':4}
for key in bag:
    print(key,bag[key])

#Obteniendo listas de los dicc
jjj={'Agus':24,'Clara':23,'Fran':18}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#Iteraciones de 2 variables
for aaa,bbb in jjj.items():
    print(aaa,bbb)

#Encontrar la palabra que mas se repite
ins=open('Chopin.txt')
busqueda=dict()
for line in ins:
    letters=line.split()
    for letter in letters:
        busqueda[letter]=busqueda.get(letter,0)+1
masrepetida= None
nrodeveces= None
for letter, nro in busqueda.items():
    if nrodeveces is None or nro> nrodeveces:
        masrepetida=letter
        nrodeveces=nro
print(masrepetida,nrodeveces)