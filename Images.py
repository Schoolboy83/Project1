import pygame
from pygame import *
class Images():
    def __init__(self):
        self.playerright1 = pygame.image.load('Images/char1.jpg')
        self.block1 = pygame.image.load('Images/block1.jpg')
        self.playerBullet = pygame.image.load('Images/playerBullet.jpg')
        self.enemy1right1 = pygame.image.load('Images/enemy1-1.jpg')
        self.enemy1hitleft = pygame.image.load('Images/enemy1hitleft.jpg')
        self.enemy1hitright =pygame.image.load('Images/enemy1hitright.jpg')
        self.bonus1 = pygame.image.load('Images/bonus1.jpg')
        self.bonus2 = pygame.image.load('Images/bonus2.jpg')
