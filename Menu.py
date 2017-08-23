#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame import *
from Player import *
from Blocks import *
from Levels import *
from Enemy import *
from Camera import *
from Images import *
from Bonus import *
from Enemy1attack import *
import GameFN as functions


WIN_WIDTH = 960
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

def deathscreen():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Game")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color("#FFFFFF"))

    myfont = pygame.font.SysFont("arial", 50, False, False)
    label = myfont.render("You are dead, press ENTER to restart", 1, (0, 0, 0))
    while True:

        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_RETURN:
                main()

            if e.type == QUIT:
                raise SystemExit

        screen.blit(bg, (0, 0))
        screen.blit(label, (100, 300))
        pygame.display.update()

def main():
    pygame.init()
    x=0
    y=0
    images = Images()
    screen = pygame.display.set_mode(DISPLAY)
    player = Character(screen)
    pygame.display.set_caption("Game")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bullets = pygame.sprite.Group()
    bg.fill(Color(BACKGROUND_COLOR))
    blocks = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    hits = pygame.sprite.Group()
    bonuses = pygame.sprite.Group()
    bonusesgot = 0
    camera = Camera(player)
    level = Level_1

    for i in level:
        for j in i:
            if j=='-':
                blocks.add(Block(x, y))
            if j=='*':
                enemies.add(Enemy1(x, y, screen))
            if j=='a':
                bonuses.add(Bonus(images.bonus1, x, y, bonusesgot))
            if j=='b':
                bonuses.add(Bonus(images.bonus2, x, y, bonusesgot))
            x += 32
        x=0
        y+=32


    while True:
        if player.HP <= 0:
            deathscreen()
        timer = pygame.time.Clock()
        timer.tick(60)
        player.update(blocks)
        bullets.update()
        for bullet in bullets:
            if bullet.range <= 0:
                bullets.remove(bullet)

        for enemy in enemies:
            enemy.update(blocks, player)
            enemy.GetShot(bullets)
            if (enemy.direction == True or enemy.direction == False) and enemy.CanHit():
                hits.add(Enemy1Hit(enemy))
            if enemy.HP <= 0:
                enemies.remove(enemy)
        for hit in hits:

            if player.DamageTaken(hit) or hit.update() or hit.hittime():
                hits.remove(hits)
        for bonus in bonuses:
            if bonus.collision(player):
                bonusesgot += 1

        camera.update()
        functions.events(player, bullets,camera, bonusesgot)
        screen.blit(bg, (0, 0))


        functions.draw(screen, player, blocks, bullets,enemies, hits, bonuses, camera)
        pygame.display.update()
        print(bonusesgot)


if __name__ == "__main__":
    main()
