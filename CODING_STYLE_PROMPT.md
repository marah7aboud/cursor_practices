# Coding Style Preferences

## Architecture & Design Principles

### 1. Modular Architecture
- **Separation of Concerns**: Strictly separate API routes, business logic (services), and data models (schemas)
- **Layered Architecture**: 
  - `api/routes/` - HTTP endpoint handlers (thin layer, delegates to services)
  - `services/` - Business logic (pure functions, testable, no HTTP concerns)
  - `schemas/` - Pydantic models for request/response validation
- **Single Responsibility**: Each module/function has one clear purpose
- **DRY (Don't Repeat Yourself)**: Centralize reusable logic in service layer

### 2. Project Structure
```
project_root/
├── app/                    # Main application package
│   ├── __init__.py         # Package initialization
│   ├── main.py             # FastAPI app initialization
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/         # API route modules
│   ├── services/           # Business logic layer
│   └── schemas/            # Pydantic models
├── docs/                   # Documentation folder
├── run.py                  # Entry point (avoid naming conflicts with app/)
├── .env                    # Environment configuration
├── pyproject.toml         # Dependencies
└── README.md              # Project documentation
```

### 3. Naming Conventions
- **Avoid Naming Conflicts**: Be extremely careful about file names that conflict with package names (e.g., `app.py` conflicts with `app/` package - use `run.py` instead)
- **Descriptive Names**: Use clear, descriptive names that indicate purpose
- **Module Names**: Use snake_case for files and modules
- **Class Names**: Use PascalCase for classes and Pydantic models
- **Function Names**: Use snake_case for functions

## Documentation Standards

### 1. Module-Level Docstrings
Every module must start with a comprehensive docstring:
```python
"""
Brief description of the module's purpose.

This module contains [detailed explanation of what it does and why].
It's separated from [other layers] to follow clean architecture principles
and make the code more testable and maintainable.
"""
```

### 2. Function Docstrings
Use Google-style or NumPy-style docstrings with:
- Clear description of what the function does
- **Parameters**: Document all parameters (if any)
- **Returns**: Document return type and what it contains
- **Examples**: Include usage examples when helpful
- **Notes**: Explain any important behavior or side effects

Example:
```python
def generate_random_number() -> float:
    """
    Generate a random number with no range limits.
    
    This function uses Python's random module to generate a random float
    between 0.0 and 1.0, then scales it to a larger range to provide
    more variety. The number can be any valid floating-point number.
    
    Returns:
        float: A randomly generated number (no range limits)
    
    Example:
        >>> num = generate_random_number()
        >>> isinstance(num, float)
        True
    """
```

### 3. Inline Comments
- **Explain "Why", Not "What"**: Comments should explain reasoning and context, not just restate what the code does
- **Complex Logic**: Add comments for non-obvious algorithms or business rules
- **Configuration**: Comment configuration choices and their implications
- **Avoid Obvious Comments**: Don't comment self-explanatory code

Good comment example:
```python
# Using string reference "app.main:app" to load the FastAPI instance
# from the app package's main module. This works correctly because
# there's no naming conflict - run.py doesn't interfere with app/ package
```

Bad comment example:
```python
# Get port from environment variable
port = int(os.getenv("PORT", 8000))  # This is obvious, no comment needed
```

### 4. API Documentation
- Use FastAPI's built-in documentation features
- Add comprehensive `description` parameters to endpoints
- Include `summary` for each endpoint
- Use `response_description` for clarity
- Add examples in Pydantic Field definitions

## Code Quality Standards

### 1. Type Hints
- **Mandatory**: Use type hints on all function signatures
- **Return Types**: Always specify return types
- **Pydantic Models**: Use Pydantic models for complex data structures
- **Type Safety**: Leverage type checking for validation

Example:
```python
async def get_random_number() -> RandomNumberResponse:
    """
    GET endpoint to generate a random number.
    
    Returns:
        RandomNumberResponse: Response containing the random number and message
    """
```

### 2. Error Handling
- Plan for error handling structure (ready for extension)
- Use appropriate HTTP status codes
- Provide meaningful error messages
- Consider adding error handling middleware for production

### 3. Configuration Management
- **Environment Variables**: Use `.env` files for configuration
- **Centralized Config**: Load configuration from environment variables
- **Default Values**: Provide sensible defaults
- **Documentation**: Document configuration options

Example:
```python
# Load environment variables from .env file
load_dotenv()

# Get port from environment variable, default to 8000
port = int(os.getenv("PORT", 8000))
```

### 4. FastAPI Best Practices
- Use `APIRouter` for organizing endpoints
- Use Pydantic models for request/response validation
- Leverage FastAPI's automatic OpenAPI/Swagger documentation
- Use tags for organizing endpoints in Swagger UI
- Include health check endpoints

## Implementation Guidelines

### 1. Service Layer Pattern
- Services contain pure business logic
- No HTTP/API concerns in services
- Functions should be testable in isolation
- Services can be reused across different contexts

Example:
```python
def generate_random_number() -> float:
    """
    Generate a random number with no range limits.
    [Implementation details...]
    """
    # Pure business logic, no API dependencies
```

### 2. API Route Pattern
- Routes are thin - they handle HTTP concerns only
- Routes delegate to service layer for business logic
- Routes use Pydantic models for validation
- Routes include comprehensive documentation

Example:
```python
@router.get("/", response_model=RandomNumberResponse)
async def get_random_number() -> RandomNumberResponse:
    """
    GET endpoint to generate a random number.
    """
    # Call the service layer to generate the random number
    random_num = generate_random_number()
    
    # Return the response with the generated number
    return RandomNumberResponse(...)
```

### 3. Pydantic Models
- Use Field descriptions for Swagger documentation
- Include examples in Field definitions
- Use Config class for additional schema customization
- Document all attributes in class docstrings

Example:
```python
class RandomNumberResponse(BaseModel):
    """
    Response model for random number generation endpoint.
    
    Attributes:
        number: The generated random number (can be any valid number)
        message: A descriptive message about the generated number
    """
    
    number: float = Field(
        ...,
        description="The randomly generated number",
        examples=[42.0, 123456.789, -15.5]
    )
```

## Development Workflow

### 1. Planning Before Implementation
- Discuss implementation plan before coding
- Explain design decisions and reasoning
- Consider edge cases and potential issues
- Document architecture decisions

### 2. Incremental Development
- Build in logical steps
- Test each component as you build
- Verify functionality before moving to next step
- Update documentation as you go

### 3. Documentation
- Create implementation documentation in `docs/` folder
- Document step-by-step process
- Explain design decisions and trade-offs
- Include "why" explanations, not just "what"

## Code Review Checklist

When reviewing or writing code, ensure:
- [ ] Modular architecture with clear separation of concerns
- [ ] Comprehensive docstrings on all modules and functions
- [ ] Inline comments explain "why", not "what"
- [ ] Type hints on all function signatures
- [ ] Pydantic models for data validation
- [ ] No naming conflicts (especially file vs package names)
- [ ] Environment-based configuration
- [ ] FastAPI best practices followed
- [ ] Code follows DRY principles
- [ ] Business logic separated from API layer
- [ ] Comprehensive API documentation for Swagger
- [ ] Implementation documentation created

## Key Principles Summary

1. **Clean Architecture**: Separate layers (API, Services, Schemas)
2. **Comprehensive Documentation**: Docstrings, comments, and implementation docs
3. **Type Safety**: Type hints and Pydantic validation everywhere
4. **DRY**: Don't repeat yourself - centralize logic
5. **Modularity**: Each component has single responsibility
6. **Testability**: Business logic isolated and testable
7. **Configuration**: Environment-based, centralized
8. **Best Practices**: Follow framework conventions (FastAPI, Python)
9. **Naming Conflicts**: Be vigilant about avoiding conflicts
10. **Explain Reasoning**: Comments and docs explain "why", not just "what"

