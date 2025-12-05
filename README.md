# Sample API - FastAPI Authentication System

This is a FastAPI application with login authentication and protected endpoints.

## Features

- **User Login** - Authenticate with username and password to receive JWT tokens
- **Protected Route** - Access `/products` endpoint with authentication
- **JWT Authentication** - Token-based authentication
- **Hardcoded User** - Single user authentication (username: rahul, password: rahul@2021)

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

### 1. Login
**POST** `/login`

Request body:
```json
{
    "username": "rahul",
    "password": "rahul@2021"
}
```

Response:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

### 2. Get Products (Protected)
**GET** `/products`

Headers:
```
Authorization: Bearer <your_access_token>
```

Response:
```json
[
    {
        "productId": "P101",
        "name": "Laptop",
        "price": 55000,
        "inStock": true,
        "category": "Electronics"
    },
    {
        "productId": "P102",
        "name": "Headphones",
        "price": 2500,
        "inStock": false,
        "category": "Accessories"
    },
    {
        "productId": "P103",
        "name": "Smartwatch",
        "price": 9999,
        "inStock": true,
        "category": "Wearables"
    }
]
```

## Testing the API

You can test the API using:
- **Swagger UI**: Navigate to `http://localhost:8000/docs`
- **ReDoc**: Navigate to `http://localhost:8000/redoc`
- **cURL or Postman**: Use the endpoints above

### Example Flow:

1. Login at `/login` with username: `rahul` and password: `rahul@2021` to get an access token
2. Use the token in the Authorization header to access `/products`

## Project Structure

```
sample-api/
├── main.py           # FastAPI application and endpoints
├── models.py         # SQLAlchemy database models (not used for login)
├── auth.py           # Authentication utilities (JWT)
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

## Security Notes

⚠️ **Important**: 
- Change the `SECRET_KEY` in `auth.py` before deploying to production!
- The hardcoded credentials are for development only. Use a proper authentication system in production.
