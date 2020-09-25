import random
import matplotlib.pyplot as plt
import math


# Global Variables:
number_of_generators_t = 10
number_of_fuels_k = 4  # Types of fuels
number_of_intervals_j = 96
number_of_hours_in_interval_nj = 0.25
# fuel_costs_per_unit = np.array([2.75, 2.25, 2.00, 3.00])
P_array_low = [11, 36, 36, 47, 47, 60, 60, 43, 43, 43]
P_array_high = [16, 114, 114, 97, 97, 190, 190, 60, 60, 60]

# Fuel allocation factor for 24
# R_array = np.random.rand(number_of_generators_t, number_of_fuels_k)

N_loadings_tj, N_fuel_allocation_factor_tj = 9, 9

# N: number of iterations, M: Selection Size
N, M = 50, 20

# # Range of output values
# low, high = 0, pow(10, 10)

# Size of initial population and chromosome length
pop_size = 10

# Chromosome length has 1 extra bit -> for series or parallel
chr_length_P = N_loadings_tj * number_of_intervals_j * number_of_generators_t
chr_length_RHO = N_fuel_allocation_factor_tj * number_of_generators_t * number_of_intervals_j * number_of_fuels_k

# crossover and mutation rates
crossover_rate, mutation_rate = 0.4, 0.2

# Number of bits to be mutated in one instance of the mutation function
B = 1


# convert a chromosome(string of binary characters) to its real value
def binary_to_real_p(c):
    global P_array_high, P_array_low, N_loadings_tj
    j = 0
    count = 0
    op = []

    for i in range(N_loadings_tj, len(c) + 1, N_loadings_tj):
        op.append(P_array_low[j] + ((P_array_high[j] - P_array_low[j]) / (pow(2, N_loadings_tj - 1)) * int(c[i - N_loadings_tj:i], 2)))
        count += 1
        if count == 96:
            count = 0
            j += 1

    return op


def binary_to_real_r(c):
    global N_fuel_allocation_factor_tj, number_of_generators_t
    op = []
    for i in range(N_fuel_allocation_factor_tj, len(c) + 1, N_fuel_allocation_factor_tj):
        op.append((1 / pow(2, N_fuel_allocation_factor_tj - 1)) * int(c[i - N_fuel_allocation_factor_tj:i], 2))

    return op


def heat_rate(p):
    global P_array_low
    a = [0.0586, 0.01172, 0.0069, 0.0069, 0.0114, 0.0035, 0.0016, 0.0009, 0.000052, 0.000052]
    b = [10.32, 10.32, 6.7378, 6.7378, 5.3519, 7.2038, 6.4352, 6.5651, 11.1222, 11.1222]
    c = [36.53, 18.27, 94.7055, 94.7055, 148.8907, 83.1773, 222.9258, 233.4006, 15.723, 15.723]
    e = [0, 0, 100, 100, 120, 120, 150, 150, 0, 0]
    f = [0, 0, 0.084, 0.084, 0.077, 0.077, 0.063, 0.063, 0, 0]

    op = []
    for i in range(len(p)):
        op.append((a[i % 10] * (p[i] ** 2)) + (b[i % 10] * p[i]) + c[i % 10] + abs(e[i % 10] * math.sin(f[i % 10] * (p[i] - P_array_low[i % 10]))))
    return op


# returns the objective function value for a given chromosome
def obj_function(c_p, c_r):
    array_p = binary_to_real_p(c_p)
    array_r = binary_to_real_r(c_r)
    # if sum(array_r) > 1:
    #     return -math.inf
    # else:
    array_heat_rate = [array_p[i] * array_r[i] for i in range(len(array_p))]
    array_heat_rate = heat_rate(array_heat_rate)
    op = sum(array_heat_rate)
    return -op


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


# takes population (1-d array of strings) and returns 2-d array (string, obj fn value)
def pop_obj(pop):
    half = len(pop[0]) // 2
    return [[i, obj_function(i[:half], i[half:])] for i in pop]


# Combine two arrays
def combine(pop1, pop2):
    return pop1 + pop2


# Split array into two
def split(pop):
    half = len(pop) // 2
    return pop[:half], pop[half:]


mating_pool_p = pop_generator(pop_size, chr_length_P)
# mating_pool_r = pop_generator(pop_size, chr_length_RHO)
# mating_pool = [mating_pool_p[i] + mating_pool_r[i] for i in range(len(mating_pool_r))]


best_p_1 = (min([i for i in pop_obj(mating_pool_p)], key=sort_key))
print(len(best_p_1[0]))
output_graph_x = []
output_graph_y = []


for i1 in range(N):
    mating_pool_p_1 = []
    mating_pool_p_2 = []
    mating_pool_p_3 = []
    # selection
    for _ in range(M):
        mating_pool_p_1.append(sel_roulette(pop_obj(mating_pool_p)))
    # cross-over (rate = 0.6)
    for _ in range(M):
        if random.random() <= crossover_rate:
            mating_pool_p_2.append(cross_two_pt(mating_pool_p_1[random.randint(0, M - 1)], mating_pool_p_1[random.randint(0, M - 1)]))
        else:
            mating_pool_p_2.append(mating_pool_p_1[random.randint(0, M - 1)])

    # mutation (rate = 0.1)
    for _ in range(M):
        k = random.randint(0, M - 1)
        if random.random() <= mutation_rate:
            mating_pool_p_3.append(mutation(mating_pool_p_2[k]))
        else:
            mating_pool_p_3.append(mating_pool_p_2[k])
    mating_pool_p = mating_pool_p_3
    best_p_2 = (min([i for i in pop_obj(mating_pool_p)], key=sort_key))
    if best_p_2[1] > best_p_1[1]:
        best_p_1 = best_p_2
    output_graph_x.append(i1+1)
    output_graph_y.append(best_p_1[1])
    print('best after ' + str(i1+1) + ' iteration ' + str(abs(best_p_2[1])), ', Overall Best: ' + str(abs(best_p_1[1])))

plt.style.use('ggplot')
plt.plot(output_graph_x, output_graph_y)
plt.grid(True)
plt.title("Genetic Algorithm")
plt.xlabel("Number of iterations")
plt.ylabel("Value of Objective Function")
plt.show()










