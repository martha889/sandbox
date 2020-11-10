def permutation(string):
    ind = 0
    string = list(string)
    output_array = list()

    def looping(index, array):
        if index == len(array) - 1:
            output_array.append("".join(array))

        else:
            for i in range(index, len(string)):
                array1 = array.copy()
                array1[index], array1[i] = array1[i], array1[index]
                looping(index + 1, array1)

    looping(ind, string)
    return output_array


print((permutation('ABC')))