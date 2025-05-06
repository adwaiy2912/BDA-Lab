from functools import reduce

# Mapper function: This will read and emit (key, value) pairs, where the key is the student's name and the value is the entire student record.
def mapper(line):
    parts = line.strip().split(', ')  # Split by comma and space
    if len(parts) != 3:  # Check if the line has exactly 3 parts (reg_no, name, marks)
        return None  # Skip malformed lines
    reg_no = parts[0]
    name = parts[1]
    marks = parts[2]
    return (name, line)  # Emit a tuple (name, full record)

# Reducer function: This will sort the data by student name.
def reducer(mapped_data):
    # Filter out any None values (malformed lines) from the mapped data
    mapped_data = list(filter(None, mapped_data))
    # Sort the data based on the student name (which is the key)
    return sorted(mapped_data, key=lambda x: x[0])

# Main function to simulate MapReduce
def main():
    # Read data from the file
    with open("/home/bdalab/220968424/week2/students.txt", "r") as file:
        lines = file.readlines()

    # Step 1: Apply mapper to each line in the file
    mapped_data = list(map(mapper, lines))

    # Step 2: Apply reducer to sort the mapped data by student name
    sorted_data = reducer(mapped_data)

    # Output the sorted student details
    print("Sorted Student Data by Name:")
    for _, student_record in sorted_data:
        print(student_record)

if __name__ == "__main__":
    main()

