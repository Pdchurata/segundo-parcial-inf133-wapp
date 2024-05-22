from flask import Flask
from flask_login import LoginManager
from database import db
from controllers import user_controller
from controllers import patient_controller
from models.user_model import User

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize the database
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(user_controller.user_bp)
app.register_blueprint(patient_controller.patient_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
