from registry import FEATURES

# AC-2: FEATURES contains "farewell" and preserves every pre-existing entry


def test_features_contains_farewell_ac2() -> None:
    """FEATURES must include the newly registered "farewell" entry."""
    assert "farewell" in FEATURES


def test_features_contains_existing_ac2() -> None:
    """All entries that existed before the change must still be present in FEATURES."""
    assert "alpha" in FEATURES


def test_features_contains_shout_ac2() -> None:
    assert "shout" in FEATURES


def test_features_contains_alpha_ac2() -> None:
    assert "alpha" in FEATURES


def test_features_contains_beta_ac2() -> None:
    assert "beta" in FEATURES
