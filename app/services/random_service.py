"""
Random number generation service.

This module contains the business logic for generating random numbers.
It's separated from the API layer to follow clean architecture principles
and make the code more testable and maintainable.
"""

import random


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
    # Generate a random float between 0 and 1
    base_random = random.random()
    
    # Scale it to a larger range for more variety
    # Using multiplication and addition to create diverse numbers
    # This ensures we get numbers across different magnitudes
    scaled_number = base_random * (10 ** random.randint(-10, 10))
    
    # Add some randomness to the sign (positive or negative)
    if random.random() < 0.5:
        scaled_number = -scaled_number
    
    return scaled_number

