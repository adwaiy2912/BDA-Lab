import sys
from collections import defaultdict

# Step 1: Read matrix data from standard input (sys.stdin)
def read_matrix():
    matrix_A = []
    matrix_B = []
    
    # Reading input from sys.stdin
    for line in sys.stdin:
        # Split each line by commas
        parts = line.strip().split(',')
        matrix_type = parts[0]
        i = int(parts[1])
        j = int(parts[2])
        value = int(parts[3])
        
        if matrix_type == 'a':
            matrix_A.append((i, j, value))  # Store (row, col, value) for A
        elif matrix_type == 'b':
            matrix_B.append((i, j, value))  # Store (row, col, value) for B
    
    return matrix_A, matrix_B

# Step 2: Mapper function for Matrix Multiplication
def mapper(matrix_A, matrix_B):
    # Emitting intermediate key-value pairs
    intermediate = []
    
    # Matrix A emits (i, k) -> A(i,k)
    for i, k, value_A in matrix_A:
        for k_B, j, value_B in matrix_B:
            if k == k_B:  # Only consider valid k values that match
                intermediate.append(((i, j), value_A * value_B))  # Emit (i, j) -> product of values
                
    return intermediate

# Step 3: Reducer function to combine results
def reducer(mapped_data):
    # Group values by (i, j)
    result = defaultdict(int)  # Initialize the result dictionary to hold the final sum of products
    
    for (i, j), value in mapped_data:
        result[(i, j)] += value  # Sum up all the products for each (i, j)
    
    return result

# Step 4: Main function to perform the matrix multiplication
def matrix_multiplication():
    # Read matrix data from standard input
    matrix_A, matrix_B = read_matrix()
    
    # Map step: Generate intermediate key-value pairs
    mapped_data = mapper(matrix_A, matrix_B)
    
    # Reduce step: Combine values based on the (i, j) key
    result = reducer(mapped_data)
    
    # Display the result (Matrix C)
    print("Resulting Matrix C:")
    for (i, j), value in sorted(result.items()):
        print(f"C({i},{j}) = {value}")

# Entry point of the program
if __name__ == "__main__":
    print("Enter the matrix data (Matrix A and B). Use Ctrl-D (or Ctrl-Z on Windows) to finish input.")
    matrix_multiplication()

