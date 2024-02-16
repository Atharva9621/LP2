import pygame
import numpy as np
import random
from collections import namedtuple
import sys 

pygame.init()
font = pygame.font.SysFont('arial', 25)

class Grid:
    def __init__(self, grid=None, shape=None, width = 512, height = 512, fr=60, title="Grid Display"):
        self.WIDTH, self.HEIGHT = width, height
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()  

        self.FRAME_RATE = fr
        self.reset(grid, shape)

        self.colors = [(10, 10, 10), (200, 150, 150)]

    def reset(self, grid, shape):
        self.grid = grid
        self.shape = shape
        if self.shape == None:
            self.shape = (len(grid), len(grid[0]))
        self.cell_w = self.WIDTH/self.shape[1]
        self.cell_h = self.HEIGHT/self.shape[0]

    def color_cell(self, i, j) -> tuple:
        return self.colors[(i+j)%2]
    
    def draw_grid(self):
        rows, cols = self.shape[0], self.shape[1]
        cell_width, cell_height = self.WIDTH//cols, self.HEIGHT//rows
        padding = 0.05

        for row in range(rows):
            for col in range(cols):
                color = self.color_cell(row, col)
                pygame.draw.rect(self.display, color, (col*cell_width+padding, row*cell_height+padding, cell_width-2*padding, cell_height-2*padding))


    def draw_on_top(self):
        pass

    def draw(self):
        self.display.fill((0, 0, 0))
        self.draw_grid()
        self.draw_on_top()
        pygame.display.flip()
        
    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw()
            self.clock.tick(self.FRAME_RATE)


if __name__ == "__main__":
    game = Grid(width = 1240, height = 700, shape=(6, 10))
    game.run()