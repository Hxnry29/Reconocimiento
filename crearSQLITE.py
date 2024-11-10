#pip install opencv-python
#pip install deepface

import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('registro.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla Emotions si no existe (incluyendo la columna Age)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Emotions (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Emotion TEXT,
        Gender TEXT,
        Age INTEGER,  -- Agregar la columna Age
        CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Confirmar los cambios
conn.commit()

# Crear la tabla Workers si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Workers (
        TrabajadorID INTEGER PRIMARY KEY,
        Nombre TEXT
    )
''')

# Insertar datos en la tabla Workers
cursor.executemany('''
    INSERT INTO Workers (TrabajadorID, Nombre) VALUES (?, ?)
''', [
    (1, 'Alfredo'),
    (2, 'Ana'),
    (3, 'Juan'),
    (4, 'María'),
    (5, 'Pedro'),
    (6, 'Laura'),
    (7, 'David'),
    (8, 'Sofía'),
    (9, 'Alejandro'),
    (10, 'Elena')
])

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Tablas creadas, datos insertados correctamente.")
