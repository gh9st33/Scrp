```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import user_auth
import dashboard
import deploy_scrapers
import data_view
import logs_metrics

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Distributed Scraper Management Web App!"

@app.route('/login', methods=['POST'])
def login():
    return user_auth.login(request)

@app.route('/register', methods=['POST'])
def register():
    return user_auth.register(request)

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    return dashboard.get_dashboard()

@app.route('/deploy_scraper', methods=['POST'])
def deploy_scraper():
    return deploy_scrapers.deploy_scraper(request)

@app.route('/data', methods=['GET'])
def view_data():
    return data_view.view_data(request)

@app.route('/logs', methods=['GET'])
def view_logs():
    return logs_metrics.view_logs(request)

@app.route('/metrics', methods=['GET'])
def view_metrics():
    return logs_metrics.view_metrics(request)

if __name__ == '__main__':
    app.run(debug=True)
```