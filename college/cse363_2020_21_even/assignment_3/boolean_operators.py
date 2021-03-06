from read_index import document_number


def operator_and(list1, list2):

    result_list = []

    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result_list.append(list1[i])
            i += 1
            j += 1

        else:
            if list1[i] > list2[j]:
                j += 1
            else:
                i += 1

    return result_list


def operator_or(list1, list2):

    result_list = []

    i, j = 0, 0

    while True:
        if i == len(list1) and j < len(list2):
            result_list.extend(list2[j:])
            break
        elif j == len(list2) and i < len(list1):
            result_list.extend(list1[i:])
            break
        elif i == len(list1) and j == len(list2):
            break

        if list1[i] == list2[j]:
            result_list.append(list1[i])
            i += 1
            j += 1
        else:
            if list1[i] < list2[j]:
                result_list.append(list1[i])
                i += 1
            else:
                result_list.append(list2[j])
                j += 1

    return result_list


def operator_not(list1):
    result_list = []

    i = 0

    while i <= document_number:
        if i not in list1:
            result_list.append(i)
        i += 1

    return result_list
