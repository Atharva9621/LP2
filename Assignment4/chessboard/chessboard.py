from .grid import Grid
import pygame
import os
DIR = os.path.dirname(__file__)

class Chessboard(Grid):

    def __init__(self, grid=None, shape=None, width=512, height=512, fr=60, title="Grid Display"):
        super().__init__(grid, shape, width, height, fr, title)
        self.queen = pygame.image.load(os.path.join(DIR, 'queen.png'))
        self.side = self.cell_w
        self.colors = [(10, 10, 10), (200, 200, 100)]

    def draw_on_top(self):
        rows, cols = self.shape[0], self.shape[1]
        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col] == 1:
                    self.display.blit(pygame.transform.scale(self.queen, (self.side, self.side)), (row*self.side, col*self.side, ))