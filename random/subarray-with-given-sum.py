# Sub-array with a given sum

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    array = list(map(int, input().split()))

    total = 0
    i, j = 0, 0

    while j < n:
        if total == s:
            print(i, j)
            break
        elif total < s:
            total += array[j]
            if total >= s:
                continue
            else:
                j += 1
        else:
            while total > s:
                total -= array[i]
                i += 1
