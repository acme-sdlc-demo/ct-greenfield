from registry import FEATURES


def test_features_contains_farewell() -> None:
    assert "farewell" in FEATURES


def test_features_contains_existing() -> None:
    assert "alpha" in FEATURES
    assert "beta" in FEATURES
