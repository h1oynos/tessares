import pygame
import pygame_gui as gui
import numpy as np


# Setting up Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Setting up the game

matrix = np.zeros((22, 10))
def draw_matrix():
    row_no = 0
    cell_no = 0
    for row in matrix:
        cell_no = 0
        row_pixels_added = row_no * 25 # Number of pixels to shift down the Y position of the cell
        for cell in row:
            cell_pixels_added = cell_no * 25 # Number of pixels to shift right the X position of the cell
            match cell:
                case 0: # Empty Cell
                    if row_no < 2:
                        break
                    pygame.draw.rect(screen, pygame.Color(46, 40, 42), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case 1: # L
                    pygame.draw.rect(screen, pygame.Color(186, 92, 18), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case 2: # J
                    pygame.draw.rect(screen, pygame.Color(30, 56, 136), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case 3: # S
                    pygame.draw.rect(screen, pygame.Color(255, 209, 102), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case 4: # Z
                    pygame.draw.rect(screen, pygame.Color(226, 52, 40), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case 5: # O
                    pygame.draw.rect(screen, pygame.Color(214, 190, 31), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case 6: # I
                    pygame.draw.rect(screen, pygame.Color(71, 168, 189), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case 7: # T
                    pygame.draw.rect(screen, pygame.Color(157+20, 105+20, 163+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case -1: # Active L
                    pygame.draw.rect(screen, pygame.Color(186+20, 92+20, 18+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case -2: # Active J
                    pygame.draw.rect(screen, pygame.Color(30+20, 56+20, 136+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case -3: # Active S
                    pygame.draw.rect(screen, pygame.Color(255+20, 209+20, 102+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case -4: # Active Z
                    pygame.draw.rect(screen, pygame.Color(226+20, 52+20, 40+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case -5: # Active O
                    pygame.draw.rect(screen, pygame.Color(214+20, 190+20, 31+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case -6: # Active I
                    pygame.draw.rect(screen, pygame.Color(71+20, 168+20, 189+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))
                case -7: # Active T
                    pygame.draw.rect(screen, pygame.Color(157+20, 105+20, 163+20), pygame.rect.FRect(200+cell_pixels_added, 50+row_pixels_added, 24, 24))

                
            cell_no += 1
        row_no += 1

class Piece:
    def __init__(self, shape):
        self.type = shape
        match shape:
            case 1: # L
                [
                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [-1, -1, -1, 0],
                     [-1, 0, 0, 0]],

                    [[0, 0, 0, 0],
                     [-1, -1, 0, 0],
                     [0, -1, 0, 0],
                     [0, -1, 0, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, -1, 0],
                     [-1, -1, -1, 0]],

                    [[0, 0, 0, 0],
                     [0, -1, 0, 0],
                     [0, -1, 0, 0],
                     [0, -1, -1, 0]]
                ]
            case 2: # J
                [
                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [-2, -2, -2, 0],
                     [0, 0, -2, 0]],

                    [[0, 0, 0, 0],
                     [0, -2, 0, 0],
                     [0, -2, 0, 0],
                     [-2, -2, 0, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [-2, 0, 0, 0],
                     [-2, -2, -2, 0]],

                    [[0, 0, 0, 0],
                     [0, -2, -2, 0],
                     [0, -2, 0, 0],
                     [0, -2, 0, 0]]
                ]
            case 3: # S
                [
                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, -3, -3, 0],
                     [-3, -3, 0, 0]],

                    [[0, 0, 0, 0],
                     [-3, 0, 0, 0],
                     [-3, -3, 0, 0],
                     [0, -3, 0, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, -3, -3, 0],
                     [-3, -3, 0, 0]],

                    [[0, 0, 0, 0],
                     [-3, 0, 0, 0],
                     [-3, -3, 0, 0],
                     [0, -3, 0, 0]]
                ]
            case 4: # Z
                [
                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [-4, -4, 0, 0],
                     [0, -4, -4, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, -4, 0],
                     [0, -4, -4, 0],
                     [0, -4, 0, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [-4, -4, 0, 0],
                     [0, -4, -4, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, -4, 0],
                     [0, -4, -4, 0],
                     [0, -4, 0, 0]]
                ]
            case 5: # O
                [
                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, -5, -5, 0],
                     [0, -5, -5, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, -5, -5, 0],
                     [0, -5, -5, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, -5, -5, 0],
                     [0, -5, -5, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, -5, -5, 0],
                     [0, -5, -5, 0]]
                ]
            case 6: # I
                [
                    [[0, 0, 0, 0],
                     [-6, -6, -6, -6],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],

                    [[0, 0, -6, 0],
                     [0, 0, -6, 0],
                     [0, 0, -6, 0],
                     [0, 0, -6, 0]],

                    [[0, 0, 0, 0],
                     [-6, -6, -6, -6],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],

                    [[0, 0, -6, 0],
                     [0, 0, -6, 0],
                     [0, 0, -6, 0],
                     [0, 0, -6, 0]]
                ]
            case 7: # T
                [
                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [-7, -7, -7, 0],
                     [0, -7, 0, 0]],

                    [[0, 0, 0, 0],
                     [0, -7, 0, 0],
                     [-7, -7, 0, 0],
                     [0, -7, 0, 0]],

                    [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, -7, 0, 0],
                     [-7, -7, -7, 0]],

                    [[0, 0, 0, 0],
                     [0, -7, 0, 0],
                     [0, -7, -7, 0],
                     [0, -7, 0, 0]
                ]
                ]

while running:
    # Event Polling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    ## Begin Rendering Loop 

    draw_matrix()
    ## End Rendering Loop

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()