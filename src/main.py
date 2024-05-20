import pygame
import sys

from board import Board
import img

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

GRID_SIZE = 9

SQUARE_SIZE = SCREEN_WIDTH // GRID_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Queens")
icon = img.Image(file_name="queen.png")
icon_image = icon.image
pygame.display.set_icon(icon_image)

clock = pygame.time.Clock()
FPS = 60

board = Board(GRID_SIZE, SQUARE_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.update_square_fill(event.pos, event.button)

    board.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
