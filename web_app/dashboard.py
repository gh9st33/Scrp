```python
from flask import Flask, render_template, session
from flask_login import login_required
from .database_connection import get_db

app = Flask(__name__)

@app.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    active_tasks = db.execute(
        'SELECT * FROM tasks WHERE status = ?', ('active',)
    ).fetchall()
    completed_tasks = db.execute(
        'SELECT * FROM tasks WHERE status = ?', ('completed',)
    ).fetchall()

    return render_template('dashboard.html', active_tasks=active_tasks, completed_tasks=completed_tasks)

@app.route('/task/<int:id>')
@login_required
def task(id):
    db = get_db()
    task = db.execute(
        'SELECT * FROM tasks WHERE id = ?', (id,)
    ).fetchone()

    if task is None:
        abort(404, "Task id {0} doesn't exist.".format(id))

    return render_template('task.html', task=task)
```