#!/usr/bin/env python3
import sys
from collections import defaultdict

# Dictionary to store word to document mapping
word_to_docs = defaultdict(set)

# Read input line by line (key: word, value: document)
for line in sys.stdin:
    # Strip leading/trailing whitespace
    line = line.strip()
    
    # Split the line into word and document
    word, doc_id = line.split('\t')
    
    # Add document to the set of documents for this word
    word_to_docs[word].add(doc_id)

# Output the results
for word, docs in word_to_docs.items():
    # Sort the document IDs and join them with a comma
    print(f"{word}\t{','.join(sorted(docs))}")

