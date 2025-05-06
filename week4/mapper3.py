#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()
    
    # Split the line into document ID and the content
    fields = line.split(' ', 1)
    
    if len(fields) == 2:
        doc_id, content = fields
        
        # Tokenize the content into words
        words = content.split()
        
        # Emit the word as the key, with document ID as the value
        for word in words:
            # Clean the word (lowercase and remove punctuation)
            word = word.lower().strip('.,!?":;()[]{}')
            
            # Emit word and document ID
            print(f"{word}\t{doc_id}")

