#!/usr/bin/env python3 
import sys 

# Read input line by line 
for line in sys.stdin: 
	# Strip leading/trailing whitespace 
	line = line.strip()
	
	# Split the line into fields 
	fields = line.split(',')
	
	# Ensure the input format is valid 
	if len(fields) == 4:
		employee_id, department, name, salary = fields
		
		# Emit department and salary as composite key, with other details as 
		print(f"{department}\t{salary}\t{employee_id},{name}")
