import random
from math import ceil, log2

"""GLOBAL VARIABLES"""
BOARD_SIDE_LENGTH = 4  # A square board is assumed

NUMBER_OF_ITERATIONS = 1000
MUTATION_BITS = 1
POPULATION_SIZE, SELECTION_SIZE = 10, 20
CROSSOVER_RATE, MUTATION_RATE = 0.6, 0.7

"""Initialize an NxN array to represent the square board.
A value of 0 represents empty space, and a value of 1 represents filled space.
Initially, the board is empty"""
BOARD = [[0] * BOARD_SIDE_LENGTH for i in range(BOARD_SIDE_LENGTH)]

BLOCK_DIMENSIONS = [(1, 1), (1, 1), (1, 1)]  # Array containing (width, height) of the blocks
UNIT_LENGTH = ceil(log2(BOARD_SIDE_LENGTH - 1))  # Bits used for one unit coordinate unit (X or Y)

"""For a board length of n, at least ceil(lg2(n)) bits are needed.
1 subtracted as 0-indexing scheme is used. 
Multiplied by 2 since there are two coordinates: x and y.
Finally, this is multiplied by the number of blocks."""

CHROMOSOME_LENGTH = UNIT_LENGTH * 2 * len(BLOCK_DIMENSIONS)


def binary_to_real(chromosome):
    """Convert chromosome with binary values to its real values
    Returns an array which contains positions of the top-left corner of each block as a tuple.
    Example: [(x1, y1), (x2, y2), ..., ]"""
    global UNIT_LENGTH
    output_array = []

    multiply = 0
    while (multiply + 2) * UNIT_LENGTH <= len(chromosome):
        x = chromosome[UNIT_LENGTH * multiply: UNIT_LENGTH * (multiply + 1)]
        y = chromosome[UNIT_LENGTH * (multiply + 1): UNIT_LENGTH * (multiply + 2)]
        output_array.append([int(x, 2), int(y, 2)])
        multiply += 2

    return output_array


def chromosome_generator(length):
    """Generate a random chromosome of the given length"""
    output_chromosome = ""
    for _ in range(length):
        if random.random() > 0.5:
            output_chromosome += "1"
        else:
            output_chromosome += "0"
    return output_chromosome


def population_generator(size, length):
    """Generates a population, or 1D array which contains string of chromosomes as elements
    Example - ['10001', '10010'] """

    population = []
    for _ in range(size):
        population.append(chromosome_generator(length))
    return population


def check_empty_space(board):
    """Returns the amount of empty space on the board
    Simply counts the number of 0s still present on the board"""

    cost = 0

    for row in board:
        for col in row:
            if col == 0:
                cost += 1

    return cost


def cost_function(chromosome):
    """Total cost is the sum of three costs:
        1. The amount of empty space on the board
        2. The amount of overlap between blocks
        3. The amount of block area which does not lie on the board

        The first two should be penalized more than the third cost.
        So, they've been multiplied by a factor of 5.
        """

    global BLOCK_DIMENSIONS, BOARD

    board_local = BOARD.copy()
    cost = 0
    real_values_array = binary_to_real(chromosome)

    def check_one_block(position, dimension):
        nonlocal cost

        x, y = position[0], position[1]
        width, height = dimension[0], dimension[1]

        for row in range(x, x + width):
            for col in range(y, y + height):
                if row > (BOARD_SIDE_LENGTH - 1) or col > (BOARD_SIDE_LENGTH - 1):
                    cost += max(0, row - (BOARD_SIDE_LENGTH - 1)) + max(0, col - (BOARD_SIDE_LENGTH - 1))
                else:
                    if board_local[row][col] == 0:
                        board_local[row][col] = 1
                    else:
                        cost += 1

    for block_position, dimensions in zip(real_values_array, BLOCK_DIMENSIONS):
        check_one_block(block_position, dimensions)

    # return -(5 * cost + check_empty_space(board_local))
    return -cost


def population_fitness(population):
    """Takes in the array of the entire population.
    Returns a 2D array of the form [chromosome, fitness score] for entire population"""
    return [[chromosome, cost_function(chromosome)] for chromosome in population]


