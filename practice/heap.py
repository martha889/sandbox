def heap_create(arr):
    heap = []

    for i in range(len(arr)):
        heap.append(arr[i])
        j = len(heap) - 1

        while True:
            if j % 2:
                p = j // 2
                if p >= 0 and heap[p] < heap[j]:
                    heap[j], heap[p] = heap[p], heap[j]
                    j = p
                else:
                    break
            else:
                p = j // 2 - 1
                if p >= 0 and heap[p] < heap[j]:
                    heap[j], heap[p] = heap[p], heap[j]
                    j = p
                else:
                    break

    return heap


def heap_max_element(heap):
    return heap[0]


def heap_max_extract(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    op = heap.pop()
    l = len(heap) - 1
    i = 0

    while True:
        left = 2 * i + 1
        right = 2 * i + 2

        if left <= l and right <= l:
            if heap[i] >= heap[left] and heap[i] >= heap[right]:
                break
            elif heap[left] > heap[i] and heap[left] >= heap[right]:
                heap[i], heap[left] = heap[left], heap[i]
                i = left
            else:
                heap[i], heap[right] = heap[right], heap[i]
                i = right
        elif left <= l:
            if heap[i] >= heap[left]:
                break
            else:
                heap[i], heap[left] = heap[left], heap[i]
                i = left
        elif right <= l:
            if heap[i] >= heap[right]:
                break
            else:
                heap[i], heap[right] = heap[right], heap[i]
                i = right
        else:
            break

    return op


# Correct violations of the max-heap property
def heap_heapify(heap, l):

    for i in range(l, -1, -1):
        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            if left <= l and right <= l:
                if heap[i] >= heap[left] and heap[i] >= heap[right]:
                    break
                elif heap[left] > heap[i] and heap[left] >= heap[right]:
                    heap[i], heap[left] = heap[left], heap[i]
                    i = left
                    continue
                else:
                    heap[i], heap[right] = heap[right], heap[i]
                    i = right
                    continue
            elif left <= l:
                if heap[i] >= heap[left]:
                    break
                else:
                    heap[i], heap[left] = heap[left], heap[i]
                    i = left
                    continue
            elif right <= l:
                if heap[i] >= heap[right]:
                    break
                else:
                    heap[i], heap[right] = heap[right], heap[i]
                    i = right
                    continue
            else:
                break


def heap_sort(heap):
    l = len(heap) - 1

    while l >= 0:
        heap[0], heap[l] = heap[l], heap[0]
        l -= 1
        heap_heapify(heap, l)

    return heap


array = heap_create([i for i in range(200, 7, -9)])
print(array)
print(heap_sort(array))
