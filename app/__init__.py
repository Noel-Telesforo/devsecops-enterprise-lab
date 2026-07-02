from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configuración
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

    # Registrar rutas
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
