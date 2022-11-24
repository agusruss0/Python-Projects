import time

def cuentaregre(t):
    while t:
         
         min, sec = divmod(t,60)
         timer = "{:02d} min:{:02d} s".format(min, sec)
         print(timer, end="\r")
         time.sleep(1)
         t -= 1

    print("Tiempo completado!")

t = input("Ingrese su tiempo: ")

cuentaregre(int(t*60))
