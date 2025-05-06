#!/usr/bin/env python3
# weather_reducer.py
import sys

# Initialize variables
current_year = None
max_temp = -float('inf')  # Start with a very low value for comparison

# Read the input from the standard input
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()
    
    # Skip empty lines
    if not line:
        continue

    # Parse the input into year and temperature
    year, temp = line.split('\t')
    temp = int(temp)  # Convert temperature to integer

    # If we encounter a new year, print the maximum temperature for the previous year
    if current_year != year:
        if current_year:
            print(f'{current_year}\t{max_temp}')
        current_year = year
        max_temp = temp
    else:
        # If the year is the same, update the maximum temperature
        max_temp = max(max_temp, temp)

# Print the maximum temperature for the last year
if current_year:
    print(f'{current_year}\t{max_temp}')

