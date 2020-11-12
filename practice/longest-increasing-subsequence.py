def function(array):
    """Function to print the count of the longest increasing subsequence"""
    count_array = [1] * len(array)

    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j] and count_array[i] <= count_array[j]:
                count_array[i] = count_array[j] + 1

    return count_array


def lis(array):
    """Function to print the longest increasing subsequence"""
    count_array = function(array)
    lis_array = []
    index = count_array[0]
    element = array[0]

    for i in range(len(array)):
        if index == count_array[i] and array[i] < element:
            element = array[i]
        elif count_array[i] == index + 1:
            lis_array.append(element)
            index += 1
            element = array[i]

    if count_array[-1] > count_array[-2]:
        lis_array.append(array[-1])

    return lis_array


print(lis([9, 1, 3, 7, 5, 6, 20]))
print(lis([3, 10, 2, 1, 20]))
print(lis([50, 3, 10, 7, 40, 80]))