# Sample API - FastAPI Authentication System

This is a FastAPI application with user registration, login, and protected endpoints using SQLite database.

## Features

- **User Registration** - Create new user accounts with name, email, password, and phone
- **User Login** - Authenticate users and receive JWT tokens
- **Protected Route** - Access `/users` endpoint with authentication
- **SQLite Database** - Persistent storage for user data
- **Password Security** - Bcrypt password hashing
- **JWT Authentication** - Token-based authentication

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Register a New User
**POST** `/register`

Request body:
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "phone": "1234567890"
}
```

### 2. Login
**POST** `/login`

Request body:
```json
{
    "email": "john@example.com",
    "password": "securepassword123"
}
```

Response:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

### 3. Get Users (Protected)
**GET** `/users`

Headers:
```
Authorization: Bearer <your_access_token>
```

Response:
```json
[
    {
        "name": "John Doe",
        "phone": "1234567890",
        "email": "john@example.com"
    }
]
```

## Testing the API

You can test the API using:
- **Swagger UI**: Navigate to `http://localhost:8000/docs`
- **ReDoc**: Navigate to `http://localhost:8000/redoc`
- **cURL or Postman**: Use the endpoints above

### Example Flow:

1. Register a user at `/register`
2. Login at `/login` to get an access token
3. Use the token in the Authorization header to access `/users`

## Project Structure

```
sample-api/
├── main.py           # FastAPI application and endpoints
├── models.py         # SQLAlchemy database models
├── auth.py           # Authentication utilities (password hashing, JWT)
├── requirements.txt  # Python dependencies
└── users.db          # SQLite database (created automatically)
```

## Security Notes

⚠️ **Important**: Change the `SECRET_KEY` in `auth.py` before deploying to production!
