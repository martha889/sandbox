"""Karp-Rabin Algorithm"""

parent_string = 'abcdkflasjfksjfalskfjiwohefkncfoweifwoifnsidjfsoi'
substring = 'fk'


def hash_function(arr):
    """Takes O(length of array) time; returns the hash value for a string"""

    arr = list(map(lambda x: ord(x) - ord('a'), arr))
    arr.reverse()  # Adds n iterations; use (n - i - 1)th index in the for loop for a minor increase in efficiency
    total = 0

    for i in range(len(arr)):
        total += arr[i] * (26 ** i)

    return total


hash_target = hash_function(substring)
hash_value = 0
index_found = []

for start in range(0, len(parent_string) - len(substring) + 1):
    if start == 0:
        hash_value += hash_function(parent_string[:len(substring)])

        if hash_target == hash_value:
            index_found.append(start)

        continue
    else:
        hash_value -= (ord(parent_string[start-1]) - ord('a')) * (26 ** (len(substring) - 1))
        hash_value *= 26
        hash_value += ord(parent_string[start + len(substring) - 1]) - ord('a')

        if hash_target == hash_value:
            index_found.append(start)


print(index_found)




