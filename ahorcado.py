print('Elegi tu palabra: ')
palabra=input()
errores=0
progreso= []
for i in range(len(palabra)):
    progreso.append('_ ')
palabra_con_espacio=[]
for char in palabra:
    palabra_con_espacio.append(char+' ')
letras_usadas=[]
while errores <7:
    if errores==0:
        print(' ____  ')
        print(' |  |  ')
        print(' |     ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif errores==1:
        print(' ____  ')
        print(' |  |  ')
        print(' |  0  ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif errores==2:
        print(' ____  ')
        print(' |  |  ')
        print(' |  0  ')
        print(' |  |  ')
        print(' |     ')
        print('---    ')
    elif errores==3:
        print(' ____  ')
        print(' |  |  ')
        print(' |  0  ')
        print(' |  |  ')
        print(' | /   ')
        print('---    ')
    elif errores==4:
        print(' ____  ')
        print(' |  |  ')
        print(' |  0  ')
        print(' |  |  ')
        print(' | / \ ')
        print('---    ')
    elif errores==5:
        print(' ____  ')
        print(' |  |  ')
        print(' |  0  ')
        print(' | /|  ')
        print(' | / \ ')
        print('---    ')
    elif errores==6:
        print(' ____  ')
        print(' |  |  ')
        print(' |  0  ')
        print(' | /|\ ')
        print(' | / \ ')
        print('---    ')
        print('PERDISTE!!')
        break
    print(''.join(progreso))
    print('Letra usadas: ', letras_usadas)
    print('Elegi una letra:')
    letra=input()
    if letra in letras_usadas:
        print('Ya la usaste...')
    else:
        letras_usadas.append(letra)
        hay_error=True
        for i in range(len(palabra)):
            if letra==palabra[i]:
                progreso[i]=letra+' '
                hay_error=False
        if hay_error:
            errores=errores +1
        if palabra_con_espacio==progreso:
            print(''.join(progreso))
            print('GANASTE!!')
            break