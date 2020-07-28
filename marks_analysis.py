from matplotlib import pyplot as plt
import numpy as np


def dictionary_to_list(dic):
    array = []

    for i1 in dic:
        array.append([float(i1), dic[i1]])

    return array


def percentile(marks, arr):
    """Take 2D array with element of type [marks, count] as input"""

    total = 0
    num = 0

    for i2 in arr:
        if i2[0] <= marks:
            num += i2[1]

        total += i2[1]

    return f'{round(num / total * 100, 2)}%'


def excel_to_list(marks):
    """Returns list with element [marks, count] after taking a string of marks"""
    marks = marks.split("\n")

    while marks.count(""):
        marks.remove("")

    dic_marks = {}

    for i in marks:
        if i not in dic_marks:
            dic_marks[i] = 1
        else:
            dic_marks[i] += 1

    array = sorted(dictionary_to_list(dic_marks))

    return array


def graph_of_marks(array):
    """Take 2D array with element of type [marks, count] as input"""

    x, y = [], []

    for i in array:
        x.append(i[0])
        y.append(i[1])

    plt.plot(x, y)
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.show()


marksMA = """
17
25
17
26
16
12
27
28
19
16
12
22
20
22
8
21
15
15
18
9
16
16
9
11
9
20
29
26
23
11
27
24
24
19
29
24
28
27
7
29
17
25
22
8
27
22
7
22
22
27
26
25
30
26
10
3
21
11
18
9
11
4
25
14
28
22
4
11
23
21
19
19
16
26
19
21
22
25
12
"""
marksMKV_theory = """11
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
11
12
9
11
12
12
12
11
12
11
12
9
12
11
11
12
12
12
9
9
12
11
11
10
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
11
12
12
12
10
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
10
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12"""
marksMKV = """17.5
10
30
29
15
21.5
27.5
26.5
17.5
15
34
25
22.5
19
37.5
30
30
32.5
17.5
19
6.5
40
5
9
11.5
21.5
24
32.5
24
26.5
25
32.5
25
42.5
4
21.5
27.5
35
26.5
17.5
20
12.5
24
27.5
14
35
21.5
29
32.5
22.5
17.5
40
40
27.5
31.5
25
27.5
37.5
19
17.5
5
26.5
32.5
32.5
15
30
27.5
29
16.5
32.5
24
30
22.5
27.5

19
30
31.5
34
39
27.5
30
37.5
41.5
27.5
37.5
26.5
31.5
29
15
35
31.5
17.5
11.5
42.5
16.5
10
27.5
15
19
17.5
25
26.5
25.5
19
12.5
11.5
12.5
37.5
32.5
25
"""
marksMKVTotal = """61.5
81.5
77
62
59
89.5
64
56
77.5
62.5
64.5
65
70.5
73.5
73.5
67
60.5
58.5
58.5
83.5
79.5
72.5
61.5
58
77.5
76.5
61.5
69
75
73.5
64.5
63
82
72.5
70.5
68.5
87
78.5
79.5
80
64.5
67
47.5
85.5
53
56.5
58.5
66
71
78.5
71
70.5
73
79
71.5
90.5
51.5
69.5
71
79.5
74.5
63
68
60.5
70.5
75.5
61
82
67.5
76
80.5
70.5
65
86.5
87.5
75
79
73.5
73
84
63
65.5
52
76
81.5
80.5
61
74
75.5
78.5
61.5
80
70.5
77
70.5
74.5
66
78
78.5
80.5
86
76
79
86.5
89.5
75
83.5
73.5
79.5
77
"""
marksRM = """13.5
16
26
24
21
22.5
23
21
8
5.5
24.5
20.5
20
21
22.5
20.5
18
29
15
14
15
18.5
13
3.5
14.5
19
13
22.5
25.5
24.5
6
22
9.5
26.5
5.5
23
17.5
28
20.5
18.5
8
7
18.5
22.5
10.5
27
22
19
15
16.5
13
25.5
25.5
25
19.5
11.5
25
22.5
12.5
16.5
5
21.5
26.5
24.5
19.5
22.5
25.5
19
12.5
20.5
25
17.5
13
19.5
13.5
27.5
17
26.5
28
27
26
22.5
29
28
25.5
21
26
26
8
16.5
21.5
14
2
27.5
13
11.5
23.5
23.5
22.5
16.5
23.5
22.5
26.5
8.5
8
11.5
16.5
15
21.5
21.5"""

# array1 = excel_to_list(marksMA)
# array2 = excel_to_list(marksMKV)
# array3 = excel_to_list(marksMKV_theory)
#
# X1 = np.array([i[0] for i in array1])
# Y1 = [i[1] for i in array1]
# X1 /= max(X1)
# X1 *= 100
#
# X2 = np.array([i[0] for i in array2])
# Y2 = [i[1] for i in array2]
# X2 /= max(X2)
# X2 *= 100

# plt.plot(X1, Y1)
# plt.plot(X2, Y2)
# plt.legend(["Finite Element", "MKV"])
# plt.xlabel("% of Marks")
# plt.ylabel("Number of Students")
# plt.show()

array = excel_to_list(marksRM)
X = [i[0] for i in array]
Y = [i[1] for i in array]

print(percentile(20, array))
print(percentile(25, array))
plt.xlabel("Marks Obtained")
plt.ylabel("Number of Students")
plt.plot(X, Y)
plt.show()
