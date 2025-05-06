import sys

for line in sys.stdin:
    line = line.strip()
    
    # Split the line into columns
    fields = line.split(',')
    
    # Check if it's a Student record based on StudentID starting with "STU"
    if len(fields) == 3 and fields[0].startswith("STU"):
        student_id, name, course_id = fields
        print(f"{course_id}\tS\t{student_id},{name}")
    
    # Handle the Courses dataset
    elif len(fields) == 3 and not fields[0].startswith("STU"):
        course_id, course_name, sem = fields
        print(f"{course_id}\tC\t{course_name},{sem}")

