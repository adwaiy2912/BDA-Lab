from functools import reduce

# Matrix A
A = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Matrix B
B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Function for Matrix Addition
def matrix_addition(A, B):
    return list(map(lambda row_a, row_b: list(map(lambda x, y: x + y, row_a, row_b)), A, B))

# Function for Matrix Subtraction
def matrix_subtraction(A, B):
    return list(map(lambda row_a, row_b: list(map(lambda x, y: x - y, row_a, row_b)), A, B))

# Function for Matrix Multiplication
def matrix_multiplication(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))
    ]

# Function for Matrix Transpose
def matrix_transpose(A):
    return list(map(list, zip(*A)))

# Matrix Operations
addition_result = matrix_addition(A, B)
subtraction_result = matrix_subtraction(A, B)
multiplication_result = matrix_multiplication(A, B)
transpose_result_A = matrix_transpose(A)
transpose_result_B = matrix_transpose(B)

# Print results
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nMatrix A + Matrix B:")
for row in addition_result:
    print(row)

print("\nMatrix A - Matrix B:")
for row in subtraction_result:
    print(row)

print("\nMatrix A * Matrix B:")
for row in multiplication_result:
    print(row)

print("\nTranspose of Matrix A:")
for row in transpose_result_A:
    print(row)

print("\nTranspose of Matrix B:")
for row in transpose_result_B:
    print(row)

