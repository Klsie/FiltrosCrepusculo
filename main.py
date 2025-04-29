import tkinter as tk
from PIL import ImageTk
from camera import Camera
from sinCamera import Archivos

# Crear instancias de las clases
camara = Camera()
archivos = Archivos()

def mostrar_imagen(imagen_pil):
    if imagen_pil is not None:
        imagen_pil = imagen_pil.resize((400, 400))
        img_tk = ImageTk.PhotoImage(imagen_pil)
        panel.config(image=img_tk)
        panel.image = img_tk

def boton_subir():
    imagen = archivos.abrir_archivo()
    mostrar_imagen(imagen)

def boton_capturar():
    imagen = camara.tomar_foto()
    mostrar_imagen(imagen)

# Interfaz principal
root = tk.Tk()
root.title("App Crepúsculo")

frame = tk.Frame(root)
frame.pack()

btn_archivo = tk.Button(frame, text="Subir Foto", command=boton_subir)
btn_archivo.grid(row=0, column=0, padx=10, pady=10)

btn_camara = tk.Button(frame, text="Tomar Foto", command=boton_capturar)
btn_camara.grid(row=0, column=1, padx=10, pady=10)

panel = tk.Label(root)
panel.pack(padx=10, pady=10)

root.mainloop()


