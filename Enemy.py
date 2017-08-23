from pygame import *
from Settings import *
from Images import *

class Enemy1(sprite.Sprite):
    def __init__(self,x,y,screen):
        images = Images()
        settings = GameSettings()
        pygame.sprite.Sprite.__init__(self)
        self.gravity = settings.enemy1gravity
        self.screenrect = screen.get_rect()
        self.image = images.enemy1right1
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.bottom = y + 32
        self.aggroRange = settings.enemy1aggroRange
        self.moveSpeed = settings.enemy1moveSpeed
        self.Xspeed = 0
        self.Yspeed = 0
        self.onGround = False
        self.lasthit = time.get_ticks()
        self.hitCD = settings.enemy1hitCD
        self.direction = None
        self.HP = settings.enemy1HP

    def update(self, group, player):
        if self.onGround:
            self.Yspeed = 0
        self.aggro(player)
        if not self.onGround:
            self.Yspeed +=self.gravity


        self.onGround = False
        self.rect.x += self.Xspeed
        self.collisionX(group)
        self.rect.y += self.Yspeed
        self.collisionY(group)
        if self.rect.bottom >= self.screenrect.bottom:
            self.rect.bottom = self.screenrect.bottom
            self.onGround = True
        if self.rect.left <= self.screenrect.left:
            self.rect.left = self.screenrect.left



    def aggro(self, player):
        if abs(player.rect.centerx - self.rect.centerx) <= self.aggroRange and abs(player.rect.centerx - self.rect.centerx) >= 200:
            if (self.rect.bottom >= player.rect.top) and (self.rect.top <= player.rect.bottom):
                if player.rect.x > self.rect.x:
                    self.Xspeed = self.moveSpeed

                if player.rect.x < self.rect.x:
                    self.Xspeed = -self.moveSpeed


        elif abs(player.rect.centerx - self.rect.centerx) < 200:
            if (self.rect.bottom >= player.rect.centery) and (self.rect.top <= player.rect.centery):
                if player.rect.x > self.rect.x:
                    self.Xspeed = self.moveSpeed
                    self.direction = True
                    self.Xspeed = 0
                if player.rect.x < self.rect.x:
                    self.Xspeed = -self.moveSpeed
                    self.direction = False
                    self.Xspeed = 0
            else:
                self.Xspeed = 0
                self.direction = None


    def GetShot(self, bullets):
        for bullet in bullets:
            if sprite.collide_rect(self, bullet):
                self.HP -= bullet.damage
                bullets.remove(bullet)

    def CanHit(self):
        self.hit = time.get_ticks()
        if self.hit - self.lasthit >= self.hitCD:
            self.lasthit = self.hit
            return True


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

    def draw(self, screen, camera):
        screen.blit(self.image, (self.rect.x - camera.x, self.rect.y))