import tkinter as tk

window = tk.Tk()

'''frame_1 = tk.Frame().pack(side=tk.RIGHT) #Crea un Frame que contiene a distintos widgets

titulo = tk.Label( #Crea un texto en la ventana
    master=frame_1, #Incluye al widget dentro del Frame elegido
    text="nombre", #Caracteristicas del widget
    fg="white",
    bg="black",
    width=10,
    height=5
    ).pack() #incluye este widget en la ventana

entry = tk.Entry( #Crea una entrada
    master=frame_1,
    fg="black",
    bg="white",
    width=25    
).pack()


txt = tk.Text( #Crea una casilla donde se ingresan textos largos
    master=frame_1,
).pack()

enter = tk.Button( #Crea un boton
    master=frame_1,
    text="Enter",
    fg="white",
    bg="black",
    width=25,
    height=5
).pack()

border_effects = { #tipos de bordes de Frame
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name, relief in border_effects.items(): #Prueba todos los bordes
    frame= tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame,text=relief_name)
    label.pack()

frm_red = tk.Frame(#Crea un frame rojo de determinada altura 
    master=window,
    width=100,
    height=100, 
    bg="red").pack(fill=tk.BOTH, side=tk.LEFT, expand=True) #y fill en pack rellena en el eje x , y o both. side decide en q lado va a estar


frm_yellow = tk.Frame(master=window, width=50,height=50,bg="yellow").pack(fill=tk.BOTH, side=tk.LEFT,expand=True)

frm_blue = tk.Frame(master=window, width=25, height=25, bg="blue").pack(fill=tk.BOTH, side=tk.LEFT,expand=True)
'''
#Grid
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75) #weight determina como va a responder al resize de la ventana
    window.rowconfigure(i, weight=1, minsize=50) #minsize es la medida minima que puede tener la altura de la fila o ancho de columna
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5) #posiciona el label en la posicion ij del grid y agregra un margen de 5
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()