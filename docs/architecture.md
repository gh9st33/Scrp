# Architecture

Our Distributed Scraper Management Framework & Web App is designed to be robust, scalable, and capable of managing multiple web scrapers. The architecture is divided into two main parts: the Framework and the Web App.

## Framework

The Framework is responsible for managing the scraper tasks. It is designed with a distributed architecture, allowing scraper tasks to be distributed across multiple servers or nodes. The main components of the Framework are:

- **Scraper Manager (`scraper_manager.py`)**: This is the main component that manages the scraper tasks. It interacts with the Task Queue, Scheduler, API, Error Handler, and Data Storage components.

- **Task Queue (`task_queue.py`)**: This component holds the tasks that need to be executed. It uses RabbitMQ, Kafka, or Redis as the queuing mechanism.

- **Scheduler (`scheduler.py`)**: This component is responsible for the automated timing of scraper deployment. It uses Cron or Celery for Python.

- **API (`api.py`)**: This component provides a RESTful API to interact programmatically with the system. It uses Flask for Python, Express for Node.js, or Gin for Go.

- **Error Handler (`error_handler.py`)**: This component provides effective logging and alert mechanisms for scraper errors or failures.

- **Data Storage (`data_storage.py`)**: This component provides flexible storage solutions to accommodate both structured data (like JSON, CSV) and unstructured data (like images). It uses PostgreSQL or MongoDB as the database.

## Web App

The Web App provides a user interface for deploying, monitoring, and retrieving data from the scraper tasks. The main components of the Web App are:

- **User Authentication (`authentication.py`)**: This component provides secure login and user management. It uses JWT or OAuth 2.0 for authentication.

- **Dashboard (`dashboard.py`)**: This component provides a real-time overview of all active and completed scraper tasks.

- **Deploy Scrapers (`deploy_scrapers.py`)**: This component provides a user interface for deploying new scraper tasks.

- **Data Viewing (`data_viewer.py`)**: This component provides a simple yet effective way to view and download scraped data and images.

- **Logs and Metrics (`logs_metrics.py`)**: This component allows users to view logs and performance metrics of the scrapers.

- **Node Editor (`node_editor.py`)**: This component allows users to design scrapers with a node editor.

- **Scraper Designer (`scraper_designer.py`)**: This component allows users to create, modify, and update distributed scrapers remotely from within the editor.

- **SSH Deployer (`ssh_deployer.py`)**: This component allows automatic deployment of scraper agents via SSH to install and run them on Ubuntu and Debian servers.

- **Scraper Updater (`scraper_updater.py`)**: This component allows users to update the scrapers remotely.

- **Scraper Creator (`scraper_creator.py`)**: This component allows users to create new scrapers remotely.

The Web App uses the same language, database, and API framework as the Framework. The front-end of the Web App is built with React or Angular.

## Tests

The system includes unit tests (`unit_tests.py`) and integration tests (`integration_tests.py`) to ensure its reliability.

## Documentation

The system includes documentation explaining the architecture (`architecture.md`), setup instructions (`setup_instructions.md`), and API endpoints (`api_endpoints.md`).