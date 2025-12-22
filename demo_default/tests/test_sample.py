import pytest


@pytest.mark.smoke
def test_sample_smoke_check():
    """Basic smoke test to verify that the test suite is wired correctly."""
    # Given
    expected_value = 1

    # When
    result = 1

    # Then
    assert result == expected_value
