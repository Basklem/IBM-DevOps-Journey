import pytest
from converter import convert


def test_celsius_to_fahrenheit():
    assert convert("c2f", 0) == pytest.approx(32.0)
    assert convert("c2f", 100) == pytest.approx(212.0)


def test_fahrenheit_to_celsius():
    assert convert("f2c", 32) == pytest.approx(0.0)
    assert convert("f2c", 212) == pytest.approx(100.0)


def test_miles_to_km():
    assert convert("mi2km", 1) == pytest.approx(1.60934)


def test_km_to_miles():
    assert convert("km2mi", 1.60934) == pytest.approx(1.0)


def test_lbs_to_kg():
    assert convert("lb2kg", 1) == pytest.approx(0.453592)


def test_kg_to_lbs():
    assert convert("kg2lb", 0.453592) == pytest.approx(1.0)


def test_unknown_conversion_raises():
    with pytest.raises(ValueError):
        convert("bogus", 1)


def test_round_trip_celsius():
    original = 37.0
    converted = convert("c2f", original)
    back = convert("f2c", converted)
    assert back == pytest.approx(original)
