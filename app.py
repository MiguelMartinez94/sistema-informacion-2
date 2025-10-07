from flask import Flask, render_template

# --- Creación de la Instancia de la Aplicación ---
app = Flask(__name__)

# --- Registro de Blueprints (Controladores) ---
# Aquí registraremos los controladores cuando los creemos.
# Por ejemplo:
# from controllers.map_controller import map_bp
# app.register_blueprint(map_bp)

from controllers.map_controller import map_bp
app.register_blueprint(map_bp)


# --- Manejadores de Errores ---

# --- Manejadores de Errores Simplificados ---

@app.errorhandler(404)
def page_not_found(error):
    """
    Manejador para el error 404 (Página no encontrada).
    Devuelve un mensaje simple en el navegador.
    """
    return "<h1>Error 404: La página que buscas no existe.</h1>", 404

@app.errorhandler(405)
def method_not_allowed(error):
    """
    Manejador para el error 405 (Método no permitido).
    Devuelve un mensaje simple en el navegador.
    """
    return "<h1>Error 405: El método HTTP no es permitido para esta ruta.</h1>", 405

@app.route('/')
def index():
    return render_template('vista_principal.html')

@app.route('/crear_mapa')
def crear_mapa():
    
    return render_template('crear_mapa.html')

# --- Ejecución de la Aplicación ---

if __name__ == '__main__':
    # Inicia el servidor de Flask en modo de depuración.
    app.run(debug=True)