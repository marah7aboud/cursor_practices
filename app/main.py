"""
FastAPI application main module.

This module initializes the FastAPI application, includes routers,
and configures the application metadata for Swagger documentation.
"""

import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.routes import random_number

# Load environment variables from .env file
load_dotenv()

# Create FastAPI application instance
app = FastAPI(
    title="Random Number Generator API",
    description="""
    A simple FastAPI application that generates random numbers.
    
    ## Features
    
    * Generate random numbers with no range limits
    * Automatic API documentation with Swagger UI
    * Clean, modular, and well-documented code
    
    ## Endpoints
    
    * **GET /random**: Generate a random number
    """,
    version="1.0.0",
    docs_url="/docs",  # Swagger UI endpoint
    redoc_url="/redoc",  # ReDoc endpoint
)

# Include API routers
app.include_router(random_number.router)


@app.get("/", tags=["root"])
async def root():
    """
    Root endpoint providing API information.
    
    Returns:
        dict: Welcome message and API information
    """
    return {
        "message": "Welcome to Random Number Generator API",
        "docs": "/docs",
        "redoc": "/redoc",
        "random_number_endpoint": "/random"
    }


@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        dict: Health status of the API
    """
    return {"status": "healthy", "service": "random-number-generator"}

