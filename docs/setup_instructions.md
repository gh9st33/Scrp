# Setup Instructions

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- Node.js 12 or higher
- PostgreSQL 12 or higher
- RabbitMQ 3.8 or higher
- Scrapy 2.4 or higher
- Scrapyd 1.2 or higher

## Framework Setup

1. Clone the repository:

```bash
git clone https://github.com/your-repo/distributed-scraper-framework.git
cd distributed-scraper-framework
```

2. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the PostgreSQL database:

```bash
createdb scraper_db
psql -d scraper_db -f framework/db/schema.sql
```

4. Start the RabbitMQ server:

```bash
rabbitmq-server start
```

5. Start the framework:

```bash
python framework/main.py
```

## Web App Setup

1. Navigate to the web app directory:

```bash
cd web_app
```

2. Install the Node.js dependencies:

```bash
npm install
```

3. Start the web app:

```bash
npm start
```

## Scrapy and Scrapyd Setup

1. Install Scrapy and Scrapyd:

```bash
pip install scrapy scrapyd
```

2. Start the Scrapyd server:

```bash
scrapyd
```

## SSH Deployment Setup

1. Generate an SSH key pair:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

2. Copy the public key to the remote server:

```bash
ssh-copy-id user@remote-server
```

3. Test the SSH connection:

```bash
ssh user@remote-server
```

## Node Editor Setup

The node editor is part of the web app and does not require additional setup.

## Running Tests

1. Navigate to the tests directory:

```bash
cd tests
```

2. Run the tests:

```bash
python framework_tests.py
python web_app_tests.py
```

## Accessing the Web App

Open your web browser and navigate to `http://localhost:3000`.

## API Usage

Refer to the `docs/api_endpoints.md` file for information on how to use the API.