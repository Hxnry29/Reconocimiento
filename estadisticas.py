import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos SQLite
conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

# Consultar los datos de la base de datos
query = "SELECT Emotion, Gender, Age FROM EMOTIONS"
cursor.execute(query)
rows = cursor.fetchall()

# Convertir los datos en un DataFrame de pandas para su fácil manipulación
df = pd.DataFrame(rows, columns=['Emotion', 'Gender', 'Age'])

# Cerrar la conexión con la base de datos
conn.close()

# 1. Gráfico de número de personas detectadas
print(f"Total de personas detectadas: {len(df)}")

# 2. Número de hombres y mujeres
gender_count = df['Gender'].value_counts()
print(f"Conteo de géneros:\n{gender_count}")

# Gráfico de barras de géneros
gender_count.plot(kind='bar', color=['blue', 'pink'])
plt.title('Número de hombres y mujeres')
plt.xlabel('Género')
plt.ylabel('Número de personas')
plt.xticks(rotation=0)
plt.show()

# 3. Distribución de frecuencias de la edad
age_distribution = df['Age'].value_counts().sort_index()

# Gráfico de barras de la distribución de edades
age_distribution.plot(kind='bar', color='skyblue')
plt.title('Distribución de frecuencias de la edad')
plt.xlabel('Edad')
plt.ylabel('Número de personas')
plt.show()

# 4. Diagrama de pastel de las emociones
emotion_count = df['Emotion'].value_counts()
print(f"Conteo de emociones:\n{emotion_count}")

# Gráfico de pastel para las emociones
emotion_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Set3')
plt.title('Distribución de emociones')
plt.ylabel('')  # Para quitar la etiqueta del eje y
plt.show()

# 5. Relación entre Edad y Género
plt.figure(figsize=(8, 6))
for gender in df['Gender'].unique():
    subset = df[df['Gender'] == gender]
    plt.scatter(subset['Age'], [gender] * len(subset), label=gender)
    
plt.title('Relación entre Edad y Género')
plt.xlabel('Edad')
plt.ylabel('Género')
plt.legend(title='Género')
plt.show()

# 6. Relación entre Género y Emoción
plt.figure(figsize=(8, 6))
for gender in df['Gender'].unique():
    subset = df[df['Gender'] == gender]
    emotion_counts = subset['Emotion'].value_counts()
    plt.scatter([gender] * len(emotion_counts), emotion_counts.index, s=emotion_counts.values * 10, alpha=0.5, label=gender)
    
plt.title('Relación entre Género y Emoción')
plt.xlabel('Género')
plt.ylabel('Emoción')
plt.legend(title='Género')
plt.show()
