import colors

import pygame

BOARD_BORDER_WIDTH = 12
DIFFERENT_COLOR_BORDER_WIDTH = BOARD_BORDER_WIDTH // 2
SAME_COLOR_BORDER_WIDTH = BOARD_BORDER_WIDTH // 6


def draw_borders(squares, screen, row_index, column_index, grid_size, square_size):
    x = column_index * square_size
    y = row_index * square_size

    square = squares[row_index][column_index]

    if row_index != 0:
        top_square = squares[row_index - 1][column_index]

        if square.color == top_square.color:
            top_width = SAME_COLOR_BORDER_WIDTH
        else:
            top_width = DIFFERENT_COLOR_BORDER_WIDTH

    else:
        top_width = BOARD_BORDER_WIDTH

    if row_index < grid_size - 1:
        bottom_square = squares[row_index + 1][column_index]

        if square.color == bottom_square.color:
            bottom_width = SAME_COLOR_BORDER_WIDTH
        else:
            bottom_width = DIFFERENT_COLOR_BORDER_WIDTH

    else:
        bottom_width = BOARD_BORDER_WIDTH

    if column_index < grid_size - 1:
        right_square = squares[row_index][column_index + 1]

        if square.color == right_square.color:
            right_width = SAME_COLOR_BORDER_WIDTH
        else:
            right_width = DIFFERENT_COLOR_BORDER_WIDTH

    else:
        right_width = BOARD_BORDER_WIDTH

    if column_index != 0:
        left_square = squares[row_index][column_index - 1]

        if square.color == left_square.color:
            left_width = SAME_COLOR_BORDER_WIDTH
        else:
            left_width = DIFFERENT_COLOR_BORDER_WIDTH

    else:
        left_width = BOARD_BORDER_WIDTH

    pygame.draw.line(screen, colors.BLACK, (x, y), (x + square_size, y), top_width)
    pygame.draw.line(
        screen,
        colors.BLACK,
        (x, y + square_size),
        (x + square_size, y + square_size),
        bottom_width,
    )
    pygame.draw.line(
        screen,
        colors.BLACK,
        (x + square_size, y),
        (x + square_size, y + square_size),
        right_width,
    )
    pygame.draw.line(screen, colors.BLACK, (x, y), (x, y + square_size), left_width)
