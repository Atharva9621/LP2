# import pygame
# import numpy as np
# import random
# from collections import namedtuple
# import sys 

# pygame.init()
# font = pygame.font.SysFont('arial', 25)

# class Grid:
#     FRAME_RATE = 60
#     WIDTH = 512
#     HEIGHT = 512
#     def __init__(self, grid, shape, fr=60):
#         self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
#         pygame.display.set_caption('Frozen Lake')
#         self.clock = pygame.time.Clock()  
#         self.reset(grid, shape)

#     def reset(self, grid, shape):
#         self.grid = grid
#         self.shape = shape
#         if self.shape == None:
#             self.shape = (len(grid), len(grid[0]))
#             print(f'Shape: {self.shape}')

#     def draw(self):
#         self.display.fill((0, 0, 0))
#         rows = self.shape[0]
#         cols = self.shape[1]
#         cell_width = self.WIDTH//cols
#         cell_height = self.HEIGHT//rows
#         padding = 0.05

#         for row in range(rows):
#             for col in range(cols):
#                 print(f'Drawinf row {row} col {col} ')
#                 if(row+col)%2 == 0:
#                     color = (30, 30, 160)
#                 else:
#                     color = (50, 50, 180)
#                 if self.grid[row][col]==1:
#                     color = (255, 180, 180)
#                 pygame.draw.rect(self.display, color, (col*cell_width+padding, row*cell_height+padding, cell_width-2*padding, cell_height-2*padding))

#         pygame.display.flip()

#     def run(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#             self.draw()
#             self.clock.tick(self.FRAME_RATE)

# # if __name__ == "__main__":
# #     grid = [
# # [1, 1, 1, 1, 1, 1, 1],
# # [1, 0, 0, 0, 0, 0, 1],
# # [1, 0, 0, 0, 0, 0, 1],
# # [1, 0, 0, 0, 0, 0, 1],
# # [1, 0, 0, 0, 0, 0, 1],
# # [1, 0, 0, 1, 0, 0, 1],
# # [1, 0, 2, 2, 2, 0, 1],
# # [1, 0, 0, 1, 0, 0, 1],
# # [1, 1, 1, 1, 1, 1, 1]]
# #     game = FrozenLake(grid, None)
# #     game.run()