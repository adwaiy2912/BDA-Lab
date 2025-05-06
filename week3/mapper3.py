#!/usr/bin/env python3
# record_mapper.py
import sys

# Read lines from standard input
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue
    
    try:
        name, score = line.split(',')
        score = int(score)
        
        print(f'{name}\t{score}')
    except ValueError:
        # Skip lines that don't match the expected format (e.g., headers)
        continue

