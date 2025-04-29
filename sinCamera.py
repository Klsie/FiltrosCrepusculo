import cv2
from tkinter import filedialog
import numpy as np

def cargar_y_filtrar():
    filepath = filedialog.askopenfilename(filetypes=[("Imagen", "*.jpg *.png *.jpeg")])
    if not filepath:
        return
    
    img = cv2.imread(filepath)
    if img is None:
        print("Error cargando la imagen.")
        return
    
    img_filtrada = filtro_crepusculo(img)
    cv2.imshow("Imagen con Filtro Crepúsculo", img_filtrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def filtro_crepusculo(img):
    # Filtro estilo crepúsculo: tonos fríos + contraste
    azul_crepusculo = np.full(img.shape, (166, 119, 0), dtype=np.uint8)  # BGR

    # Mezclamos la imagen original con la capa azul (alpha blending)
    filtrada = cv2.addWeighted(img, 0.6, azul_crepusculo, 0.4, 0)
    
    # (Opcional) Aumentar el contraste un poco
    filtrada = cv2.convertScaleAbs(filtrada, alpha=1.1, beta=5)
    return filtrada
