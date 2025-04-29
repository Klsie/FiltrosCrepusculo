import cv2
from sinCamera import filtro_crepusculo

def capturar_con_filtro():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    print("Presiona 's' para tomar la foto, 'q' para salir.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error capturando frame.")
            break
        
        cv2.imshow("Vista previa - Presiona 's' para capturar", frame)
        key = cv2.waitKey(1)
        
        if key == ord('s'):
            foto = frame.copy()
            break
        elif key == ord('q'):
            foto = None
            break

    cap.release()
    cv2.destroyAllWindows()

    if foto is not None:
        foto_filtrada = filtro_crepusculo(foto)
        cv2.imshow("Foto con Filtro Crepúsculo", foto_filtrada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
