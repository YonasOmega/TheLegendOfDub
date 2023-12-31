import pygame, sys
from settings import *
from level import Level
from player import Player


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Dungeon Adventure')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.grass_surface = pygame.image.load('../Assets/Backgrounds/Tilesets/ground.png')
        self.grass_surface = pygame.transform.scale(self.grass_surface, (WIDTH, HEIGHT))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.screen.blit(self.grass_surface, (0, 0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
