#!/usr/bin/env python3
"""Convert between wei, gwei and ether without floating point error.

Usage: python3 convert_units.py 1500000000 gwei ether
"""
import sys
from decimal import Decimal

UNITS = {"wei": Decimal(1), "gwei": Decimal(10) ** 9, "ether": Decimal(10) ** 18}


def convert(amount: str, src: str, dst: str) -> Decimal:
    return Decimal(amount) * UNITS[src] / UNITS[dst]


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        raise SystemExit(2)
    print(convert(sys.argv[1], sys.argv[2].lower(), sys.argv[3].lower()))
