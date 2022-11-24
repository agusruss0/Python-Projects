#busqueda naive
import random
import time

def naive_search (l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

#Busqueda binaria   
def bin_search(l, target, low=None, high=None):
    if low is None:
        low = 0 
    if high is None:
        high = len(l)-1
   
    if high < low:
        return -1
    
    puntoMedio = (low + high) // 2

    if l[puntoMedio] == target:
        return puntoMedio
    elif target < l[puntoMedio]:
        return bin_search(l, target, low, puntoMedio-1)
    else:
        return bin_search (l,target, puntoMedio+1, high)

if __name__=="__main__":
    #l = [1, 2, 5, 10, 12]
    #target = 10
    #print(naive_search(l, target))
    #print(bin_search(l, target))
    length = 10000 #Creamos una lista de largo 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

#Duracion de la busqueda
    comienzo = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    final = time.time()
    print("Tiempo de busqueda Naive: ", (final - comienzo)/length, "segundos")

    comienzo = time. time()
    for target in sorted_list:
        bin_search(sorted_list, target)
    final = time.time()
    print("Tiempo de busqueda binaria:", (final - comienzo)/length, "segundos" )

print(target)