from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import Config

# 1. Crea la instancia de MySQL fuera de la función
mysql = MySQL()

def create_app():
    """
    Función 'Application Factory' para crear y configurar la app.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Vincula la instancia de MySQL con la app
    mysql.init_app(app)
    
    # 2. Importa y registra el Blueprint DENTRO de la función
    #    Esto rompe la importación circular.
    from controllers.map_controller import map_bp
    app.register_blueprint(map_bp)

    # --- Rutas Principales y de Error ---
    @app.route('/')
    def index():
        return render_template('vista_principal.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return "<h1>Error 404: La página que buscas no existe.</h1>", 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return "<h1>Error 405: El método HTTP no es permitido para esta ruta.</h1>", 405
        
    return app

# --- Ejecución ---
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)