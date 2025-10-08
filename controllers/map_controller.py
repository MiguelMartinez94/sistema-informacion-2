# controllers/map_controller.py

from flask import Blueprint, render_template, request, redirect, url_for
from models.mapa_model import crear_mapa_y_municipios, get_mapa_por_id, get_municipios_con_contenido, actualizar_contenido_municipio
from app import mysql
import os

# Blueprint para los mapas
map_bp = Blueprint('mapas', __name__, url_prefix='/mapas')

@map_bp.route('/crear', methods=['GET', 'POST'])
def vista_crear_mapa():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        
        nuevo_id_mapa = crear_mapa_y_municipios(nombre, descripcion)
        
        return redirect(url_for('mapas.vista_creando_mapa', id_mapa=nuevo_id_mapa))

    return render_template('crear_mapa.html')

@map_bp.route('/editando/<int:id_mapa>')
def vista_creando_mapa(id_mapa):
    mapa_info = get_mapa_por_id(id_mapa)
    municipios_info = get_municipios_con_contenido(id_mapa)
    
    return render_template('creando_mapa.html', mapa=mapa_info, municipios=municipios_info)

# --- INICIO DE LA FUNCIÓN QUE FALTABA ---
@map_bp.route('/municipio/guardar', methods=['POST'])
def guardar_contenido_municipio():
    """
    Recibe los datos del formulario de edición de un municipio y los guarda.
    """
    id_municipio = request.form['id_municipio']
    color = request.form['color']
    detalle = request.form['detalle']
    imagen = request.files.get('imagen')

    nombre_imagen = None
    if imagen and imagen.filename != '':
        nombre_imagen = imagen.filename
        # Asegúrate de tener una carpeta 'uploads' dentro de 'static'
        # Si no existe, créala manualmente.
        if not os.path.exists('static/uploads'):
            os.makedirs('static/uploads')
        imagen.save(os.path.join('static/uploads', nombre_imagen))

    actualizar_contenido_municipio(id_municipio, color, detalle, nombre_imagen)

    # Obtenemos el id_mapa para poder redirigir de vuelta a la misma página
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT id_mapa FROM Municipios WHERE id_municipio = %s", (id_municipio,))
    municipio = cursor.fetchone()
    cursor.close()

    return redirect(url_for('mapas.vista_creando_mapa', id_mapa=municipio['id_mapa']))
# --- FIN DE LA FUNCIÓN QUE FALTABA ---