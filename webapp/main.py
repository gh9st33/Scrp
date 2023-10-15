```python
from flask import Flask, render_template
from flask_cors import CORS
from user_auth import auth_blueprint
from dashboard import dashboard_blueprint
from deploy_scrapers import deploy_blueprint
from data_view import data_view_blueprint
from logs_metrics import logs_metrics_blueprint

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(deploy_blueprint)
app.register_blueprint(data_view_blueprint)
app.register_blueprint(logs_metrics_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```