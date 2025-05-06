#!/usr/bin/env python3
# record_reducer.py
import sys

# Dictionary to store scores by name
scores = {}

# Read lines from standard input (key-value pairs from the mapper)
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Parse the name and score
    name, score = line.split('\t')
    
    try:
        score = int(score)
        # Store the highest score for each name
        if name not in scores or score > scores[name]:
            scores[name] = score
    except ValueError:
        # Skip lines with invalid scores
        continue

# Sort the names by their scores in descending order and select the top 10
top_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]

# Output the top 3 highest scorers
for name, score in top_scores:
    print(f'{name}\t{score}')

