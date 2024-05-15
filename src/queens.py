def main():
    solutions = []
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    for m in range(8):
                        for n in range(8):
                            for o in range(8):
                                for p in range(8):
                                    if not check_columns(i, j, k, l, m, n, o, p):
                                        continue
                                    if not check_diagonals(i, j, k, l, m, n, o, p):
                                        continue
                                    solutions.append([i, j, k, l, m, n, o, p])

    return solutions

def check_columns(*args):
    return len(args) == len(set(args))

def check_diagonals(*args):
    return check_upper_diagonals(*args) and check_lower_diagonals(*args)

def check_upper_diagonals(*args):
    adjusted_values = [args[i] + i for i in range(len(args))]
    return len(adjusted_values) == len(set(adjusted_values))

def check_lower_diagonals(*args):
    adjusted_values = [args[i] - i for i in range(len(args))]
    return len(adjusted_values) == len(set(adjusted_values))


if __name__ == "__main__":
    solutions = main()
    for solution in solutions:
        print(solution)
