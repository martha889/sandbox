import random
import matplotlib.pyplot as plt
# Global Variables:

# N_c = Number of bits used to describe one load, N_rlc = number of loads, N_l = number of locations for one load
N_c, N_rlc, N_l = 2, 3, 4

# N: number of iterations, M: Selection Size
N, M = 100, 20

# Range of output values
low, high = 0, pow(10, 6)

# Size of initial population and chromosome length
pop_size = 10

# Chromosome length has 1 extra bit -> for series or parallel
chr_length = N_rlc * (N_l + 3 * N_c + 1)

# crossover and mutation rates
crossover_rate, mutation_rate = 0.6, 0.1

# Number of bits to be mutated in one instance of the mutation function
B = 1


# convert a chromosome(string of binary characters) to its real value
def binary_to_real(c):
    return low + ((high - low) / (pow(2, len(c)) - 1)) * int(c, 2)


# returns the objective function value for a given chromosome
def obj_function(c):
    return binary_to_real(c)


# generates a chromosome of a given length(k)
def c_generator(k):
    c = ''
    for _ in range(k):
        if random.random() > 0.5:
            c += '1'
        else:
            c += '0'
    return c


# generates population (1-D array of chromosomes) given total size(n) and individual length(k) respectively
def pop_generator(n, k):
    pop = []
    for _ in range(n):
        pop.append(c_generator(k))
    return pop


# returns the 2nd element of a 1d array
def sort_key(array_1d):
    return array_1d[1]


# returns a crossed chromosomes, given 2 chromosomes and a crossover point
def cross_one_pt(chr1, chr2):
    p = random.randint(0, len(chr1) - 1)
    o1 = chr1[:p] + chr2[p:]
    return o1


# returns a crossed chromosome, given 2 chromosomes
def cross_two_pt(chr1, chr2):
    p1, p2 = random.randint(0, len(chr1) - 1), random.randint(0, len(chr1) - 1)
    p1, p2 = min(p1, p2), max(p1, p2)
    o1 = chr1[:p1] + chr2[p1:p2] + chr1[p2:]
    return o1


# returns a crossed chromosomes after uniform crossover
def cross_uni(chr1, chr2):
    o1 = ''
    for i in range(len(chr1)):
        if random.random() > 0.5:
            o1 += chr1[i]
        else:
            o1 += chr2[i]
    return o1


# takes chromosome and mutates b bits in it
def mutation(c):
    o = ''
    mut_b = [random.randint(0, len(c) - 1) for i in range(B)]
    for i in range(len(c)):
        if i in mut_b:
            o += str(1 - int(c[i]))
        else:
            o += c[i]
    return o


# takes population of chromosome (with their fitness scores) and tournament size, returns a single individual
def sel_tournament(p_obj, n):
    return max([p_obj[random.randint(0, len(p_obj) - 1)] for i in range(n)], key=sort_key)[0]


# takes population (with fitness) and returns a single individual
def sel_roulette(p_obj):
    total = sum(i[1] for i in p_obj)
    p = [i[0] for i in p_obj]
    w = [i[1] / total for i in p_obj]
    op = (random.choices(p, weights=w))[0]
    return op


def sel_ranking(p_obj):
    n = len(p_obj)
    total = n * (n + 1) / 2
    p1 = sorted(p_obj, key=sort_key)
    p = [i[0] for i in p1]
    w = [(i + 1) / total for i in range(len(p1))]
    op = (random.choices(p, weights=w))[0]
    return op


# takes population (1-d array of strings) and returns 2-d array (string, obj fn value)
def pop_obj(pop):
    return [[i, obj_function(i)] for i in pop]


def real_values(c):
    op = []


mating_pool = pop_generator(pop_size, chr_length)
best1 = (max([i for i in pop_obj(mating_pool)], key=sort_key))
output_graph_x = []
output_graph_y = []

for i1 in range(N):
    mating_pool1 = []
    mating_pool2 = []
    mating_pool3 = []
    # selection
    for _ in range(M):
        mating_pool1.append(sel_roulette(pop_obj(mating_pool)))
    # cross-over (rate = 0.6)
    for _ in range(M):
        if random.random() <= crossover_rate:
            mating_pool2.append(cross_two_pt(mating_pool1[random.randint(0, M - 1)], mating_pool1[random.randint(0, M - 1)]))
        else:
            mating_pool2.append(mating_pool1[random.randint(0, M - 1)])
    # mutation (rate = 0.1)
    for _ in range(M):
        k = random.randint(0, M - 1)
        if random.random() <= mutation_rate:
            mating_pool3.append(mutation(mating_pool2[k]))
        else:
            mating_pool3.append(mating_pool2[k])
    mating_pool = mating_pool3
    best2 = (max([i for i in pop_obj(mating_pool)], key=sort_key))
    if best2[1] > best1[1]:
        best1 = best2
    output_graph_x.append(i1+1)
    output_graph_y.append(best1[1])
    print('best after ' + str(i1+1) + ' iteration ' + str(best2[1]), ', Overall Best: ' + str(best1[1]))

plt.style.use('ggplot')
plt.plot(output_graph_x, output_graph_y)
plt.grid(True)
plt.title("Genetic Algorithm")
plt.xlabel("Number of iterations")
plt.ylabel("Value of Objective Function")
plt.show()










