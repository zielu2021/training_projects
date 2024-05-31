from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db, Project, UserProject
from functools import wraps

resources_bp = Blueprint('resources', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@resources_bp.route('/projects', methods=['GET'])
@login_required
def get_projects():
    page = int(request.args.get('page', 1))
    per_page = 5
    projects = Project.query.paginate(page, per_page, False)
    if current_user.is_admin:
        user_projects = [project.id for project in projects.items]
    else:
        user_projects = [p.project_id for p in UserProject.query.filter_by(user_id=current_user.id).all()]
    return render_template('projects.html', projects=projects, user_projects=user_projects)

@resources_bp.route('/projects/<int:project_id>', methods=['GET'])
@login_required
def view_project(project_id):
    if not current_user.is_admin:
        user_project = UserProject.query.filter_by(user_id=current_user.id, project_id=project_id).first()
        if not user_project:
            flash('You do not have permission to view this project', 'danger')
            return redirect(url_for('resources.get_projects'))
    
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@resources_bp.route('/projects/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_project():
    if request.method == 'POST':
        project_name = request.form['name']
        new_project = Project(name=project_name)
        db.session.add(new_project)
        db.session.commit()
        flash('Project created successfully', 'success')
        return redirect(url_for('resources.get_projects'))
    return render_template('new_project.html')

@resources_bp.route('/projects/seed', methods=['GET'])
def seed_projects():
    for i in range(1, 16):
        project_name = f'xyz{i}'
        new_project = Project(name=project_name)
        db.session.add(new_project)
    db.session.commit()
    return '15 projects created successfully.'
