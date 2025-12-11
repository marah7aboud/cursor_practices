# Random Number Generator API

A clean, modular FastAPI application that generates random numbers with no range limits.

## Features

- ✅ **Random Number Generation**: Generate random numbers with no range limits
- ✅ **Swagger UI**: Automatic API documentation at `/docs`
- ✅ **ReDoc**: Alternative API documentation at `/redoc`
- ✅ **Clean Architecture**: Modular, DRY code following best practices
- ✅ **Environment Configuration**: Easy port configuration via `.env` file
- ✅ **Type Safety**: Full type hints and Pydantic validation
- ✅ **Well Documented**: Comprehensive comments and docstrings

## Quick Start

### 1. Install Dependencies

```bash
pip install -e .
```

### 2. Configure Port (Optional)

Edit the `.env` file to change the port (default is 8000):

```env
PORT=8000
```

### 3. Run the Application

```bash
python run.py
```

### 4. Access the API

- **API Base URL**: `http://localhost:8000`
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Random Number Endpoint**: `http://localhost:8000/random`

## API Endpoints

### GET `/random`

Generate a random number with no range limits.

**Response:**
```json
{
  "number": 42.123456,
  "message": "Random number generated successfully"
}
```

### GET `/`

Get API information and available endpoints.

### GET `/health`

Health check endpoint for monitoring.

## Project Structure

```
cursor_practices/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── random_number.py  # Random number endpoint
│   ├── services/
│   │   ├── __init__.py
│   │   └── random_service.py     # Business logic
│   └── schemas/
│       ├── __init__.py
│       └── responses.py           # Response models
├── docs/
│   └── IMPLEMENTATION_STEPS.md    # Implementation documentation
├── run.py                   # Entry point (renamed from app.py to avoid conflict with app/ package)
├── .env                     # Environment configuration
├── pyproject.toml          # Dependencies
└── README.md               # This file
```

## Documentation

For detailed implementation steps and architecture decisions, see:
- [Implementation Steps](docs/IMPLEMENTATION_STEPS.md)

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **python-dotenv**: Environment variable management
- **Pydantic**: Data validation using Python type annotations

## Development

The application uses:
- **Python 3.13+**
- **FastAPI** for the web framework
- **Uvicorn** with auto-reload for development
- **Pydantic** for data validation

## License

This is a practice project for learning FastAPI and clean code principles.

