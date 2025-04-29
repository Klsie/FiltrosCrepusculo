import cv2
from tkinter import filedialog
import numpy as np
import pygame 

def cargar_y_filtrar():
    filepath = filedialog.askopenfilename(filetypes=[("Imagen", "*.jpg *.png *.jpeg")])
    if not filepath:
        return
    
    img = cv2.imread(filepath)
    if img is None:
        print("Error cargando la imagen.")
        return
    
    img_filtrada = filtro_crepusculo(img)
    cv2.imshow("Imagen con Filtro Crepusculo", img_filtrada)
    musiquita()
    cv2.waitKey(0)
    detener_musica()
    cv2.destroyAllWindows()

def filtro_crepusculo(img):
    azul_crepusculo = np.full(img.shape, (166, 119, 0), dtype=np.uint8)  # BGR
    filtrada = cv2.addWeighted(img, 0.6, azul_crepusculo, 0.4, 0)    
    filtrada = cv2.convertScaleAbs(filtrada, alpha=1.1, beta=5)
    return filtrada

import pygame

def musiquita():
    pygame.mixer.init()
    pygame.mixer.music.load("cancion.mp3")
    pygame.mixer.music.play(-1)  # Reproduce en bucle (infinito)
  
    print("♫ Música sonando en segundo plano...")

def detener_musica():
    pygame.mixer.music.stop()
    print("⏹️ Música detenida.")