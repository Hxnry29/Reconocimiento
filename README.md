## Sobre Emotion_Tracker
Este proyecto presenta un algoritmo que utiliza el modelo preentrenado 'Deepface'. Se compone de varias funciones esenciales:
   + Detección en tiempo real de la emoción regsitrada
   + Detección en tiempo real del género registrado
   + Craeación de la base de datos
   + Conexión del algoritmo con la base de datos
   + Análisis de los datos registrados

## Funcionamiento del algoritmo
Este script de Python utiliza la biblioteca OpenCV para capturar video desde la webcam y detectar rostros en tiempo real. Además, utiliza la biblioteca DeepFace para analizar las emociones y el género de los rostros detectados.
Aquí hay una descripción de las principales funciones y bibliotecas utilizadas:

### Bibliotecas Importadas:
  + **pyodbc:** Permite la conexión y manipulación de bases de datos SQL Server.
    cv2 (OpenCV): Proporciona funciones para procesar imágenes y videos, incluida la detección de     rostros.
  + **os:** Proporciona funciones para interactuar con el sistema operativo, como acceder a 
    archivos.
  + **deepface:** Una biblioteca de Python para el reconocimiento facial y la detección de   
    emociones y género.
  + **datetime:** Proporciona clases para manipular fechas y horas en Python.
### Inicialización de la Captura de Video:
  + Se inicia la captura de video desde la webcam utilizando cv2.VideoCapture(0).
### Detección de Rostros:
  + Se utiliza el clasificador de Haar para detectar rostros en el video capturado.
  + Se dibuja un rectángulo alrededor de cada rostro detectado en el marco.
### Análisis de Emociones y Género:
  + Para cada rostro detectado, se extrae la región de interés (ROI) del marco.
  + Se utiliza DeepFace para analizar la emoción y el género de cada rostro.
  + Se extraen los resultados de análisis, incluida la emoción dominante y el género dominante.
### Inserción de Datos en la Base de Datos:
  + Para cada rostro analizado, se insertan los datos de emoción, género y marca de tiempo en una     tabla de la base de datos.
# Visualización del Marco Resultante:
  + Se muestra el marco resultante con los rectángulos dibujados alrededor de los rostros y la     
    información de emoción y género.
### Finalización del Programa:
  + El programa se ejecuta hasta que se presiona la tecla 'q' para salir.
  + Se liberan los recursos de la captura de video y se cierran todas las ventanas.

## Creación de la base de datos
  + El script Python proporcionado realiza varias operaciones relacionadas con la manipulación de     una base de datos SQL Server llamada "EMOTIONS" y dos de sus tablas: "Emotions" y "Workers". 
  + Aquí hay una descripción de lo que hace cada parte del código:

### Conexión a la Base de Datos:
  + Se establece una conexión con el servidor SQL utilizando pyodbc.connect.
  + Se imprime un mensaje de confirmación si la conexión es exitosa.
### Creación de la Base de Datos y Tablas:
  + Se ejecutan consultas SQL para crear la base de datos "EMOTIONS" y la tabla "Emotions" si no     existen.
  + La tabla "Emotions" tiene las columnas "ID" (identificador único), "Emotion" (emoción     
   detectada), "Gender" (género detectado) y "CreatedAt" (marca de tiempo de creación).
  + Se verifica si la tabla "Workers" ya existe antes de crearla, y si no existe, se crea con las     columnas "TrabajadorID" y "Nombre".
### Inserción de Datos en la Tabla "Workers":
  + Se insertan datos en la tabla "Workers" utilizando el método executemany.
  + Cada fila insertada contiene un ID de trabajador y un nombre correspondiente.
### Confirmación de Cambios:
  + Se confirman los cambios en la base de datos utilizando conn.commit().
