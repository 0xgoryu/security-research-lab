#!/usr/bin/env python3
"""Check whether a host falls inside a set of scope patterns.

Usage:
    python3 scope_match.py "*.example.com,app.example.com" app.example.com
    python3 scope_match.py "*.example.com" evil-example.com   # -> OUT

Rules:
- "*.example.com" matches subdomains of example.com, not example.com itself.
- A plain pattern matches exactly.
- Matching is case-insensitive. No network access is made.
"""

import sys


def in_scope(patterns: list[str], host: str) -> bool:
    host = host.strip().lower().rstrip(".")
    for raw in patterns:
        pattern = raw.strip().lower().rstrip(".")
        if not pattern:
            continue
        if pattern.startswith("*."):
            suffix = pattern[1:]  # ".example.com"
            if host.endswith(suffix) and host != suffix.lstrip("."):
                return True
        elif host == pattern:
            return True
    return False


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    patterns = argv[1].split(",")
    host = argv[2]
    print("IN SCOPE" if in_scope(patterns, host) else "OUT OF SCOPE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
