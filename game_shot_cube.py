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
vehicle = Vehicle(screen)
# Bullet object
bullet = Bullet(screen, box_group)


def draw_lines(py):
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
                    box_item["show"] = 0
                    break

                #bullet.feed_obstacle(b.get_rect()) # Adding bullet ostable
            px = px + size + space
        px = 0
        py = py + size + space
        countdown = countdown - 1

# palco
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    # Tela
    screen.fill((0, 0, 0))

    # Drawing top bar    
    top_bar_height = 40
    top_bar = pygame.draw.rect(screen, (147, 184, 116), (0,0,screen_width,top_bar_height))

    # Drawing bottom bar
    bottom_bar_height = 25
    bottom_bar_py = (screen_height - bottom_bar_height)
    bottom_bar = pygame.draw.rect(screen, (147, 184, 116), (0,bottom_bar_py,screen_width,bottom_bar_height))

    # Drawing the bullet
    bullet_size = 5
    bullet.draw_bullet(vehicle, event, (255,0,0), bullet_size)    

    # Drawing the vehicle
    vehicle_width = 35
    vehicle_height = 25
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