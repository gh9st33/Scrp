# API Endpoints

This document outlines the API endpoints used in the Distributed Scraper Management Framework & Web App.

## User Authentication

- **POST /api/auth/login**
  - Description: Authenticate a user and return a JWT token.
  - Request Body: `{ "username": "<username>", "password": "<password>" }`
  - Response: `{ "token": "<JWT token>" }`

- **POST /api/auth/logout**
  - Description: Invalidate a user's JWT token.
  - Request Body: None
  - Response: `{ "message": "Logged out successfully" }`

## Scraper Management

- **POST /api/scrapers**
  - Description: Deploy a new scraper task.
  - Request Body: `{ "scraper_config": "<scraper configuration>" }`
  - Response: `{ "task_id": "<task id>" }`

- **GET /api/scrapers**
  - Description: Get a list of all active and completed scraper tasks.
  - Request Body: None
  - Response: `{ "tasks": "<list of tasks>" }`

- **GET /api/scrapers/:id**
  - Description: Get details of a specific scraper task.
  - Request Body: None
  - Response: `{ "task": "<task details>" }`

- **PUT /api/scrapers/:id**
  - Description: Update a specific scraper task.
  - Request Body: `{ "scraper_config": "<scraper configuration>" }`
  - Response: `{ "task": "<updated task details>" }`

- **DELETE /api/scrapers/:id**
  - Description: Delete a specific scraper task.
  - Request Body: None
  - Response: `{ "message": "Task deleted successfully" }`

## Data Viewing

- **GET /api/data/:id**
  - Description: Get scraped data for a specific task.
  - Request Body: None
  - Response: `{ "data": "<scraped data>" }`

## Logs and Metrics

- **GET /api/logs/:id**
  - Description: Get logs for a specific scraper task.
  - Request Body: None
  - Response: `{ "logs": "<task logs>" }`

- **GET /api/metrics/:id**
  - Description: Get performance metrics for a specific scraper task.
  - Request Body: None
  - Response: `{ "metrics": "<task metrics>" }`

Please note that all requests must be authenticated with a JWT token in the `Authorization` header.