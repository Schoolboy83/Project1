#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame import *
from Player import *
from Blocks import *
from Levels import *
from Enemy import *
from Enemy1attack import *
import GameFN as functions


WIN_WIDTH = 960
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"


def main():
    pygame.init()
    x=0
    y=0
    screen = pygame.display.set_mode(DISPLAY)
    player = Character(screen)
    pygame.display.set_caption("Game")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bullets = pygame.sprite.Group()
    bg.fill(Color(BACKGROUND_COLOR))
    blocks = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    hits = pygame.sprite.Group()
    level = Level_1
    for i in level:
        for j in i:
            if j=='-':
                blocks.add(Block(x, y))
            if j=='*':
                enemies.add(Enemy1(x, y, screen))
            x += 32
        x=0
        y+=32


    while True:
        if player.HP <= 0:
            time.delay(500)
            main()
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








        functions.events(player, bullets)
        screen.blit(bg, (0, 0))
        functions.draw(screen, player, blocks, bullets,enemies,hits)
        pygame.display.update()


if __name__ == "__main__":
    main()
