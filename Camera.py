from pygame import *

class Camera():
    def __init__(self,player):
        self.player = player
        self.x = 0
    def update(self):
        if self.player.rect.centerx >= 480:
            if self.player.rect.centerx <= 960*3-480:
                self.x = self.player.rect.centerx - 480

        else:
            self.x = 0