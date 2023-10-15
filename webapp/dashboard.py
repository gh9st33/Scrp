```python
from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .user_auth import User
from .database_connection import db

app = Flask(__name__)

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(email=current_user.email).first()
    tasks = user.tasks.all()
    return render_template('dashboard.html', name=current_user.name, tasks=tasks)

@app.route('/task/<task_id>')
@login_required
def task_detail(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        return render_template('task_detail.html', task=task)
    else:
        return redirect(url_for('dashboard'))

@app.route('/task/<task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('dashboard'))
```