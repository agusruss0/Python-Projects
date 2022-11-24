
from pprint import pprint


def vacio_siguiente(puzzle):
    for f in range(9):
        for c in range(9):
            if puzzle[f][c] == -1:
                return f, c
    return None, None

def es_valido(puzzle, guess,fila, col):#verifica si el intento es valido en l fila/columna
    #devuelce True si es valido, False si ees falso
    val_fila = puzzle[fila]
    if guess in val_fila:
        return False
    
    val_col = [puzzle[i][col] for i in range(9)]
    if guess in val_col:
        return False
    
    #despues el cuadrado
    #queremos obtener donde empieza el cuadrado de 3x3
    #e iterar sobre los 3 valores en el fila/col
    fila_ini = (fila // 3)*3
    col_ini = (col // 3)*3

    for f in range(fila_ini, fila_ini+3):
        for c in range(col_ini, col_ini+3):
            if puzzle[f][c] == guess:
                return False
    return True
    
    

def res_sudoku(puzzle): #resolver el sudoku usando backtracking
    # el puzzle es una lista de listas donde cada lista es una fila en el sudoku
    #devuelve si existe una solucion
    #cambia el puzzle para hacer la solucion
    fila, col = vacio_siguiente(puzzle)

    #Si no hay lugar libre, terminamos por q no se permiten mas inputs
    if fila is None:
        return True
    
    #si hay lugar adivinamos entre el 1-9
    for guess in range(1, 10):
        if es_valido(puzzle,guess,fila, col):#ver si es valido
            puzzle[fila][col] = guess #ahora recursar usando este puzzle
            if res_sudoku(puzzle): #recursivamente llamar a la funcion
                return True
        #si no es valido o el intento no resuelve el puzzle entonces tenemos que retroceder y probar de nuevo
        puzzle[fila][col] = -1 #resetea el intento
    #si ningun numero funciona significa que no hay solucion 
    return False

if __name__=="__main__":
    tabla_ej = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(res_sudoku(tabla_ej))
    pprint(tabla_ej)