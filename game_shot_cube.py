#! /usr/bin/env python
import sys , os , math , random
from random import randint
import pygame
from pygame. locals import *

import Box
from  Box import *

import box_groups # Importa o arquivo
from  box_groups import * # Importa as classes do arquivo

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

def draw_lines():
    #print("Drawing lines ...")
    box_lines = box_group.get_box_lines()
    px = 0
    py = 0
    size = 30
    # Calculate the space 
    space = (screen_width - (box_group.box_ammount * size))/box_group.box_ammount
    countdown = (len(box_lines)-1)
    while countdown >= 0:
        for color_index in box_lines[countdown]:
            b = Box(screen, box_group.get_color(color_index), size, (px,py))
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

    draw_lines()

    time_tick = clock.tick()
    current_time += time_tick
    if current_time > (max_time * 1000):
        box_group.feed_box_lines()
        current_time = 0

    # Atualizacao da tela
    pygame.display.update()