#!/usr/bin/env python3
# mapper.py

import sys

# Read lines from standard input
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()

    # Process each character in the line
    for char in line:
        # We are only interested in alphabetic characters
        if char.isalpha():
            print(f"{char.lower()}\t1")

