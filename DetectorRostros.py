import cv2

# Cargamos el clasificador de Haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Iniciamos la captura de video
cap = cv2.VideoCapture(0)
contador_total = 0

while True:
    # Leemos la imagen
    ret, img = cap.read()
    # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detectamos las caras
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Sumamos el número de caras detectadas en este cuadro
    contador_total += len(faces)
    
    # Imprimimos tanto el número de caras en el cuadro actual como el total acumulado
    print("Caras en este cuadro:", len(faces))
    print("Total acumulado de detecciones:", contador_total)
    
    # Dibujamos un rectángulo alrededor de cada cara detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    # Mostramos la imagen con la detección
    cv2.imshow('Imagen', img)
    
    # Salir al presionar 'esc'
    k = cv2.waitKey(30)
    if k == 27:
        break

# Liberamos la cámara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
