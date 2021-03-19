import random
from matplotlib import pyplot as plt


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x = [random.random() for i in range(30)]
y = [random.random() for i in range(30)]


"""Randomly pick two points as means"""
index_1 = random.randint(0, len(x)-1)
index_2 = random.randint(0, len(y)-1)

mu_r = [x[index_1], y[index_1]]
mu_g = [x[index_2], y[index_2]]

cluster = [0] * len(x)

iteration = 5

while iteration > 0:
    for i in range(len(x)):
        if distance(x[i], y[i], mu_r[0], mu_r[1]) < distance(x[i], y[i], mu_g[0], mu_g[1]):
            cluster[i] = 'r'
        else:
            cluster[i] = 'g'

    mu_r_x, mu_r_y = 0, 0
    mu_g_x, mu_g_y = 0, 0
    count_r = 0
    count_g = 0

    for i in range(len(cluster)):
        if cluster[i] == 'r':
            count_r += 1
            mu_r_x += x[i]
            mu_r_y += y[i]
        else:
            count_g += 1
            mu_g_x += x[i]
            mu_g_y += y[i]

    mu_r = [mu_r_x / count_r, mu_r_y / count_r]
    mu_g = [mu_g_x / count_g, mu_g_y / count_g]

    plt.scatter(x, y, c=cluster)
    plt.show()

    iteration -= 1







