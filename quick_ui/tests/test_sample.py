import pytest


@pytest.mark.smoke
@pytest.mark.ui
def test_ui_sample_placeholder():
    """Example ui test skeleton.

    This test does NOT hit a real browser yet. It is a placeholder to
    show naming and structure. Replace its body with real ui automation
    using Playwright, Selenium, etc.
    """
    # Given
    expected_title = "Swag Labs"

    # When
    # TODO: replace this with a real browser call to get the title
    current_title = expected_title

    # Then
    assert current_title == expected_title
