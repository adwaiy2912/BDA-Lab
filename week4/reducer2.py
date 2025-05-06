#!/usr/bin/env python3
import sys
from collections import defaultdict

# Dictionary to store word counts
word_counts = defaultdict(int)

# Read input line by line
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()
    
    # Split the line into key and count (format: word \t count)
    word, count = line.split('\t')
    
    # Increment the word count
    word_counts[word] += int(count)

# Output the results
for word, count in word_counts.items():
    print(f"{word}\t{count}")

