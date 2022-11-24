from player import CompuGenio, playerReal, randomCompuPlay
import time 

class tateti:
    def __init__(self):
        self.tabla = [" " for _ in range(9)]
        self.actual_ganador = None

    def printTabla(self):
        for fila in [self.tabla[i*3:(i+1)*3] for i in range(3)]:
            print (" | " + " | ".join(fila) + " | ")

    @staticmethod

    def mostarNrosTabla():
        nroTabla = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for fila in nroTabla:
            print(" | " + " | ".join(fila) + " | ")
   
    def movDisponibles(self):
        return [i for i, espacio in enumerate(self.tabla) if espacio == " "]
    
    def vacios (self):
        return " " in self.tabla
    
    def nrosVacios (self):
        return self.tabla.count(" ")
    
    def turno(self, cuadra, letter):
        if self.tabla[cuadra] == " ":
            self.tabla[cuadra] = letter
            if self.ganador(cuadra, letter):
                self.actual_ganador = letter
            return True
        return False
    
    def ganador(self, cuadra, letter):
        fila_ind = cuadra // 3
        fila = self.tabla[fila_ind*3 : (fila_ind+1)*3]
        if all([espacio == letter for espacio in fila]):
            return True
        col_ind = cuadra % 3
        col = [self.tabla[col_ind*3 :(col_ind+1)*3] for i in range(3)]
        if all([espacio == letter for espacio in col]):
            return True
        if cuadra % 2 == 0:
            diago1 = [self.tabla[i] for i in [0, 4, 8]]
            if all([espacio == letter for espacio in diago1]):
                return True
            diago2 = [self.tabla[i] for i in [2, 4, 6]]
            if all([espacio == letter for espacio in diago2]):
                return True
        return False

def play(game, x_player, o_player, printGame=True):
    if printGame:
        game.mostarNrosTabla()
    
    letter = "X"
    while game.vacios():
        if letter == "O":
            cuadra = o_player.mover(game)
        else:
            cuadra = x_player.mover(game)
        if game.turno (cuadra, letter):
            if printGame:
                print(letter + f" Ocupa el cuadrado {cuadra}")
                game.printTabla()
                print(" ")
            if game.actual_ganador:
                if printGame:
                    print(letter + " Gano!!")
                return letter
            letter = "O" if letter =="X" else "X"
        
        time.sleep(0.8)

    if printGame:
        print("Empate!")

if __name__ == "__main__":
    x_player = playerReal('X')
    o_player = CompuGenio("O")
    t = tateti()
    play(t, x_player, o_player, printGame=True)