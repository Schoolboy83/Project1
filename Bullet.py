from pygame import *
from Settings import *
from Images import *


class YourBullet(sprite.Sprite):
    def __init__(self, player, direction, bonusesgot):
        images = Images()
        settings = GameSettings()
        sprite.Sprite.__init__(self)
        self.speed = settings.playerBulletSpeed
        self.image = images.playerBullet
        self.rect = self.image.get_rect()
        self.rect.centery = player.rect.centery
        self.range = settings.playerBulletRange*(bonusesgot+1)
        if bonusesgot == 2:
            self.damage = 9999999999
        else:
            self.damage = settings.playerBulletDamage*(bonusesgot+1)
        if direction:
            self.rect.left = player.rect.right
        else:
            self.rect.right = player.rect.left
            self.speed = -self.speed

    def update(self):
        self.rect.x += self.speed
        self.range -= abs(self.speed)

    def draw(self, screen,camera):
        screen.blit(self.image, (self.rect.x - camera.x, self.rect.y))
