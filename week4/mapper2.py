#!/usr/bin/env python3
import sys

# Define the stop words
STOP_WORDS = {'is', 'the', 'and', 'a', 'of', 'in', 'to', 'for', 'on', 'with', 'by'}

# Read input line by line
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()
    
    # Tokenize the line into words
    words = line.split()
    
    for word in words:
        # Convert to lowercase and remove punctuation
        word = word.lower().strip('.,!?":;()[]{}')
        
        # Emit word and count (1) if it's not a stop word
        if word not in STOP_WORDS:
            print(f"{word}\t1")

