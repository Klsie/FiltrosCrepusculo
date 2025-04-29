import cv2
import os
from PIL import Image, ImageEnhance

# Suponiendo que 'capturas' es la carpeta donde se guardan las imágenes
capturas = "capturas"  # Asegúrate de que esta carpeta exista

if not os.path.exists(capturas):
    os.makedirs(capturas)

# Abrir la cámara
cap = cv2.VideoCapture(0)

def aplicar_filtro_crepusculo(imagen):
    # Convertir a PIL para aplicar filtro de Crepúsculo
    imagen_pil = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    enhancer = ImageEnhance.Color(imagen_pil)
    imagen_filtrada = enhancer.enhance(1.5)  # Más color (efecto Crepúsculo)
    return cv2.cvtColor(np.array(imagen_filtrada), cv2.COLOR_RGB2BGR)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se puede leer el frame.")
        break

    # Mostrar el frame en una ventana de OpenCV
    cv2.imshow('FOTITO CHECK', frame)
    key = cv2.waitKey(1) & 0xFF

    # Activar filtro y guardar con 's'
    if key == ord('s'):
        # Aplicar el filtro Crepúsculo
        frame_filtrada = aplicar_filtro_crepusculo(frame)

        # Mostrar la imagen filtrada
        cv2.imshow('Imagen Crepúsculo', frame_filtrada)

        # Guardar la imagen con el filtro
        cv2.imwrite(os.path.join(capturas, 'captura_crepusculo.png'), frame_filtrada)
        print("Captura guardada en la carpeta 'capturas'.")

    # Salir con la tecla 'q'
    elif key == ord('q'):
        break

# Liberar cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
