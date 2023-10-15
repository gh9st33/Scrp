```python
import unittest
from flask import url_for
from webapp import create_app, db
from webapp.models import User, ScraperTask

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_dashboard_page(self):
        # create a test user and scraper task
        user = User(username='test', password='test')
        task = ScraperTask(name='test_task', status='active', user=user)
        db.session.add_all([user, task])
        db.session.commit()

        # login as the test user
        response = self.client.post(url_for('auth.login'), data={
            'username': 'test',
            'password': 'test'
        }, follow_redirects=True)

        # navigate to the dashboard
        response = self.client.get(url_for('main.dashboard'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # check if the dashboard displays the correct data
        self.assertTrue('test_task' in response.get_data(as_text=True))
        self.assertTrue('active' in response.get_data(as_text=True))
```