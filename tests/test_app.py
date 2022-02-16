"""testing for unitesting"""
from src.app import index


def test_index():
    """testing app index """
    assert index() == "Hello World"

