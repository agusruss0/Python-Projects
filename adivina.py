import random

valores= int(input("Se juega desde el 1 al... "))   

def adivina(x):
        nro_random = random.randint(1,x)
        adivina = 0
        cuenta = 0
        while adivina != nro_random:
            adivina = int(input(f"Adivina el numero entre 1 y {x}: "))
            if adivina < nro_random and adivina >=1:
                print("Muy bajo, proba de vuelta!")
            elif adivina > nro_random and adivina<=x:
                print("Muy alto, proba de nuevo!")
            elif adivina == 000:
                break        
            elif adivina<1 or adivina>x:
                print("Ese numero no esta en el juego")
            cuenta = cuenta + 1
        print (f"Correcto!! adivinaste el numero {nro_random} en {cuenta} intentos")

def com_adivina(x):
        bajo = 1
        alto = x
        feedback = " "
        cuenta2 = 0
        while feedback != "c": 
            if bajo != alto:
                adivina = random.randint(bajo, alto)
            else:
                adivina = bajo
            feedback = input(f"Es {adivina} muy alto (A), muy bajo(B), o correcto (C)?? ").lower()
            if feedback == "a":
                alto = adivina - 1
            elif feedback =="b":
                bajo = adivina + 1
            elif feedback == "p":
                break
            #elif bajo>x or alto<1:    
                print ("Tu numero no pertenece al juego")
            cuenta2 = cuenta2 + 1
        print(f"La computadora adivino el numero {adivina} en {cuenta2} intentos!!")

adivina(valores)
com_adivina(valores)

#print()

#while contador1 and contador2 != 50:
   
    
    #if contador1 == 50:
       # print(f"La computadora ha ganado con {contador2} intentos")
    #elif contador2 == 50:
       # print(f"Ganaste con {contador1} intentos")