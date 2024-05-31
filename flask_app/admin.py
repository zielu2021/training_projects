from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_required, current_user
from models import db, User, Project, UserProject
from functools import wraps

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/projects')
@login_required
@admin_required
def manage_projects():
    projects = Project.query.all()
    return render_template('manage_projects.html', projects=projects)

@admin_bp.route('/projects/<int:project_id>')
@login_required
@admin_required
def manage_project_users(project_id):
    project = Project.query.get_or_404(project_id)
    assigned_users = User.query.join(UserProject).filter(UserProject.project_id == project_id).all()
    all_users = User.query.all()
    return render_template('manage_project_users.html', project=project, assigned_users=assigned_users, all_users=all_users)

@admin_bp.route('/projects/<int:project_id>/assign', methods=['POST'])
@login_required
@admin_required
def assign_user(project_id):
    user_id = request.form.get('user_id')
    if user_id:
        user_project = UserProject(user_id=user_id, project_id=project_id)
        db.session.add(user_project)
        db.session.commit()
        flash('User assigned to project successfully', 'success')
    return redirect(url_for('admin.manage_project_users', project_id=project_id))

@admin_bp.route('/projects/<int:project_id>/remove', methods=['POST'])
@login_required
@admin_required
def remove_user(project_id):
    user_id = request.form.get('user_id')
    if user_id:
        user_project = UserProject.query.filter_by(user_id=user_id, project_id=project_id).first()
        db.session.delete(user_project)
        db.session.commit()
        flash('User removed from project successfully', 'success')
    return redirect(url_for('admin.manage_project_users', project_id=project_id))
