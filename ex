import numpy as np

# Step 1: Represent the system of equations as an augmented matrix
# Given system of equations:
# 2x + 3y + z = 9
# 2x - 3y + z = 13
# 3x + 4y + 5z = 40

# Coefficient matrix (A) and constant matrix (B)
A = np.array([[2, 3, 1],
              [2, -3, 1],
              [3, 4, 5]])

B = np.array([[9],
              [13],
              [40]])

# Augmented matrix
augmented_matrix = np.hstack((A, B))

# Step 2: Applying Gauss-Jordan Elimination
def gauss_jordan(matrix):
    rows, cols = matrix.shape
    
    for i in range(rows):
        # Make the diagonal element 1
        matrix[i] = matrix[i] / matrix[i, i]
        
        # Make the other elements in the current column 0
        for j in range(rows):
            if i != j:
                matrix[j] = matrix[j] - matrix[j, i] * matrix[i]
                
    return matrix

# Applying the Gauss-Jordan method
result = gauss_jordan(augmented_matrix.copy())

# Step 3: Extracting solutions
solutions = result[:, -1]

# Display the augmented matrix in reduced row-echelon form and the solutions
print("Reduced Row-Echelon Form (RREF):")
print(result)

print("\nSolutions:")
variables = ['x', 'y', 'z']
for var, sol in zip(variables, solutions):
    print(f"{var} = {sol}")