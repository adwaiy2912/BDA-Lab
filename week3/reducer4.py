#!/usr/bin/env python3
# reducer.py

import sys

# Initialize variables for the current key, sum, and count
current_key = None
current_sum = 0
current_count = 0

# Read lines from standard input (key-value pairs from the mapper)
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Parse the line into key and value
    key, value = line.split('\t')

    try:
        value = int(value)
    except ValueError:
        continue  # Skip lines with invalid values

    # If the key changes, output the average for the previous key
    if current_key != key:
        if current_key:
            # Calculate the average and print it
            average = current_sum / current_count
            print(f"{current_key}\t{average:.2f}")
        
        # Update the current key and reset sum and count
        current_key = key
        current_sum = value
        current_count = 1
    else:
        # Accumulate the sum and count for the current key
        current_sum += value
        current_count += 1

# Output the average for the last key
if current_key:
    average = current_sum / current_count
    print(f"{current_key}\t{average:.2f}")

