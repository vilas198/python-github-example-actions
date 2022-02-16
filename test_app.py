"""testing for unitesting"""
from app import index


def test_index():
    """testing app index """
    assert index() == "Hello World"

