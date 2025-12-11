"""
Random number generation API routes.

This module defines the API endpoint for generating random numbers.
It handles HTTP requests and delegates business logic to the service layer.
"""

from fastapi import APIRouter
from app.schemas.responses import RandomNumberResponse
from app.services.random_service import generate_random_number

# Create a router for random number endpoints
router = APIRouter(
    prefix="/random",
    tags=["random"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=RandomNumberResponse,
    summary="Generate a random number",
    description="""
    Generate a random number with no range limits.
    
    This endpoint returns a randomly generated number that can be any valid
    floating-point number. The number is generated using Python's random module
    and has no upper or lower bounds.
    
    **Returns:**
    - A JSON object containing:
        - `number`: The randomly generated number
        - `message`: A descriptive success message
    """,
    response_description="A random number with a success message"
)
async def get_random_number() -> RandomNumberResponse:
    """
    GET endpoint to generate a random number.
    
    This endpoint calls the random service to generate a number and
    returns it in a structured response format.
    
    Returns:
        RandomNumberResponse: Response containing the random number and message
    """
    # Call the service layer to generate the random number
    random_num = generate_random_number()
    
    # Return the response with the generated number
    return RandomNumberResponse(
        number=random_num,
        message="Random number generated successfully"
    )

