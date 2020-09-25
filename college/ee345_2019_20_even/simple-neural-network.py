import random


# Function to multiply two matrices
def matrix_multiplication(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


# Function to add two matrices
def matrix_addition(a, b):
    total = [0] * len(a)
    for i in range(len(a)):
        total[i] = a[i] + b[i]
    return total


# Number of Iterations
n = 100

# Correction Parameter (threshold)
t = 0.01

# Input Values
x1 = [-1, 1, 2, 3]
x2 = [-1, 9, 2, 4]
x3 = [-1, 1, 5, 6]

# Desired Outputs
d1 = 1.4
d2 = 2.5
d3 = 2.9

# Weights (Random numbers between 0 to 10)
w1 = [random.uniform(0, 10) for i in range(4)]
w2 = [random.uniform(0, 10) for i in range(4)]
w3 = [random.uniform(0, 10) for i in range(4)]

for i in range(n):
    op1 = matrix_multiplication(x1, w1)
    err1 = d1 - op1
    delta_w1 = [t * err1 * i for i in x1]
    w1 = matrix_addition(w1, delta_w1)

    op2 = matrix_multiplication(x2, w2)
    err2 = d2 - op2
    delta_w2 = [t * err2 * i for i in x2]
    w2 = matrix_addition(w2, delta_w2)

    op3 = matrix_multiplication(x3, w3)
    err3 = d3 - op3
    delta_w3 = [t * err3 * i for i in x3]
    w3 = matrix_addition(w3, delta_w3)
    print(f"After iteration {i+1}: {op1}, {op2}, {op3}")

print("\nThe final weights are as follows:")
print("W1:", w1)
print("W2:", w2)
print("W3:", w3)