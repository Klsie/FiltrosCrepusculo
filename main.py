import tkinter as tk
from sinCamera import cargar_y_filtrar
from camera import capturar_con_filtro

def main():
    root = tk.Tk()
    root.title("Filtro Crepúsculo")
    root.geometry("300x150")

    btn_archivo = tk.Button(root, text="Subir Imagen", command=cargar_y_filtrar, width=25, height=2)
    btn_archivo.pack(pady=10)

    btn_camara = tk.Button(root, text="Tomar Foto con Cámara", command=capturar_con_filtro, width=25, height=2)
    btn_camara.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
