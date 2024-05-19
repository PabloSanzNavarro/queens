import itertools
import random


def get_solution():
    combinations = list(itertools.permutations(range(9), r=9))
    solutions = []

    for combination in combinations:
        combination = list(combination)
        if not check_diagonals(combination):
            continue
        solutions.append(combination)

    return random.choice(solutions)


def check_diagonals(combination):
    for i in range(len(combination) - 1):
        if combination[i] == combination[i + 1] + 1:
            return False
        if combination[i] == combination[i + 1] - 1:
            return False
    return True
