import numpy as np
import random

# Learning rate
t = 0.1


# Signum (activation) function
def activation(z):
    if z > 0:
        return 1
    elif z < 0:
        return -1
    else:
        return 0


# Function to calculate ∇w or the change in weight
def change_w(w, x, d):
    return t * (d - activation(np.matmul(x, w))) * x


# Desired outputs
d1, d2, d3 = -1, -1, 1


# Input Vectors
x1 = np.array([1, -2, 0, -1])
x2 = np.array([0, 1.5, -0.5, -1])
x3 = np.array([-1, 1, 0.5, -1])


# Weight Vector
w1 = np.array([random.uniform(0, 10) for i in range(4)])


# Number of Iterations
n = 100

for _ in range(n):
    w1 += change_w(w1, x1, d1)
    w1 += change_w(w1, x2, d2)
    w1 += change_w(w1, x3, d3)

# Output Values
o1 = activation(np.matmul(x1, w1))
o2 = activation(np.matmul(x2, w1))
o3 = activation(np.matmul(x3, w1))

print("Output Values:", o1, o2, o3)
print("Weight Vector:", w1)
