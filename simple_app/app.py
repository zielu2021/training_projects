from flask import Flask, render_template, session, redirect, url_for, request, jsonify, flash
from config import Config
from auth import auth_bp
from resources import resources_bp
from admin import admin_bp
from models import db, User, Project, UserProject
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(resources_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/admin')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    # user = current_user if current_user.is_authenticated else None
    # # return f'Hello, {user.email}!' if user else 'Hello, World!'
    return render_template('index.html')
import os

directory = os.path.join('static', 'profile_pics')
if not os.path.exists(directory):
    os.makedirs(directory)
    
if __name__ == '__main__':
    app.run(debug=True)
