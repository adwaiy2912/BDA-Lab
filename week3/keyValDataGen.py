import random
import string

# Function to generate a random key (name or category)
def generate_random_key():
    length = 1
    key = ''.join(random.choices(string.ascii_uppercase, k=length))
    return key

# Function to generate a random value (integer)
def generate_random_value():
    return random.randint(1, 100)  # Random value between 1 and 100

# Parameters
num_records = 100  # Number of records to generate
output_file = "keyVal_data.txt"  # Output file name

# Generate data and write to file
with open(output_file, 'w') as f:
    f.write("Key,Value\n")  # Write header
    for _ in range(num_records):
        key = generate_random_key()
        value = generate_random_value()
        f.write(f"{key},{value}\n")

print(f"{num_records} records generated and saved in {output_file}.")

