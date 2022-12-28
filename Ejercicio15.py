import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()



# Crear la lista de elementos y añadirla a la ventana
elementos = ["pera", "manzana", "plátano", "naranja"]
lista = tk.Listbox(ventana, selectmode="multiple")
for elemento in elementos:
    lista.insert("end", elemento)
lista.pack()

# Crear un botón para imprimir los elementos seleccionados
# def imprimir_seleccion():
#     seleccion = lista.curselection()
#     print([elementos[i] for i in seleccion])

# boton = tk.Button(ventana, text="Imprimir selección", command=imprimir_seleccion)
# boton.pack()

ventana.title("Lista de elementos")
# Crear una etiqueta y añadirla a la ventana
etiqueta = tk.Label(ventana, text="Hola, soy una etiqueta")
etiqueta.pack()
# Iniciar el bucle de eventos de la ventana
ventana.mainloop()