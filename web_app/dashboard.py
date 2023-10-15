```python
from flask import Flask, render_template, request, jsonify
from flask_login import login_required, current_user
from .user_auth import User
from .database import db_session, init_db
from .api import get_all_tasks, get_task_status

app = Flask(__name__)

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    user = User.query.filter_by(email=current_user.email).first()
    if user is None:
        return jsonify({'message': 'No user found!'}), 404

    tasks = get_all_tasks(user.id)
    task_statuses = [get_task_status(task.id) for task in tasks]

    return render_template('dashboard.html', tasks=tasks, task_statuses=task_statuses)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run()
```