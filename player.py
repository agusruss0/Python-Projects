import math 
import random

class player:
    def __init__(self, letter):
       self.letter = letter

    def mover(self, game):
        pass

class randomCompuPlay(player):
    def __init__(self, letter):
        super().__init__(letter)

    def mover(self, game):
        cuadra = random.choice(game.movDisponibles())
        return cuadra

class playerReal(player):
    def __init__(self, letter):
        super().__init__(letter)
    def mover(self, game):
        cuadraDispo = False
        val = None
        while not cuadraDispo:
            cuadra = input(self.letter + "\'s turn. Ingrese lugar (0-8): ")
            try:
                val = int(cuadra)
                if val not in game.movDisponibles():
                    raise ValueError
                cuadraDispo = True
            except ValueError:
                print("Ya esta ocupado! Proba otro...")
        return val

class CompuGenio (player):
    def __init__(self, letter):
        super().__init__(letter)

    def mover(self, game):
        if len(game.movDisponibles()) == 9:
            cuadra = random.choice(game.movDisponibles())
        else:
            cuadra = self.minimax(game, self.letter)["Posicion"]
        return cuadra

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        if  state.actual_ganador == other_player:
            return {"Posicion": None,
                    "Puntaje": 1*(state.nrosVacios()+1) if other_player == max_player else -1*(state.nrosVacios()+1)}
        
        elif not state.nrosVacios():
            return {"Posicion": None, "Puntaje":0}
        
        if player == max_player:
            mejor = {"Posicion": None, "Puntaje": -math.inf}
        else:
            mejor= {"Posicion": None, "Puntaje": math.inf}
        
        for posibles in state.movDisponibles():
            
            #Paso 1: hace un movimiento, prueba el lugar
            state.turno(posibles, player)
            
            #Paso 2: Recursar usando minimax para simular un juego despues de haber hecho el movimiento
            sim_punt = self.minimax(state, other_player)
            
            #Paso 3: Deshacer el movimiento
            state.tabla[posibles] = " "
            state.actual_ganador = None
            sim_punt["Posicion"] = posibles
            
            #Paso 4: Actualizar el diccionario
            if player == max_player: #Maximizar a este jugador
                if sim_punt["Puntaje"] > mejor["Puntaje"]:
                    mejor = sim_punt
            else: #Minimizar al otro
                if sim_punt["Puntaje"] < mejor["Puntaje"]:
                    mejor = sim_punt
        
        return mejor