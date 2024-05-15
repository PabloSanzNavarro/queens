import itertools

def main(n):
    for i in range(1, n + 1):
        combinations = list(itertools.permutations(range(i), r=i))
        solutions = []
        
        for combination in combinations:
            combination = list(combination)
            if not check_diagonals(combination):
                continue
            solutions.append(combination)
        print(f"n: {i}. Soluciones: {len(solutions)}")

def check_diagonals(combination):
    return check_upper_diagonals(combination) and check_lower_diagonals(combination)

def check_upper_diagonals(combination):
    adjusted_values = [combination[i] + i for i in range(len(combination))]
    return len(adjusted_values) == len(set(adjusted_values))

def check_lower_diagonals(combination):
    adjusted_values = [combination[i] - i for i in range(len(combination))]
    return len(adjusted_values) == len(set(adjusted_values))


if __name__ == "__main__":
    main(n=20)
