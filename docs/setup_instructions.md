# Setup Instructions

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- Node.js 12 or higher
- PostgreSQL 12 or higher
- RabbitMQ 3.8 or higher
- Scrapy 2.4 or higher
- Scrapyd 1.2 or higher

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/distributed-scraper.git
cd distributed-scraper
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies:

```bash
cd web_app
npm install
```

4. Set up the PostgreSQL database:

```bash
createdb scraper_db
psql scraper_db < db/schema.sql
```

5. Set up RabbitMQ:

```bash
rabbitmqctl add_vhost scraper_vhost
rabbitmqctl add_user scraper_user yourpassword
rabbitmqctl set_permissions -p scraper_vhost scraper_user ".*" ".*" ".*"
```

## Configuration

1. Update the `framework/config.py` and `web_app/config.js` files with your database and RabbitMQ credentials.

2. Update the `web_app/.env` file with your JWT secret key.

## Running the Application

1. Start the scraper manager:

```bash
cd framework
python scraper_manager.py
```

2. Start the web app:

```bash
cd web_app
npm start
```

3. The web app will be accessible at `http://localhost:3000`.

## Deploying Scrapers

1. Use the web app's Deploy Scrapers UI to deploy new scraper tasks.

2. Use the Node Editor to design new scrapers and deploy them via SSH to your Ubuntu or Debian servers.

## Updating Scrapers

1. Use the web app's Scraper Updater UI to modify and update your distributed scrapers remotely.

## Viewing Data

1. Use the web app's Data Viewer UI to view and download scraped data and images.

## Monitoring

1. Use the web app's Dashboard to monitor all active and completed scraper tasks.

2. Use the web app's Logs and Metrics UI to view logs and performance metrics of the scrapers.