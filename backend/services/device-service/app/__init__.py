from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import device_bp
    app.register_blueprint(device_bp)

    return app
