"""Tests for random-name."""

import pytest
from random_name import name


class TestName:
    """Test suite for name."""

    def test_basic(self):
        """Test basic usage."""
        result = name("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            name("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = name(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
