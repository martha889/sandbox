def divisibility_by_three(n):
    """Convert number to binary, takes difference of digits at odd and even positions
    (Similar to divisibility by 11 in base 10 number system"""
    binary = bin(n)[2:]
    odd = 0
    even = 0

    for i in range(0, len(binary), 2):
        if binary[i] == '1':
            odd += 1

    for i in range(1, len(binary), 2):
        if binary[i] == '1':
            even += 1

    if abs(odd - even) % 3:
        return False
    else:
        return True


for i in range(20):
    print(i, divisibility_by_three(i))
