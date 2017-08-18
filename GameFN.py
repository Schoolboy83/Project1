import pygame
from pygame import *
from Bullet import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"
last=pygame.time.get_ticks()

def events(player,bullets):
    inmenu = False

    for event in pygame.event.get():

        if event.type == QUIT:
            raise SystemExit
        if event.type == KEYDOWN:

            if event.key == K_RIGHT:
                if player.CanShoot():
                    bullets.add(YourBullet(player, True))
            if event.key == K_LEFT:
                if player.CanShoot():
                    bullets.add(YourBullet(player, False))
            if event.key == K_ESCAPE:
                if not inmenu:
                    player.moveright = False
                    player.moveleft = False
                    player.jump = False
                    menu()
                    inmenu = True
            if event.key == K_d and event.key == K_a:
                player.moveright = False
                player.moveleft = False
            elif event.key == K_d:
                player.moveright = True
            elif event.key == K_a:
                player.moveleft = True
            if event.key == K_w:
                player.jump = True

        if event.type == KEYUP:
            if event.key == K_w:
                player.jump = False
            if event.key == K_d:
                player.moveright = False
            if event.key == K_a:
                player.moveleft = False

def menu():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Menu")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color("#FFFFFF"))
    myfont = pygame.font.SysFont("arial", 50, False, False)
    label = myfont.render("Paused Press ESC to continue...", 1, (0, 0, 0))
    while True:

        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return

            if e.type == QUIT:
                raise SystemExit

        screen.blit(bg, (0, 0))
        screen.blit(label, (100, 300))
        pygame.display.update()



def draw(screen,player,group,bullets,enemies, hits):
    player.draw()
    bullets.draw(screen)
    group.draw(screen)
    enemies.draw(screen)
    hits.draw(screen)
