"""testing for unitesting"""
from app import index


def test_index1():
    """testing app index """
    assert index() == "Hello World"

