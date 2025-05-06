#!/usr/bin/env python3
# reducer.py

import sys

# Initialize variables
current_char = None
current_count = 0

# Read lines from standard input (key-value pairs from the mapper)
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Parse the line into character and count
    char, count = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        continue  # Skip lines with invalid counts

    # If the character changes, output the total count for the previous character
    if current_char != char:
        if current_char:
            # Output the count for the previous character
            print(f"{current_char}\t{current_count}")
        
        # Update the current character and reset the count
        current_char = char
        current_count = count
    else:
        # Accumulate the count for the current character
        current_count += count

# Output the count for the last character
if current_char:
    print(f"{current_char}\t{current_count}")

