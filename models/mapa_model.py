# models/mapa_model.py

from app import mysql

# --- FUNCIÓN MODIFICADA ---
def crear_mapa_y_municipios(nombre, descripcion):
    """
    Inserta un nuevo mapa y, acto seguido, crea los 18 registros de 
    municipios asociados a ese nuevo mapa.
    """
    try:
        cursor = mysql.connection.cursor()
        
        # 1. Insertar el registro en la tabla 'Mapas'
        sql_mapa = "INSERT INTO Mapas (nombre, descripcion) VALUES (%s, %s)"
        cursor.execute(sql_mapa, (nombre, descripcion))
        id_nuevo_mapa = cursor.lastrowid
        
        # 2. Lista de los 18 municipios a crear
        nombres_municipios = [
            "Amealco de Bonfil", "Pinal de Amoles", "Arroyo Seco", "Cadereyta de Montes", 
            "Colón", "Corregidora", "Ezequiel Montes", "Huimilpan", "Jalpan de Serra", 
            "Landa de Matamoros", "El Marqués", "Pedro Escobedo", "Peñamiller", 
            "Querétaro", "San Joaquín", "San Juan del Río", "Tequisquiapan", "Tolimán"
        ]
        
        # 3. Insertar los 18 registros en la tabla 'Municipios'
        sql_municipio = "INSERT INTO Municipios (nombre, id_mapa) VALUES (%s, %s)"
        datos_municipios = [(nombre_mun, id_nuevo_mapa) for nombre_mun in nombres_municipios]
            
        cursor.executemany(sql_municipio, datos_municipios)
        
        mysql.connection.commit()
        cursor.close()
        return id_nuevo_mapa

    except Exception as e:
        mysql.connection.rollback()
        print(f"Error al crear mapa y municipios: {e}")
        return None

# --- NUEVA FUNCIÓN AÑADIDA ---
def get_mapa_por_id(id_mapa):
    """
    Obtiene los datos de un mapa específico usando su ID.
    """
    try:
        # Usamos dictionary=True para poder acceder a los datos por nombre (ej: mapa['nombre'])
        cursor = mysql.connection.cursor(dictionary=True) 
        sql = "SELECT * FROM Mapas WHERE id_mapa = %s"
        cursor.execute(sql, (id_mapa,))
        mapa = cursor.fetchone()
        cursor.close()
        return mapa
    except Exception as e:
        print(f"Error al obtener el mapa por ID: {e}")
        return None