import random
import string

# Function to generate a random name
def generate_random_name():
    first_name_length = random.randint(3, 8)  # Random length for first name
    first_name = ''.join(random.choices(string.ascii_uppercase, k=first_name_length))
    return first_name

# Function to generate random score
def generate_random_score():
    return random.randint(0, 100)  # Random score between 0 and 100

# Parameters
num_records = 100  # Number of records to generate
output_file = "record_data.txt"  # Output file name

# Generate data and write to file
with open(output_file, 'w') as f:
    f.write("Name,Score\n")  # Write header
    for _ in range(num_records):
        name = generate_random_name()
        score = generate_random_score()
        f.write(f"{name},{score}\n")

print("Record data file 'record_data.txt' has been created.")

