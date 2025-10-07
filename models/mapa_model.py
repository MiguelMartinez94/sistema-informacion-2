# models/mapa_model.py

def crear_mapa(db, nombre, descripcion):
    """
    Inserta un nuevo mapa en la tabla 'Mapas'.
    
    Args:
        db: Objeto de conexión a la base de datos.
        nombre (str): El nombre del mapa.
        descripcion (str): La descripción del mapa.
        
    Returns:
        int: El ID del nuevo mapa insertado, o None si falla.
    """
    cursor = db.cursor()
    try:
        sql = "INSERT INTO Mapas (nombre, descripcion) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, descripcion))
        db.commit()
        
        # Retorna el ID del último registro insertado
        return cursor.lastrowid
    except Exception as e:
        db.rollback() # Revierte la transacción si hay un error
        print(f"Error al insertar en la base de datos: {e}")
        return None
    finally:
        cursor.close()