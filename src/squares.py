import pygame

import img

class Square:
    def __init__(self, x, y, size, color, fill=None):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.fill = fill

        queen_scale_factor = 1.5
        queen = img.Image(file_name="queen.png", square_size=self.size, scale_factor=queen_scale_factor)
        self.queen_img = queen.image
        self.queen_rect = queen.rectangle

        cross_scale_factor = 4
        cross = img.Image(file_name="cross.png", square_size=self.size, scale_factor=cross_scale_factor)
        self.cross_img = cross.image
        self.cross_rect = cross.rectangle

        self.centre_coords = (
            self.x + (self.size // 2),
            self.y + (self.size // 2)
        )

    def draw(self, screen):
        self.draw_color(screen)
        self.draw_fill(screen)
    
    def draw_color(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)

    def draw_fill(self, screen):
        if not self.fill:
            return
        
        if self.fill == "queen":
            self.queen_rect.center = self.centre_coords
            screen.blit(self.queen_img, self.queen_rect)
        
        if self.fill == "cross":
            self.cross_rect.center = self.centre_coords
            screen.blit(self.cross_img, self.cross_rect)

    def collidepoint(self, point):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return rect.collidepoint(point)
    
    def update_fill(self, mouse_button):
        if mouse_button == 1: # Right click
            if self.fill != "queen":
                self.fill = "queen"
            else:
                self.fill = None

        if mouse_button == 3: # Left click
            if self.fill != "cross":
                self.fill = "cross"
            else:
                self.fill = None
