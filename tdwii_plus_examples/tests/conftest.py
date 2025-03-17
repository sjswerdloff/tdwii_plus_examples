# conftest.py
import pytest


@pytest.fixture(autouse=True)
def add_custom_assertions(request):
    """Add custom assertion methods to all test cases."""

    def assertIsInstanceOrNone(self, obj, expected_type):
        """Assert that an object is either an instance of the specified type or None.
        The caller must explicitly pass self as the first argument"""
        if obj is not None:
            assert isinstance(obj, expected_type), (
                f"Expected {obj} to be an instance of {expected_type}, but it is {type(obj)}"
            )

    # Add the method to the test class
    if hasattr(request, "instance") and request.instance is not None:
        request.instance.assertIsInstanceOrNone = assertIsInstanceOrNone
