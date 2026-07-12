"""
Tiny unit converter CLI.

Built as an "end of chapter" project for Course 1 (Intro to DevOps) of the
IBM DevOps and Software Engineering certificate.

The app itself is intentionally simple — the real point of this project is
the DevOps pipeline wrapped around it (see .github/workflows/ci.yml).
"""

import argparse
import sys


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def miles_to_km(miles: float) -> float:
    return miles * 1.60934


def km_to_miles(km: float) -> float:
    return km / 1.60934


def lbs_to_kg(lbs: float) -> float:
    return lbs * 0.453592


def kg_to_lbs(kg: float) -> float:
    return kg / 0.453592


CONVERSIONS = {
    "c2f": celsius_to_fahrenheit,
    "f2c": fahrenheit_to_celsius,
    "mi2km": miles_to_km,
    "km2mi": km_to_miles,
    "lb2kg": lbs_to_kg,
    "kg2lb": kg_to_lbs,
}


def convert(kind: str, value: float) -> float:
    if kind not in CONVERSIONS:
        raise ValueError(f"Unknown conversion type: {kind}")
    return CONVERSIONS[kind](value)


def main():
    parser = argparse.ArgumentParser(description="Tiny unit converter CLI")
    parser.add_argument(
        "kind",
        choices=CONVERSIONS.keys(),
        help="Type of conversion to perform",
    )
    parser.add_argument("value", type=float, help="Value to convert")
    args = parser.parse_args()

    result = convert(args.kind, args.value)
    print(f"{args.value} -> {result:.2f}")


if __name__ == "__main__":
    sys.exit(main())
