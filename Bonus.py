from pygame import *
from Images import *

class Bonus(sprite.Sprite):
    def __init__(self, image, x, y,bonusesgot):
        sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y+32
        self.bonusesgot = bonusesgot

    def collision(self, player):
        if sprite.collide_rect(self, player):
            self.rect.left = 100*(self.bonusesgot)
            self.rect.top = 10
            return True

    def draw(self, screen, camera):
        screen.blit(self.image, (self.rect.x - camera.x, self.rect.y))
