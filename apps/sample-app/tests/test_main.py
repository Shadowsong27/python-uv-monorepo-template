"""Tests for the sample app main module."""

from sample_app.main import main


def test_main():
    """Test that main function runs without error."""
    # This test just ensures the main function can be called
    # In a real app, you'd test the actual functionality
    try:
        main()
        assert True
    except Exception as e:
        assert False, f"main() raised an exception: {e}"
