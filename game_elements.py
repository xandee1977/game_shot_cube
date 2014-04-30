#! /usr/bin/env python
import sys , os , math , random
from random import randint
import pygame
from pygame. locals import *

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