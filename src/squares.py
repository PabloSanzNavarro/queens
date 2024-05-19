import random

import pygame

import colors

class Square:
    def __init__(self, x, y, size, color, fill=None):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.fill = fill

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)


def generate_squares(grid_size, square_size, solution):
    squares = list()

    queen_colors = list(colors.colors_dict.values())

    for row in range(grid_size):
        square_row = []
        for column in range(grid_size):
            x = column * square_size
            y = row * square_size
            color = colors.WHITE

            fill = None
            
            if solution[row] == column:
                fill = "queen"
                color = random.choice(queen_colors)
                queen_colors.remove(color)
            
            square = Square(x, y, square_size, color, fill)
        
            square_row.append(square)

        squares.append(square_row)

    squares = fill_square_colors(squares)
    
    return squares


def fill_square_colors(squares):
    
    non_filled = list()
    filled = list()

    for row_index, row in enumerate(squares):
        for column_index, column in enumerate(row):
            square = squares[row_index][column_index]

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
        left = row_index, column_index -1

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

        squares[row_index][column_index].color = squares[new_color_row][new_color_column].color
 
        non_filled.remove((row_index, column_index))
        filled.append((row_index, column_index))

    for row in squares:
        for square in row:
            square.fill = None

    return squares


