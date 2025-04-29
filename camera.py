import cv2
from PIL import Image, ImageEnhance

class Camera:
    def __init__(self):
        pass

    def tomar_foto(self):
        cap = cv2.VideoCapture(0)  # 0 = cámara principal
        ret, frame = cap.read()
        if ret:
            cap.release()
            # Aplicar efecto tipo "Crepúsculo"
            twilight_frame = self.aplicar_filtro(frame)
            return twilight_frame
        else:
            cap.release()
            raise Exception("No se pudo capturar imagen")

    def aplicar_filtro(self, imagen):
        # Convertir a PIL para aplicar filtro sencillo
        imagen_pil = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
        enhancer = ImageEnhance.Color(imagen_pil)
        imagen_filtrada = enhancer.enhance(1.5)  # más color (como estilo película)
        return imagen_filtrada
