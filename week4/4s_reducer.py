#!/usr/bin/env python3 
import sys 
from collections import defaultdict

# Dictionary to store department data 
department_data = defaultdict(list)

# Process each line of input 
for line in sys.stdin: 
	# Strip leading/trailing whitespace 
	line = line.strip()
	
	# Split the line into department, salary, and other details 
	try: 
		department, salary, details = line.split('\t', 2) 
		salary = int(salary) # Convert salary to integer for sorting 
		department_data[department].append((salary, details)) 
	except ValueError: 
		continue	
	
# Iterate over each department and sort by salary 
for department, records in department_data.items(): 
	# Sort records by salary 
	sorted_records = sorted (records, key=lambda x: x[0]) 
	
	# Emit sorted records 
	for salary, details in sorted_records: 
		print(f"{department},{details}")
