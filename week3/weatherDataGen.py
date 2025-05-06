import random
import datetime

# Set the range of years
start_year = 2000
end_year = 2025
num_entries = 200

# Open the text file to write the data
with open('weather_data.txt', 'w') as file:
    # Generate the data for each entry
    for _ in range(num_entries):
        year = random.choice(range(start_year, end_year + 1))  # Randomly select the year (2025)
        temp = random.randint(-10, 35)  # Randomly generate a temperature between -10°C and 35°C
        file.write(f"{year}, {temp}\n")

print("Weather data file 'weather_data.txt' has been created.")

