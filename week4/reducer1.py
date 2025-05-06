import sys
from collections import defaultdict

# Dictionary to store course data
course_data = {}

# Default dictionary to store students for each course
students_data = defaultdict(list)

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    course_id, record_type, data = line.split('\t')

    if record_type == 'C':  # Course data
        course_data[course_id] = data  # Store course information
    elif record_type == 'S':  # Student data
        student_id, student_name = data.split(',')
        students_data[course_id].append((student_id, student_name))  # Store student information

# After processing all lines, Print the students enrolled in the course
for course_id in course_data:
    if course_id in students_data:
        for student in students_data[course_id]:
            print(f"{student[0]}, {student[1]}, {course_id}, {course_data[course_id]}")

