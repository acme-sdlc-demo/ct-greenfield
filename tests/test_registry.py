from registry import FEATURES


def test_features_contains_shout_ac2() -> None:
    assert "shout" in FEATURES


def test_features_contains_alpha_ac2() -> None:
    assert "alpha" in FEATURES


def test_features_contains_beta_ac2() -> None:
    assert "beta" in FEATURES
