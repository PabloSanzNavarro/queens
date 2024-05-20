import itertools
import random

import colors
from squares import Square
import borders

class Board:
    def __init__(self, grid_size, square_size):
        self.grid_size = grid_size
        self.square_size = square_size
        
        self.get_board_solution()
        self.generate_squares()

    def draw(self, screen):
        self.draw_squares(screen)
        self.draw_borders(screen)

    def draw_squares(self, screen):
        for row in self.squares:
            for square in row:
                square.draw(screen)
    
    def draw_borders(self, screen):
        for row_index, row in enumerate(self.squares):
            for column_index, square in enumerate(row): 
                borders.draw_borders(
                    self.squares, screen, row_index, column_index, self.grid_size, self.square_size
                )

    def get_board_solution(self):

        def check_diagonals(combination):
            for i in range(len(combination) - 1):
                if combination[i] == combination[i + 1] + 1:
                    return False
                if combination[i] == combination[i + 1] - 1:
                    return False
            return True
    
        combinations = list(itertools.permutations(range(self.grid_size), r=self.grid_size))
        solutions = []

        for combination in combinations:
            combination = list(combination)
            if not check_diagonals(combination):
                continue
            solutions.append(combination)

        self.board_solution = random.choice(solutions)
    
    def generate_squares(self):
        self.squares = list()

        queen_colors = list(colors.colors_dict.values())

        for row in range(self.grid_size):
            square_row = []
            for column in range(self.grid_size):
                x = column * self.square_size
                y = row * self.square_size
                color = colors.WHITE
                fill = None

                if self.board_solution[row] == column:
                    fill = "queen"
                    color = random.choice(queen_colors)
                    queen_colors.remove(color)

                square = Square(x, y, self.square_size, color, fill)

                square_row.append(square)

            self.squares.append(square_row)

        self.fill_square_colors()

    def fill_square_colors(self):

        non_filled = list()
        filled = list()

        for row_index, row in enumerate(self.squares):
            for column_index, column in enumerate(row):
                square = self.squares[row_index][column_index]

                if square.fill == "queen":
                    filled.append((row_index, column_index))
                else:
                    non_filled.append((row_index, column_index))

        while non_filled:
            neighbors = list()
            row_index, column_index = random.choice(non_filled)

            top = row_index + 1, column_index
            bottom = row_index - 1, column_index
            right = row_index, column_index + 1
            left = row_index, column_index - 1

            if top in filled:
                neighbors.append(top)
            if bottom in filled:
                neighbors.append(bottom)
            if right in filled:
                neighbors.append(right)
            if left in filled:
                neighbors.append(left)

            if not neighbors:
                continue

            new_color_row, new_color_column = random.choice(neighbors)

            self.squares[row_index][column_index].color = self.squares[new_color_row][
                new_color_column
            ].color

            non_filled.remove((row_index, column_index))
            filled.append((row_index, column_index))

        self.clear_squares_fill()

    def clear_squares_fill(self):
        for row in self.squares:
            for square in row:
                square.fill = None

    def update_square_fill(self, mouse_pos, mouse_button):
        for row in self.squares:
            for square in row:
                if square.collidepoint(mouse_pos):
                    square.update_fill(mouse_button)
    