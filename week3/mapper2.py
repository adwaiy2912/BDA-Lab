#!/usr/bin/env python3
# weather_mapper.py
import sys

# Read lines from standard input
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue
    
    # Split the line into year and temperature
    try:
        year, temp = line.split(', ')
        temp = int(temp)  # Convert temperature to integer
        # Emit the year and temperature as a key-value pair
        print(f'{year}\t{temp}')
    except ValueError:
        # Skip lines that don't match the expected format (e.g., headers)
        continue

