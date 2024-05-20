import os

import pygame

import env

class Image:
    def __init__(self, file_name, square_size=None, scale_factor=None):
        self.path = os.path.join(env.get_img_dir(), file_name)
        self.square_size = square_size
        self.scale_factor = scale_factor

        self.get_image()
        self.get_rectangle()

    def get_image(self):
        self.image = pygame.image.load(self.path)

        if self.square_size and self.scale_factor:
            self.rescale_image()

    def rescale_image(self):
        image_width = self.square_size // self.scale_factor
        image_heigh = self.square_size // self.scale_factor
        self.image = pygame.transform.scale(self.image, (image_width, image_heigh))

    def get_rectangle(self):
        self.rectangle = self.image.get_rect()
