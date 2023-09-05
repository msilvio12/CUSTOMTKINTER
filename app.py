import json
import tkinter as tk
from customtkinter import CTk
import customtkinter as ctk
import PIL.Image


# Crea la imagen ligera
light_image = PIL.Image.open("image-light.jpg")

# Crea la imagen oscura
dark_image = PIL.Image.open("image-dark.jpg")

# Crea el widget CTkImage
image_widget = ctk.CTkImage()

# Establece las imágenes del widget
image_widget.light_image = light_image
image_widget.dark_image = dark_image

# Muestra el widget
image_widget.pack()
# Cargar los datos
with open("CUSTOMTKINTER/resto.json") as f:
    restaurantes = json.load(f)

 
for restaurante in restaurantes:
    restaurante["imagen"] = "imagenes/{}.jpg".format(restaurante["nombre"])

# Se crea la ventana principal
root = ctk.CTk()
root.title("Comidas en Salta")

# Se crea el logueo de usuario y contraseña
login_frame = ctk.CTkFrame(root)
user_entry = ctk.CTkEntry(login_frame)
password_entry = ctk.CTkEntry(login_frame, show="*")
login_button = ctk.CTkButton(login_frame, text="Iniciar sesión")
login_button.configure(command=lambda: login(user_entry.get(), password_entry.get()))

user_entry.pack(side="left")
password_entry.pack(side="left")
login_button.pack(side="left")

# Se crea la galería de imágenes
gallery_frame = ctk.CTkFrame(root)
image_list = []
for restaurante in restaurantes:
    image = tk.PhotoImage(file=restaurante["imagen"])
    image_list.append(image)

image_viewer = ctk.CTkImage(gallery_frame, image_list)
image_viewer.pack()

# Muestra la ventana principal
root.mainloop()

# Función para iniciar sesión
def login(user, password):
    if user == "admin" and password == "admin":
        root.children["login_frame"].pack_forget()
        root.children["gallery_frame"].pack()
    else:
        tk.messagebox.showerror("Error", "Usuario o contraseña incorrectos")