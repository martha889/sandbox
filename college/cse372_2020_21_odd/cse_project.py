import random
import math

board_side_length = 5

"""Initialize an NxN array to represent the square board.
A value of 0 represents empty space, and a value of 1 represents filled space.
Initially, the board is empty"""
board = [[0] * board_side_length for i in range(board_side_length)]

block_dimensions = [(2, 3)]  # Array containing (width, height) of the blocks

"""For a board length of n, at least lg(n) + 1 bits are needed.
1 subtracted as 0-indexing scheme is used. 
Multiplied by 2 since there are two coordinates: x and y.
Finally, this is multiplied by the number of blocks."""
chromosome_length = (int(math.log2(board_side_length - 1)) + 1) * 2 * len(block_dimensions)


def binary_to_real(chromosome):
    """Convert chromosome with binary values to its real values
    Returns an array which contains positions of the top-right corner of each block as a tuple.
    Example: [(x1, y1), (x2, y2), ..., ]"""

    output_string = ""
    output_array = []
    i = 0
    while i + 2 <= len(chromosome):
        output_string += str(int(chromosome[i: i + 2], 2))
        i += 2

    j = 0

    while j + 1 < len(output_array):
        output_array.append((int(output_string[j]), int(output_string[j+1])))
        j += 2

    return output_array


def chromosome_generator(length):
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


def check_board(chromosome):
    """Check if the given positions of blocks lie on the board:
    return True if yes, else return False"""

    global block_dimensions
    block_positions = binary_to_real(chromosome)
    flag = True

    for i in range(len(block_positions)):
        if (block_positions[i][0] - block_dimensions[i][0] < 0) or (block_positions[i][1] - block_dimensions[i][1] < 0):
            flag = False
            break

    return flag


def check_overlap(chromosome):
    """Check if there is overlapping of blocks.
    return True if yes, else return False"""

    global N, block_dimensions
    occupied_positions = set()
    real_values = binary_to_real(chromosome)

    for i in range(len(real_values)):
        x, y = real_values[i][0], real_values[i][1]
        dx, dy = block_dimensions[i][0] - 1, block_dimensions[i][1] - 1

        while dx >= 0:
            while dy >= 0:
                to_be_added = (x - dx, y - dy)

                if to_be_added in occupied_positions:
                    return False

                occupied_positions.add(to_be_added)
                dy -= 1
            dy = block_dimensions[i][1] - 1
            dx -= 1

    return True








