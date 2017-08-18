import pygame
from pygame import *
from Images import *
from GameFN import *
from Settings import *

class Character(sprite.Sprite):

    def __init__(self,screen):

        settings = GameSettings()
        images = Images()
        sprite.Sprite.__init__(self)
        self.lastshot = time.get_ticks()
        self.movespeed = settings.movespeeed
        self.jumpspeed = settings.jumpspeed
        self.gravity = settings.gravity
        self.font = pygame.font.SysFont('arial', 30)
        self.HP = settings.playerHP
        self.healthcount = self.font.render(str(self.HP), 1, Color('#FFFFFF'))
        self.Yspeed = 0
        self.Xspeed = 0
        self.image = images.playerright1
        #self.image.set_colorkey((255, 255, 255), 0)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screenrect = self.screen.get_rect()
        self.rect.top = self.screenrect.top
        self.moveright = False
        self.moveleft = False
        self.jump = False
        self.onGround = True
        self.shotCD = settings.shotCD

    def collisionX(self, group):
        for Sprite in group:
            if sprite.collide_rect(self, Sprite):



                if self.Xspeed > 0:
                    self.rect.right = Sprite.rect.left

                if self.Xspeed < 0:
                    self.rect.left = Sprite.rect.right

    def collisionY(self, group):
        for Sprite in group:
            if sprite.collide_rect(self, Sprite):
                if self.Yspeed > 0:
                    self.rect.bottom = Sprite.rect.top

                    self.onGround = True


                if self.Yspeed < 0:
                    self.rect.top = Sprite.rect.bottom
                    self.Yspeed = 0


    def update(self,group):

        if self.onGround:
            self.Yspeed = 0

        if self.moveright:
            self.Xspeed = self.movespeed

        if self.moveleft:
            self.Xspeed = -self.movespeed

        if self.moveleft == self.moveright:
            self.Xspeed = 0

        if self.jump and self.onGround:
            self.Yspeed = -self.jumpspeed

        if not self.onGround:
            self.Yspeed += self.gravity

        self.onGround = False
        self.rect.y += self.Yspeed
        self.collisionY(group)
        self.rect.x += self.Xspeed
        self.collisionX(group)

        if self.rect.bottom >= self.screenrect.bottom:
            self.rect.bottom = self.screenrect.bottom
            self.onGround = True
        if self.rect.left <= self.screenrect.left:
            self.rect.left = self.screenrect.left

    def CanShoot(self):
        self.shot = time.get_ticks()
        if self.shot - self.lastshot >= self.shotCD:
            self.lastshot = self.shot
            return True

    def DamageTaken(self, hit):
        if sprite.collide_rect(self, hit):
            self.HP -= hit.damage
            self.healthcount = self.font.render(str(self.HP), 1, Color('#FFFFFF'))
            return True

    def draw(self):
        self.screen.blit(self.image, (self.rect))
        self.screen.blit(self.healthcount, (10, 10))
        pass
