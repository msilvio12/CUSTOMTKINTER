import tkinter as tk
import json

# Función para mostrar la información de un restaurante en una ventana emergente
def mostrar_informacion(restaurante):
    ventana_info = tk.Toplevel(root)
    ventana_info.title(restaurante["nombre"])
    
    nombre_label = tk.Label(ventana_info, text=f"Nombre: {restaurante['nombre']}")
    nombre_label.pack()
    
    direccion_label = tk.Label(ventana_info, text=f"Dirección: {restaurante['direccion']}")
    direccion_label.pack()
    
    # 
    imagen = tk.PhotoImage(file=restaurante["imagen"])
    imagen_label = tk.Label(ventana_info, image=imagen)
    imagen_label.image = imagen  # Necesario para que la imagen se muestre correctamente
    imagen_label.pack()

# Cargar los datos de restaurantes desde un archivo JSON
with open('CUSTOMTKINTER/restos.json', 'r') as file:
    datos_restaurantes = json.load(file)

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("App de Restaurantes")

# Crear una lista de botones para cada restaurante
for restaurante in datos_restaurantes['restaurantes']:
    nombre = restaurante['nombre']
    boton = tk.Button(root, text=nombre, command=lambda r=restaurante: mostrar_informacion(r))
    boton.pack()

root.mainloop()
