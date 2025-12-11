"""
Application entry point.

This module serves as the entry point for running the FastAPI application.
It loads the port configuration from environment variables and starts
the Uvicorn server.

Note: This file is named 'run.py' instead of 'app.py' to avoid naming conflicts
with the 'app/' package directory. Python's import system would be ambiguous
between 'app.py' (file) and 'app/' (package), causing import errors when
Uvicorn tries to load 'app.main:app'.
"""

import os
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
    """
    Main function to start the FastAPI application server.
    
    Reads the PORT from environment variables (defaults to 8000)
    and starts the Uvicorn ASGI server.
    """
    # Get port from environment variable, default to 8000
    port = int(os.getenv("PORT", 8000))
    
    # Start the server
    # Using string reference "app.main:app" to load the FastAPI instance
    # from the app package's main module. This works correctly because
    # there's no naming conflict - run.py doesn't interfere with app/ package
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  # Listen on all network interfaces
        port=port,
        reload=True,  # Enable auto-reload during development
        log_level="info"
    )


if __name__ == "__main__":
    main()

