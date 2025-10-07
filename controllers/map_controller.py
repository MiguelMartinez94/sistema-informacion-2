# controllers/map_controller.py

from flask import Blueprint, render_template, request, redirect, url_for
from models.mapa_model import crear_mapa
from config import Config

# Creamos un Blueprint para organizar las rutas relacionadas con los mapas
map_bp = Blueprint('mapas', __name__, url_prefix='/mapas')

@map_bp.route('/mapas/crear', methods=['GET', 'POST'])
def vista_crear_mapa():
    """
    Maneja la lógica para crear un mapa.
    - Si es GET, muestra el formulario.
    - Si es POST, procesa los datos del formulario.
    """
    if request.method == 'POST':
        # Se obtienen los datos del formulario que enviaste
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        
        # Se obtiene la conexión a la base de datos
        db = Config()
        
        # Se llama a la función del modelo para guardar los datos
        crear_mapa(db, nombre, descripcion)
        
        # Se redirige al usuario a la página de inicio
        return redirect(url_for('index'))

    # Si el método es GET, simplemente se muestra la vista para crear
    return render_template('crear_mapa.html')