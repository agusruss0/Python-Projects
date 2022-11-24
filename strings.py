from traceback import print_tb


fruta='banana'
index=0
cuenta=0
# Contar el total de letras en el string
while index<len(fruta):
    letra=fruta[index]
    print(index,letra)
    index=index+1
# Contar las 'A' dentro del string
for letras in fruta:
    if letras=='a':
        cuenta=cuenta+1
print ('Nº de A:',cuenta)
# Separar Strings
s= 'Mañana llueve'
print (s[0:5])
# Comparar Strings + String Library
nro= input('Palabra: ')
if nro == 'bananas':
    print('bananas!!'.upper())
elif nro>'bananas':
    print('Mayor')
elif nro<'bananas':
    print('Menor')
else:
    print('Igual')
