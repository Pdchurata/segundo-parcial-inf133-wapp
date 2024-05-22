from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from app.models.user_model import User
    from app.controllers.user_controller import user_bp
    from app.controllers.patient_controller import patient_bp

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

        app.register_blueprint(user_bp)
        app.register_blueprint(patient_bp)

    return app
