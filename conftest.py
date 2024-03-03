""" This file contains the fixtures that are used in the tests. """
import pytest
from faker import Faker

def pytest_addoption(parser):
    """Add a command-line option to the pytest command."""
    parser.addoption(
        "--num_records", action="store", default=1, type=int, help="Number of records to generate"
    )

@pytest.fixture
def random_number(request):
    """Generate a random number."""
    fake = Faker()
    num_records = request.config.getoption("--num_records")
    return [fake.pyint() for _ in range(num_records)]
