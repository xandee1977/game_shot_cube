#! /usr/bin/env python
import sys , os , math , random
from random import randint
import pygame
from pygame. locals import *

import game_elements
from  game_elements import *

import box_groups # Importa o arquivo
from  box_groups import * # Importa as classes do arquivo

# Vehicle movements
initial_move = 0

pygame.init();

# Settings
base_path, filename = os.path.split(os.path.abspath(__file__))
# BG
background = pygame.image.load(base_path + '/img/background.jpg')

# Box groups
box_group = box_groups() # Box Group Object
box_group.feed_box_lines() # First line feed

# Time control
current_time = 0
max_time  = 4 # Time to update
clock = pygame.time.Clock()

running = 1

screen_width = 320
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

# Vehicle object
vehicle = Vehicle(screen, base_path)
# Bullet object
bullet = Bullet(screen, box_group)


# texto do box
text_bold = True
text_font = pygame.font.SysFont("Arial", 20, text_bold)
game_score = 0

def draw_lines(py):
    global game_score

    #print("Drawing lines ...")
    box_lines = box_group.get_box_lines()
    px = 0
    py = py + 2
    size = 30
    # Calculate the space 
    space = (screen_width - (box_group.box_ammount * size))/box_group.box_ammount
    countdown = (len(box_lines)-1)
    while countdown >= 0:
        for box_item in box_lines[countdown]:
            # Show only visibles boxes
            if(box_item["show"] == 1):
                b = Box(screen, box_group.get_color(box_item["color"]), size, (px,py))
                box_item["rect"] = b.get_rect()
                if(box_item["rect"].colliderect(bullet.rect)):
                    game_score += box_item["point"]
                    box_item["show"] = 0
                    break

                #bullet.feed_obstacle(b.get_rect()) # Adding bullet ostable
            px = px + size + space
        px = 0
        py = py + size + space
        countdown = countdown - 1

# palco
while running:
    print(game_score)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    # Tela
    #screen.fill((0, 0, 0))
    screen.blit(background, background.get_rect())

    # Drawing top bar    
    top_bar_height = 40
    top_bar = pygame.draw.rect(screen, (38, 81, 118), (0,0,screen_width,top_bar_height))

    # labels dos box
    score_label = text_font.render("Score: " + str(game_score), 48, (255,255,255))
    screen.blit(score_label, ((screen_width-80, 10)))

    # Drawing bottom bar
    bottom_bar_height = 25
    bottom_bar_py = (screen_height - bottom_bar_height)
    bottom_bar = pygame.draw.rect(screen, (38, 81, 118), (0,bottom_bar_py,screen_width,bottom_bar_height))

    # Drawing the bullet
    bullet_size = 5
    bullet.draw_bullet(vehicle, event, (255,255,255), bullet_size)    

    # Drawing the vehicle
    vehicle_width = 40
    vehicle_height = 45
    vehicle_py = bottom_bar_py  - bottom_bar_height - 2
    vehicle.draw_vehicle(event, (211, 153, 64), vehicle_width, vehicle_height, (vehicle.get_pos_x(),vehicle_py))

    # Drawing lines
    draw_lines(top_bar_height)

    time_tick = clock.tick()
    current_time += time_tick
    if current_time > (max_time * 1000):
        box_group.feed_box_lines()
        current_time = 0

    # Atualizacao da tela
    pygame.display.update()