```python
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Task

data_view = Blueprint('data_view', __name__)

@data_view.route('/data', methods=['GET'])
@login_required
def view_data():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('data_view.html', tasks=tasks)

@data_view.route('/data/download/<task_id>', methods=['GET'])
@login_required
def download_data(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        # Assuming data is stored in a CSV file
        return send_file(task.data_path, as_attachment=True)
    else:
        flash('No such task found or you do not have permission to access this task.')
        return redirect(url_for('data_view.view_data'))
```