import random
import time

def is_prime(n: int) -> bool:
    """Check if an integer is a prime number."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_average(numbers: list[int]) -> float:
    """Calculate the average of a list of numbers."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        return 0.0
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError("All elements must be numbers")
    return sum(numbers) / len(numbers)

class NumberGeneratorService:
    def fetch_random_number(self) -> int:
        """Simulate fetching a random number from an external API, taking some time."""
        time.sleep(2)  # Simulate network latency
        return random.randint(1, 100)

def is_random_number_prime(service: NumberGeneratorService) -> bool:
    """Fetch a random number using the provided service and check if it is prime."""
    number = service.fetch_random_number()
    return is_prime(number)
