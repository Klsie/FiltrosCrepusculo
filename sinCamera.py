from tkinter import filedialog
from PIL import Image, ImageEnhance

class Archivos:
    def __init__(self):
        pass

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Archivos de imagen", "*.jpg *.png *.jpeg *.bmp")]
        )
        if ruta:
            imagen = Image.open(ruta)
            return self.aplicar_filtro(imagen)
        else:
            return None

    def aplicar_filtro(self, imagen):
        enhancer = ImageEnhance.Color(imagen)
        imagen_filtrada = enhancer.enhance(1.5)  # mismo efecto que la otra clase
        return imagen_filtrada
