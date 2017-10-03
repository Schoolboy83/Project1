from pygame import *
from Images import *
from Settings import *


class Enemy1Hit(sprite.Sprite):
    def __init__(self, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.images = Images()
        self.settings = GameSettings()
        self.image = self.images.enemy1hitright
        self.rect = self.image.get_rect()
        self.hitstart = pygame.time.get_ticks()
        self.damage = self.settings.enemy1hitDmg
        self.enemy = enemy
        self.timeOfHit = self.settings.enemy1hittime
        self.id = 'Enemy1'

    def update(self):
        if self.enemy.direction == True:
            self.image = self.images.enemy1hitright
            self.rect.left = self.enemy.rect.right
        elif self.enemy.direction == False:
            self.image = self.images.enemy1hitleft
            self.rect.right = self.enemy.rect.left
        else:
            return True
        self.rect.centery = self.enemy.rect.centery


    def hittime(self):
        self.now = pygame.time.get_ticks()
        if self.now - self.hitstart >= self.timeOfHit:
            return True

    def draw(self, screen,camera):
        screen.blit(self.image, (self.rect.x - camera.x, self.rect.y))




class BossHit(sprite.Sprite):
    def __init__(self, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.images = Images()
        self.settings = GameSettings()
        self.image = self.images.BossHit
        self.rect = self.image.get_rect()
        self.rect.right = enemy.rect.right
        self.hitstart = pygame.time.get_ticks()
        self.damage = self.settings.BosshitDmg
        self.enemy = enemy
        self.speed = self.settings.BosshitSpeed
        self.rect.y = 0
        self.id = 'Boss'
        self.range = 0


    def update(self):
        self.rect.x -= self.speed
        self.range += self.speed

    def hittime(self):
        if self.range == 960:
            return True

    def draw(self, screen,camera):
        screen.blit(self.image, (self.rect.x - camera.x, self.rect.y))