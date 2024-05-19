import pygame
import sys

from squares import generate_squares
import borders
import colors
import queens

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Queens")

clock = pygame.time.Clock()
FPS = 60

GRID_SIZE = 9

SQUARE_SIZE = SCREEN_WIDTH // GRID_SIZE

solution = queens.get_solution()

squares = generate_squares(GRID_SIZE, SQUARE_SIZE, solution)

IMAGE_WIDTH = SQUARE_SIZE
IMAGE_HEIGHT = SQUARE_SIZE

queen_image = pygame.image.load(
    r"C:\Users\pablodorye.sanz\Desktop\Queens\img\queen.png"
)
queen_image = pygame.transform.scale(
    queen_image, (IMAGE_WIDTH // 1.5, IMAGE_HEIGHT // 1.5)
)
queen_rect = queen_image.get_rect()

cross_image = pygame.image.load(
    r"C:\Users\pablodorye.sanz\Desktop\Queens\img\cross.png"
)
cross_image = pygame.transform.scale(cross_image, (IMAGE_WIDTH // 4, IMAGE_HEIGHT // 4))
cross_rect = cross_image.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(colors.BLACK)

    for row_index, row in enumerate(squares):
        for column_index, square in enumerate(row):
            square.draw(screen)
            borders.draw_borders(
                squares, screen, row_index, column_index, GRID_SIZE, SQUARE_SIZE
            )

            if square.fill == "queen":
                queen_rect.center = (
                    square.x + (SQUARE_SIZE // 2),
                    square.y + (SQUARE_SIZE // 2),
                )
                screen.blit(queen_image, queen_rect)

            if square.fill == "cross":
                cross_rect.center = (
                    square.x + (SQUARE_SIZE // 2),
                    square.y + (SQUARE_SIZE // 2),
                )
                screen.blit(cross_image, cross_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
