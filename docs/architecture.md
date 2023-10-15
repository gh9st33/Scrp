# Architecture

Our Distributed Scraper Management Framework & Web App is designed to be robust, scalable, and user-friendly. It is divided into two main components: the Framework and the Web App.

## Framework

The Framework is the backbone of our system, responsible for managing and executing scraper tasks. It is built with a distributed architecture, allowing scraper tasks to be distributed across multiple servers or nodes. This ensures high availability and scalability.

The Framework includes a Task Queue, which holds tasks that need to be executed. This queue is managed by a Scheduler, which automates the timing for scraper deployment.

The Framework also includes a RESTful API, which allows users to interact with the system programmatically. This API is built using Flask for Python, Express for Node.js, or Gin for Go, depending on the chosen language for the Framework.

Error Handling is a crucial part of the Framework. It includes effective logging and alert mechanisms for scraper errors or failures.

Data Storage in the Framework is flexible, accommodating both structured data (like JSON, CSV) and unstructured data (like images). The chosen database is either PostgreSQL or MongoDB.

The Framework also integrates with Scrapy and Scrapyd, and includes a feature for automatic deployment of scraper agents via SSH to Ubuntu and Debian servers.

## Web App

The Web App provides a user-friendly interface for interacting with the Framework. It includes User Authentication, ensuring secure login and user management.

The Dashboard provides a real-time overview of all active and completed scraper tasks. Users can deploy new scraper tasks through the Deploy Scrapers UI.

The Web App also includes a Data Viewing feature, which allows users to view and download scraped data and images. Logs and performance metrics of the scrapers can also be viewed in the Web App.

The Web App is built with React or Angular for the front-end, and uses the same language and database as the Framework for the back-end.

The Web App also includes a Node Editor for designing scrapers, and integrates with the Framework for automatic deployment of scraper agents.

## Shared Dependencies

Both the Framework and the Web App share several dependencies, including database schemas, API endpoints, user authentication methods, scraper definitions, task queue, error handling mechanism, DOM element IDs, message names, function names, SSH deployment feature, Scrapy and Scrapyd integration, and the Node Editor.

These shared dependencies ensure consistency and seamless interaction between the Framework and the Web App.