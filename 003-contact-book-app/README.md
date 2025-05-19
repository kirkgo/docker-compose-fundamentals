# Contact Book API

A simple contact book application with CRUD operations built using FastAPI, MySQL, and Docker Compose.

## Overview

This project demonstrates how to build a containerized FastAPI application that performs CRUD operations on a MySQL database, with Adminer for database administration. It uses Docker Compose to orchestrate all the services.

The Contact Book allows you to:
- Create, read, update, and delete contacts
- Store name, address, phone number, and email for each contact
- Manage the database through Adminer
- Deploy everything with a single Docker Compose command

## Project Structure

```
contact-book-app/
├── docker-compose.yml
├── .env
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── schemas.py
│   │   └── crud.py
└── mysql/
    └── init.sql
```

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation & Setup

1. Clone this repository
   ```bash
   git clone https://github.com/kirkgo/docker-compose-fundamentals.git
   cd contact-book-app
   ```

2. Create a `.env` file in the root directory with the following content:
   ```
   MYSQL_ROOT_PASSWORD=rootpassword
   MYSQL_DATABASE=contactbook
   MYSQL_USER=appuser
   MYSQL_PASSWORD=apppassword
   ```

3. Start the application with Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. The application should now be running at:
   - API: [http://localhost:8000](http://localhost:8000)
   - API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Adminer (Database Management): [http://localhost:8080](http://localhost:8080)

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Welcome message |
| GET | `/contacts/` | List all contacts |
| GET | `/contacts/{contact_id}` | Get a specific contact |
| POST | `/contacts/` | Create a new contact |
| PUT | `/contacts/{contact_id}` | Update an existing contact |
| DELETE | `/contacts/{contact_id}` | Delete a contact |

## Example Requests

### Create a Contact

```bash
curl -X 'POST' \
  'http://localhost:8000/contacts/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Jose Maria",
  "address": "Rua do Porto, 120",
  "phone": "9103-0978",
  "email": "jose@example.com"
}'
```

### Get All Contacts

```bash
curl -X 'GET' 'http://localhost:8000/contacts/'
```

### Get a Specific Contact

```bash
curl -X 'GET' 'http://localhost:8000/contacts/1'
```

### Update a Contact

```bash
curl -X 'PUT' \
  'http://localhost:8000/contacts/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "address": "Rua do Porto, 120"
}'
```

### Delete a Contact

```bash
curl -X 'DELETE' 'http://localhost:8000/contacts/1'
```

## Using Adminer

Adminer is included to provide a web interface for database management:

1. Open [http://localhost:8080](http://localhost:8080) in your browser
2. Use the following login information:
   - System: MySQL
   - Server: db
   - Username: appuser (or root)
   - Password: apppassword (or rootpassword for root)
   - Database: contactbook

## File Descriptions

### docker-compose.yml

This file defines and configures the three services:
- `backend`: The FastAPI application
- `db`: MySQL database
- `adminer`: Web-based database management tool

### .env

Contains environment variables for configuring the MySQL database.

### backend/Dockerfile

Defines how to build the FastAPI application container.

### backend/requirements.txt

Lists all Python dependencies for the FastAPI application.

### backend/app/database.py

Handles database connection and session management. Includes retry logic to handle database startup timing issues.

### backend/app/models.py

Defines the SQLAlchemy models (database tables).

### backend/app/schemas.py

Defines the Pydantic models for request/response validation.

### backend/app/crud.py

Contains all the CRUD (Create, Read, Update, Delete) operations.

### backend/app/main.py

The main FastAPI application file with all route definitions.

### mysql/init.sql

SQL script to initialize the database with tables and sample data.

## Common Issues & Solutions

### Connection Refused Error

If the FastAPI container can't connect to the MySQL container, it's usually because MySQL hasn't fully initialized yet. The current implementation includes retry logic in `database.py` to handle this.

If you still encounter issues:

1. Check the logs:
   ```bash
   docker-compose logs -f
   ```

2. Ensure all containers are running:
   ```bash
   docker-compose ps
   ```

3. Try restarting the backend service:
   ```bash
   docker-compose restart backend
   ```

### MySQL Data Persistence

If you need to keep your data after stopping containers:

1. Make sure you don't use the `-v` flag when stopping:
   ```bash
   # This keeps volumes intact
   docker-compose down
   
   # This would delete the volumes
   docker-compose down -v
   ```

## Extending the Application

Some ideas for extending this project:

1. Add authentication
2. Implement contact categories or groups
3. Add search functionality
4. Create a web frontend (React, Vue, etc.)
5. Add file attachments for contacts
6. Implement contact import/export features

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| MYSQL_ROOT_PASSWORD | MySQL root password | rootpassword |
| MYSQL_DATABASE | Database name | contactbook |
| MYSQL_USER | Database username | appuser |
| MYSQL_PASSWORD | Database password | apppassword |
| DATABASE_URL | SQLAlchemy connection string | mysql+pymysql://appuser:apppassword@db:3306/contactbook |

## Technology Stack

- **FastAPI**: Modern, high-performance Python web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation and settings management
- **MySQL**: Relational database
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Adminer**: Database management

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [MySQL](https://www.mysql.com/)
- [Adminer](https://www.adminer.org/)
