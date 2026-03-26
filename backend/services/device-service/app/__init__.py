from flask import Flask

def create_app():
    app = Flask("device_service")

    from .routes import device_bp
    app.register_blueprint(device_bp)

    return app
