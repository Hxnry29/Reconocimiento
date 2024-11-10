#pip install deepface
#pip install opencv-python

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


import cv2
import os
from deepface import DeepFace
from datetime import datetime
import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('emociones.db')
cursor = conn.cursor()

# Crear la tabla 'EMOTIONS' si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMOTIONS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Emotion TEXT,
        Gender TEXT,
        Age INTEGER,
        CreatedAt DATETIME
    )
''')
conn.commit()

# Cargar el clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar el logo
logo = cv2.imread('logo.jpg', cv2.IMREAD_UNCHANGED)  # Leer el logo

# Verifica que el logo se haya cargado correctamente
if logo is None:
    print("No se pudo cargar el logo.")
    exit()

# Iniciar la captura de video desde la webcam
cap = cv2.VideoCapture(0)

scaling_factor = 1  # Parámetro que especifica cuánto se reduce el tamaño de la imagen en cada iteración

while True:
    # Capturar un frame de video
    ret, frame = cap.read()

    # Redimensionar el frame de video
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # Detectar rostros en el frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        
        # Analizar la emoción, el género y la edad del rostro
        analysis = DeepFace.analyze(face, actions=['emotion', 'gender', 'age'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']
        gender = analysis[0]['dominant_gender']
        age = analysis[0]['age']  # Edad estimada
        
        # Agregar texto de emoción, género y edad al frame
        emotion_text = f"Emoción: {emotion}"
        gender_text = f"Género: {gender}"
        age_text = f"Edad: {age}"
        
        cv2.putText(frame, emotion_text, (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.putText(frame, gender_text, (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.putText(frame, age_text, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        # Generar la cadena de tiempo
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insertar datos en la base de datos
        cursor.execute("INSERT INTO EMOTIONS (Emotion, Gender, Age, CreatedAt) VALUES (?, ?, ?, ?)",
                       (emotion, gender, age, timestamp))
        conn.commit()

    # Redimensionar el logo para que se ajuste al tamaño de la ventana
    logo_resized = cv2.resize(logo, (100, 100))  # Ajusta el tamaño del logo (puedes cambiar los valores de tamaño)
    
    # Obtener las dimensiones del frame
    h, w, _ = frame.shape

    # Definir la posición para colocar el logo en la esquina superior derecha
    top_left_x = w - logo_resized.shape[1] - 10  # 10px de margen desde el borde
    top_left_y = 10  # 10px de margen desde el borde superior

    # Superponer el logo sobre el frame
    frame[top_left_y:top_left_y + logo_resized.shape[0], top_left_x:top_left_x + logo_resized.shape[1]] = logo_resized

    # Mostrar el frame con el logo
    cv2.imshow('frame', frame)
    
    # Presionar 'q' para salir
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()

# Cerrar la conexión a la base de datos
conn.close()
