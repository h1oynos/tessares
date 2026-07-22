import pygame
import pygame_gui as gui
import numpy as np

import gamevars as gv

from visual import particles as part

# Setting up Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
manager = gui.UIManager((1280, 720))
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
                self.rotations = [
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
                self.rotations = [
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
                self.rotations = [
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
                self.rotations = [
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
                self.rotations = [
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
                self.rotations = [
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
                self.rotations = [
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
                     [0, -7, 0, 0]]
                ]

# Key Frame Timers
left_held_time = 0
right_held_time = 0
up_held_time = 0
down_held_time = 0

while running:
    # Event Polling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # match event.key:
            #     case pygame.K_KP4:
            #         print("Left Pressed")
            #     case pygame.K_KP5:
            #         print("Soft Drop Pressed")
            #     case pygame.K_KP6:
            #         print("Right Pressed")
            #     case pygame.K_KP8:
            #         print("Hard Drop Pressed")
            #     case pygame.K_a:
            #         print("Rotate CCW Pressed")
            #     case pygame.K_s:
            #         print("Rotate CW Pressed")
            #     case pygame.K_d:
            #         print("Hold Pressed")
            if event.key == pygame.K_KP4 or event.key == pygame.K_LEFT:
                print("Left Pressed")
                left_held_time += 1
            else:
                left_held_time = 0
            if event.key == pygame.K_KP5 or event.key == pygame.K_DOWN:
                print("Soft Drop Pressed")
                down_held_time += 1
            else: 
                down_held_time = 0
            if event.key == pygame.K_KP6 or event.key == pygame.K_RIGHT:
                print("Right Pressed")
                right_held_time += 1
            else:
                right_held_time = 0
            if event.key == pygame.K_KP2 or event.key == pygame.K_UP:
                print("Hard Drop Pressed")
                up_held_time += 1
            else:
                up_held_time = 0
            if event.key == pygame.K_a or event.key == pygame.K_z:
                print("CCW Rotation Pressed")
            if event.key == pygame.K_s or event.key == pygame.K_x:
                print("CW Rotation Pressed")
            if event.key == pygame.K_d or event.key == pygame.K_c:
                print("Hold pressed")
            


    screen.fill((0, 0, 0))

    ## Begin Rendering Loop 

    draw_matrix()
    manager.draw_ui(screen)

    ## End Rendering Loop

    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()