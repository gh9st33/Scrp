```python
from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required, current_user
from .database_connection import db_connection

data_viewer = Blueprint('data_viewer', __name__)

@data_viewer.route('/view_data', methods=['GET'])
@login_required
def view_data():
    # Get the current user's id
    user_id = current_user.get_id()

    # Query the database for all scraper tasks associated with the current user
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM scraper_tasks WHERE user_id = %s", (user_id,))
    scraper_tasks = cursor.fetchall()

    # Close the database connection
    cursor.close()
    db.close()

    # Render the data viewer page with the scraper tasks
    return render_template('data_viewer.html', scraper_tasks=scraper_tasks)

@data_viewer.route('/download_data/<task_id>', methods=['GET'])
@login_required
def download_data(task_id):
    # Query the database for the scraper task with the given id
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM scraper_tasks WHERE id = %s", (task_id,))
    scraper_task = cursor.fetchone()

    # Check if the scraper task exists and belongs to the current user
    if scraper_task is None or scraper_task['user_id'] != current_user.get_id():
        return redirect(url_for('dashboard'))

    # Get the scraped data associated with the scraper task
    cursor.execute("SELECT * FROM scraped_data WHERE task_id = %s", (task_id,))
    scraped_data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    db.close()

    # Convert the scraped data to a downloadable format (e.g., CSV, JSON)
    # This is a placeholder and should be replaced with actual implementation
    downloadable_data = convert_to_downloadable_format(scraped_data)

    # Send the downloadable data as a response
    return downloadable_data

def convert_to_downloadable_format(scraped_data):
    # This is a placeholder and should be replaced with actual implementation
    return scraped_data
```