def crossover_one(chr1, chr2):
    """Returns a crossed chromosome after performing one point crossover"""
    p = random.randint(0, len(chr1) - 1)
    o1 = chr1[:p] + chr2[p:]
    return o1


def crossover_two(chr1, chr2):
    """Returns a crossed chromosome after performing two point crossover"""
    p1, p2 = random.randint(0, len(chr1) - 1), random.randint(0, len(chr1) - 1)
    p1, p2 = min(p1, p2), max(p1, p2)
    o1 = chr1[:p1] + chr2[p1:p2] + chr1[p2:]
    return o1


def crossover_uniform(chr1, chr2):
    """Returns a crossed chromosomes after performing uniform crossover"""
    o1 = ''
    for i in range(len(chr1)):
        if random.random() > 0.5:
            o1 += chr1[i]
        else:
            o1 += chr2[i]
    return o1


def mutation(chromosome):
    """Returns a chromosome after mutating the specified number of bits"""
    output_chromosome = ''
    mut_b = [random.randint(0, len(chromosome) - 1) for i in range(MUTATION_BITS)]
    for i in range(len(chromosome)):
        if i in mut_b:
            output_chromosome += str(1 - int(chromosome[i]))
        else:
            output_chromosome += chromosome[i]
    return output_chromosome


def selection_tournament(pop_fitness, n):
    """Takes population of chromosome (with their fitness scores) and tournament size.
     Returns the best individual after tournament selection"""
    return max([pop_fitness[random.randint(0, len(pop_fitness) - 1)] for i in range(n)], key=lambda x: x[1])[0]


def selection_roulette(pop_fitness):
    """Takes population (with fitness) and returns a single individual"""
    total = sum(i[1] for i in pop_fitness)
    p = [i[0] for i in pop_fitness]
    w = [i[1] / total for i in pop_fitness]
    op = (random.choices(p, weights=w))[0]
    return op


def selection_ranking(pop_fitness):
    """Takes population of chromosome (with their fitness scores).
    Returns the best individual after ranking selection"""
    n = len(pop_fitness)
    total = n * (n + 1) / 2
    p1 = sorted(pop_fitness, key=lambda x: x[1])
    p = [i[0] for i in p1]
    w = [(i + 1) / total for i in range(len(p1))]
    op = (random.choices(p, weights=w))[0]
    return op


"""Parallelize from here"""
mating_pool = population_generator(POPULATION_SIZE, CHROMOSOME_LENGTH)
best1 = (max([i for i in population_fitness(mating_pool)], key=lambda x: x[1]))
output_graph_x = []
output_graph_y = []

for i1 in range(NUMBER_OF_ITERATIONS):
    mating_pool1 = []
    mating_pool2 = []
    mating_pool3 = []

    # selection
    for _ in range(SELECTION_SIZE):
        mating_pool1.append(selection_roulette(population_fitness(mating_pool)))

    # cross-over (rate = 0.6)
    for _ in range(SELECTION_SIZE):
        if random.random() <= CROSSOVER_RATE:
            mating_pool2.append(crossover_two(mating_pool1[random.randint(0, SELECTION_SIZE - 1)], mating_pool1[random.randint(0, SELECTION_SIZE - 1)]))
        else:
            mating_pool2.append(mating_pool1[random.randint(0, SELECTION_SIZE - 1)])

    # mutation (rate = 0.1)
    for _ in range(SELECTION_SIZE):
        k = random.randint(0, SELECTION_SIZE - 1)
        if random.random() <= MUTATION_RATE:
            mating_pool3.append(mutation(mating_pool2[k]))
        else:
            mating_pool3.append(mating_pool2[k])

    mating_pool = mating_pool3

    best2 = (max([i for i in population_fitness(mating_pool)], key=lambda x: x[1]))

    if best2[1] > best1[1]:
        best1 = best2

    output_graph_x.append(i1+1)
    output_graph_y.append(best1[1])

    print('best after ' + str(i1+1) + ' iteration ' + str(abs(best2[1])), ', Overall Best: ' + str(abs(best1[1])))