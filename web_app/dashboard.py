```python
from flask import Blueprint, render_template
from flask_login import login_required

from .models import Task

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def dashboard():
    tasks = Task.query.all()
    return render_template('dashboard.html', tasks=tasks)
```