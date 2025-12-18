# Location Tracker API

A REST API for tracking user locations, implemented in multiple programming stacks: FastAPI (Python), Flask (Python), Node.js/Express, and Rust/Actix. All implementations provide the same functionality.

## Table of Contents
1. [Features](#features)
2. [API Endpoints](#api-endpoints)
3. [Implementations](#implementations)
4. [Installation & Running](#installation--running)
5. [Database](#database)
6. [Technologies](#technologies)
7. [Project Structure](#project-structure)
8. [How to Contribute](#how-to-contribute)

## Features

- **Multi-Stack Implementations**: Choose from Python (FastAPI/Flask), JavaScript (Node/Express), or Rust (Actix).
- **Database Persistence**: SQLite database for storing location data.
- **RESTful API**: Standard HTTP methods for location management.
- **Docker Support**: Run any implementation with Docker Compose.
- **OpenAPI Specification**: API documentation in `openapi.yaml`.

## API Endpoints

### Add Location
- **POST** `/locations`
- Body: `{"user_id": "string", "latitude": float, "longitude": float}`
- Response: `{"status": "stored"}`

### Get Latest Locations
- **GET** `/locations`
- Returns latest location for each user.

### Get User's Latest Location
- **GET** `/locations/{user_id}`
- Returns the most recent location for the specified user.

### Get User's Location History
- **GET** `/locations/{user_id}/history`
- Returns all locations for the user, ordered by timestamp.

Example using `curl`:
```bash
curl -X POST \
  http://localhost:8000/locations \
  -H "Content-Type: application/json" \
  -d '{"user_id": "1234", "latitude": -1.2833, "longitude": 36.8167}'
```

## Implementations

### FastAPI (Python)
- Port: 8000
- Dependencies: `fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`
- Run: `cd fastapi && uvicorn main:app --reload`

### Flask (Python)
- Port: 5000
- Run: `cd flask && python app.py`

### Node.js/Express
- Port: 3000
- Dependencies: See `node_express/package.json`
- Run: `cd node_express && npm install && npm start`

### Rust/Actix
- Port: 8080
- Run: `cd rust_actix && cargo run`

## Installation & Running

### Using Docker (Recommended)
```bash
docker-compose up --build
```
This will start all four implementations on their respective ports.

### Manual Setup
1. Choose an implementation directory.
2. Install dependencies (see requirements.txt or package.json).
3. Run the application as described above.

## Database
- Uses SQLite (`locations.db`).
- Tables created automatically on startup.
- Location table: `id`, `user_id`, `latitude`, `longitude`, `timestamp`.

## Technologies
- **FastAPI**: Modern Python web framework.
- **Flask**: Lightweight Python web framework.
- **Express.js**: Node.js web application framework.
- **Actix**: Rust actor framework for web services.
- **SQLAlchemy**: Python ORM for database operations.
- **SQLite**: Embedded database.
- **Docker**: Containerization.

## Project Structure
```
├── fastapi/          # FastAPI implementation
├── flask/            # Flask implementation
├── node_express/     # Node.js/Express implementation
├── rust_actix/       # Rust/Actix implementation
├── docker-compose.yml # Docker orchestration
├── openapi.yaml      # API specification
└── README.md         # This file
```

## How to Contribute

We welcome contributions! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

For more details, view our [Contributor Guide Document](https://docs.google.com/document/d/1gQFiD9HNCgo9PDGuLMrg6Wi-cfHfnB3IwXCtZ6SyPTg/edit?usp=sharing).