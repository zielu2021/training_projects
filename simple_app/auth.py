from flask import Blueprint, redirect, url_for, request, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from flask_login import login_user, logout_user, login_required, current_user
from config import Config
from authlib.integrations.flask_client import OAuth

auth_bp = Blueprint('auth', __name__)

oauth = OAuth()

google = oauth.register(
    'google',
    client_id=Config.OAUTH_CREDENTIALS['google']['id'],
    client_secret=Config.OAUTH_CREDENTIALS['google']['secret'],
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:5000/auth/login/authorized',
    client_kwargs={'scope': 'email profile'},
)

@auth_bp.route('/login/authorized')
def authorized():
    token = oauth.google.authorize_access_token()
    response = oauth.google.get('userinfo')
    user_info = response.json()
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(email=user_info['email'], password='')
        db.session.add(user)
        db.session.commit()
    login_user(user)
    return redirect(url_for('index'))

@auth_bp.route('/login/google')
def login_google():
    redirect_uri = url_for('auth.authorized', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('auth.login'))
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('This account does not exist. Please register first.', 'danger')
            return redirect(url_for('auth.register'))
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        current_user.bio = request.form['bio']
        if 'profile_picture' in request.files:
            profile_picture = request.files['profile_picture']
            profile_picture_path = f'static/profile_pics/{profile_picture.filename}'
            profile_picture.save(profile_picture_path)
            current_user.profile_picture = profile_picture_path
        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('auth.profile'))
    
    return render_template('profile.html', user=current_user)

@auth_bp.route('/profile/update', methods=['GET', 'POST'])
@login_required
def update_profile():
    return render_template('update_profile.html')

@auth_bp.route('/profile/delete', methods=['POST'])
@login_required
def delete_profile():
    user_id = current_user.id
    logout_user()
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Your account has been deleted', 'info')
    return redirect(url_for('auth.register'))


