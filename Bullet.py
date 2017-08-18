from pygame import *
from Settings import *
from Images import *


class YourBullet(sprite.Sprite):
    def __init__(self, player, direction):
        images = Images()
        settings = GameSettings()
        sprite.Sprite.__init__(self)
        self.speed = settings.playerBulletSpeed
        self.image = images.playerBullet
        self.rect = self.image.get_rect()
        self.rect.centery = player.rect.centery
        self.range = settings.playerBulletRange
        self.damage = settings.playerBulletDamage
        if direction:
            self.rect.left = player.rect.right
        else:
            self.rect.right = player.rect.left
            self.speed = -self.speed

    def update(self):
        self.rect.x += self.speed
        self.range -= abs(self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)