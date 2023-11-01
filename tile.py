import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/PC Computer - Evoland II - Bombable Rocks.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
