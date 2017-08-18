import pygame
from pygame import *
from Images import *

class Block(sprite.Sprite):
    def __init__(self,x,y):
        images = Images()
        sprite.Sprite.__init__(self)
        self.xpos = x
        self.ypos = y
        self.image = images.block1
        self.rect = self.image.get_rect()
        self.rect.left = self.xpos
        self.rect.top = self.ypos




    def draw(self,screen):
        screen.blit(self.image, self.rect)


