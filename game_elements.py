#! /usr/bin/env python
import sys , os , math , random
from random import randint
import pygame
from pygame. locals import *

VEHICLE_MOVE_LEFT=1
VEHICLE_MOVE_STOP=0
VEHICLE_MOVE_RIGHT=2

# Box
class Box(pygame.sprite.Sprite):
    rect = None

    def __init__ (self, surface, color, size, position):
        pos_x, pos_y = position
        self.rect = pygame.draw.rect(surface, color, (pos_x,pos_y,size,size))

        #self.image = pygame.image.load( base_path + '/img/box.jpg' )
        #self.image.set_clip(pygame.Rect(0, 0, 48, 48))
        #self.rect = self.image.get_rect()
        #self.rect.topleft = position
    def get_rect(self):
        return self.rect

# Bullet
class Bullet(pygame.sprite.Sprite):
    rect = None # rectangle
    fire = False # Fires flag
    move_factor = 1
    move_length = 0
    # Sizing and position   
    size,pos_x,pos_y = (0,0,0)

    def __init__ (self, surface, box_group):
        self.surface = surface
        self.box_group = box_group

    def draw_bullet(self, vehicle, event, color, size):
        self.size = size
        self.color = color
        
        if(self.fire == True):
            self.move_length = self.move_length - self.move_factor
            for box_line in self.box_group.box_lines:
                for box_item in box_line:
                    if(self.rect != None and box_item["rect"] != None):
                        if(box_item["rect"].colliderect(self.rect)):
                            self.fire = False
        else:
            self.move_length = 0

        self.pos_x = vehicle.get_pos_x() + ((vehicle.width-self.size)/2)
        self.pos_y = (vehicle.get_pos_y()) + self.move_length

        if event.type == KEYDOWN:
            if (event.key == K_s):
                self.do_fire()

        bullet = Box(self.surface, self.color, self.size, (self.pos_x,self.pos_y))
        self.rect = bullet.get_rect()
    
    def do_fire(self):
        self.fire = True

# Vehicle
class Vehicle(pygame.sprite.Sprite):
    rect = None

    current_move = 0
    surface = None
    pos_x = 0
    pos_y = 0
    width = 0
    height = 0    
    move_factor = 0.5 # Fator de movimento
    
    def __init__ (self, surface, base_path):
        self.surface = surface
        self.base_path = base_path

    def draw_vehicle(self, event, color, width, height, position):
        self.pos_x, self.pos_y = position
        self.width = width
        self.height = height
        
        self.image = pygame.image.load( self.base_path + '/img/spaceship.png' )
        self.image.set_clip(pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))


        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                self.current_move = VEHICLE_MOVE_LEFT
            elif (event.key == K_RIGHT):
                self.current_move = VEHICLE_MOVE_RIGHT
        elif event.type == KEYUP:
            self.current_move = VEHICLE_MOVE_STOP

        if self.current_move == VEHICLE_MOVE_LEFT:
            self.pos_x-=self.move_factor
        elif self.current_move == VEHICLE_MOVE_RIGHT:
            self.pos_x+=self.move_factor
        else:
            self.pos_x = self.pos_x

        #self.rect = pygame.draw.rect(self.surface, color, (self.pos_x,self.pos_y,width,height))

        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.surface.blit(self.image, self.rect)


    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_rect(self):
        return self.rect        