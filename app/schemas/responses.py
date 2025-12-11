"""
Response schemas for API endpoints.

This module contains Pydantic models that define the structure
of API responses, ensuring type safety and automatic validation.
"""

from pydantic import BaseModel, Field


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
    message: str = Field(
        ...,
        description="A descriptive message about the generated number",
        examples=["Random number generated successfully"]
    )
    
    class Config:
        """Pydantic configuration."""
        json_schema_extra = {
            "example": {
                "number": 42.0,
                "message": "Random number generated successfully"
            }
        }

