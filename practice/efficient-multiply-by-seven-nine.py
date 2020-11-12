def multiply_by_seven(n):
    """Left shift by 3 bits and take difference from the original number"""
    return (n << 3) - n


def multiply_by_nine(n):
    """Left shift by 3 bits and add the original number"""
    return (n << 3) + n


for i in range(8):
    print(multiply_by_seven(i))

for i in range(10):
    print(multiply_by_nine(i))