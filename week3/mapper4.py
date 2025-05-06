#!/usr/bin/env python3
# mapper.py

import sys

# Read lines from standard input (the input data)
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Skip the header line
    if line.startswith("Key,Value"):
        continue

    # Parse the line into key and value
    key, value = line.split(',')
    
    try:
        value = int(value)
        # Emit the key and the value
        print(f"{key}\t{value}")
    except ValueError:
        # Skip lines with invalid values
        continue

