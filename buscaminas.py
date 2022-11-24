import random
import re

class Tabla:
    def __init__(self, dim_size, num_boms):
        self.dim_size = dim_size
        self.num_bombs = num_boms
        #Crear nueva tabla
        self.tabla = self.nuevaTabla() #plantar bombas
        self.asig_val_tabla()
        #Mantener un registro de que locaciones ya derscubrimos
        #vamos a guardar (filas,colm) tuples adentro del set
        self.dug = set()

    def nuevaTabla(self): #construir una nueva tabla con las dim_size y num_bombs 
        tabla = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        #plantar las bombas
        bombas_plantadas = 0
        while bombas_plantadas < self.num_bombs:
            location =  random.randint(0, self.dim_size**2-1) #devuelve un nro entero N random talque a <= N <= b
            fila = location // self.dim_size #queremos la cantidad de veces que dim_size pasa por location
            col = location % self.dim_size 

            if tabla[fila][col] == "X":
                continue
            
            tabla [fila][col] = "X" #planta la bomba
            bombas_plantadas += 1
        return tabla 

    def asig_val_tabla(self): #queremos asignar un nro 0-8 para todos los espacios vacios
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.tabla[r][c] == "X": #si ya es una bomba, no calculamos nada
                    continue
                self.tabla[r][c] = self.num_bombs_cerca (r, c)
    
    def num_bombs_cerca(self, fila, col): #iteramos a traves de cada una de las posiciones vecinas y sumamos el nro de bombas
    #arriba-izq: (fila-1, col-1)
    #arrba-med: (fila-1, col)
    #arriba-der: (fila-1, col+1)
    #izq: (fila, col-1)
    #der. (fila, col+1)
    #abajo-izq: (fila+1, col-1)
    #abajo-med: (fila+1, col)
    #abajo-der: (fila+1, col+1)
        num_bombas_cerca = 0
        for r in range(max(0,fila-1), min(self.dim_size-1, fila+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1, col+1)+1):
                if r == fila and c == col: #posicion original, no se chekea
                    continue
                if self.tabla[r][c] == "X":
                    num_bombas_cerca += 1
        return num_bombas_cerca

    def tocar(self, fila, col):
        #buscar en esa posicion
        # devolver True si se toco exitosamente

        #caso1: toca una bomba ->Pierde
        #caso2: toca una posicion con bombas vecinas -> termina el toque
        #caso3: toca una posicion sin bombas vecinas -> tocar recurivamente espacios vecinos
        self.dug.add ((fila, col))

        if self.tabla[fila][col] == "X":
            return False
        elif self.tabla[fila][col] > 0:
         return True
    
        for r in range(max(0,fila-1), min(self.dim_size-1, fila+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue #no busques donde ya buscaste
                self.tocar(r, c)
        return True #si e toque inicial no toco una bomba, no deberiamos tocar una bomba ahi

    def __str__(self): #si printiamos este objeto, va a printear lo q esta funcian devuelva. devuelve un string que muestra la tabla al jugador
        tabla_visible = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for fila in range(self.dim_size):
            for col in range (self.dim_size):
                if (fila, col) in self.dug:
                    tabla_visible[fila][col] = str(self.tabla[fila][col])
                else: 
                    tabla_visible[fila][col] = " "
            
            
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], tabla_visible)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(tabla_visible)):
            row = tabla_visible[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep       


def play(dim_size=10, num_bombs=10):
    #paso1:  crear la tabla y plantar las bombas
    tabla = Tabla(dim_size, num_bombs)

    #paso2: mostrarle el tablero al jugador y preguntar donde quiere tocar

    #paso3a: si el lugar es una bomba, se termina el juego
    #paso3b: si el lugar no es una bomba tocar recursivamente hasta que cada cuadrado este al menos al lado de la bomba
    #paso4: repetir pasos 2 y 3a/b hasta que no haya mas lugares para tocar
    safe = True
    while len(tabla.dug) < tabla.dim_size**2 - num_bombs:
        print(tabla)
        us_input = re.split(",(\\s)*", input("Donde queres buscar? poner fila y columna: ")) 
        fila, col = int(us_input[0]), int(us_input[-1])
        if fila < 0 or fila >= tabla.dim_size or col < 0 or col >= tabla.dim_size:
            print("Posicion invalida. Intente de nuevo: ")
            continue

        safe = tabla.tocar(fila, col) #Si es valido buscamos
        if not safe:
            break #game over
    
    if safe:
        print("Ganaste!!")
    else:
        print("Perdiste!!")
        tabla.dug = [(r, c) for r in range(tabla.dim_size) for c in range(tabla.dim_size)]
        print(tabla)

if __name__== "__main__":
    play()
