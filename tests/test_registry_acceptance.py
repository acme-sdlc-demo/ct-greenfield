from registry import FEATURES


# AC-2: FEATURES contains "farewell" and still contains every pre-existing entry


def test_features_contains_farewell_ac2() -> None:
    """FEATURES must include the newly registered 'farewell' entry."""
    assert "farewell" in FEATURES


def test_features_contains_existing_ac2() -> None:
    """All entries present before the change must still appear in FEATURES."""
    assert "alpha" in FEATURES
    assert "beta" in FEATURES
