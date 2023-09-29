import pygame
from random import randrange

class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.bbloc = pygame.rect.Rect([0, 0, game.TILE_SIZE, game.TILE_SIZE])
        self.bbloc.center = self.random_pos()

    def random_pos(self):
        return [randrange(self.size//2, self.game.WIDTH - self.size//2, self.size),
                randrange(self.size//2, self.game.HEIGHT - self.size//2, self.size)]

    def draw(self):
        pygame.draw.rect(self.game.WINDOW, 'red', self.bbloc)