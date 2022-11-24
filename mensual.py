def mensualidad(t,s,d,f,o):
    viaje = 4*(d*(t+0.75*s + s+0.75*t))
    comida = 4*(d*f)
    salidas = 4*o
    total = viaje + comida + salidas
    print(f"Por mes gastas {viaje} en transporte, {comida} en comida y {salidas} en salidas, en total seria {total}")

mensualidad(9.50, 30, 5, 175, 750)
    
