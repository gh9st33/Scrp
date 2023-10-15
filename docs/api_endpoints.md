# API Endpoints

This document outlines the API endpoints for the Distributed Scraper Management Framework & Web App.

## User Authentication

- `POST /api/auth/login`: Authenticate a user and return a JWT token.
- `POST /api/auth/register`: Register a new user.
- `POST /api/auth/logout`: Invalidate a user's JWT token.

## Dashboard

- `GET /api/dashboard`: Get an overview of all active and completed scraper tasks.

## Deploy Scrapers

- `POST /api/scrapers/deploy`: Deploy a new scraper task.
- `GET /api/scrapers`: Get a list of all deployed scrapers.
- `GET /api/scrapers/{id}`: Get details of a specific scraper.
- `PUT /api/scrapers/{id}`: Update a specific scraper.
- `DELETE /api/scrapers/{id}`: Delete a specific scraper.

## Data Viewing

- `GET /api/data`: Get a list of all scraped data.
- `GET /api/data/{id}`: Get a specific scraped data.
- `POST /api/data/download/{id}`: Download a specific scraped data.

## Logs and Metrics

- `GET /api/logs`: Get a list of all logs.
- `GET /api/logs/{id}`: Get a specific log.
- `GET /api/metrics`: Get performance metrics of the scrapers.

## Node Editor and Scraper Design

- `GET /api/nodes`: Get a list of all nodes in the node editor.
- `POST /api/nodes`: Create a new node in the node editor.
- `PUT /api/nodes/{id}`: Update a specific node in the node editor.
- `DELETE /api/nodes/{id}`: Delete a specific node in the node editor.

## Automatic Deployment

- `POST /api/deployment`: Deploy scraper agents via SSH to install and run them on servers.

Please refer to the API documentation for more details on the request and response formats for each endpoint.