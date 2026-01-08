#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: July 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage
import constants


def game_scene():
    # this function is the main game_scene

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(
        image_bank_sprites,
        5,
        75,
        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    bullets = []
    for i in range(5):
        bullet = stage.Sprite(image_bank_sprites, 6, -10, -10)
        bullets.append(bullet)

    enemies = []
    for i in range(3):
        enemy = stage.Sprite(image_bank_sprites, 1, 20 + i * 30, 20)
        enemies.append(enemy)

    game = stage.Stage(ugame.display, 60)

    # background first, sprites on top
    game.layers = [background] + enemies + bullets + [ship]

    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)

        if keys & ugame.K_X:
            for bullet in bullets:
                if bullet.y < 0:
                    bullet.move(ship.x, ship.y - constants.SPRITE_SIZE)
                    break

        for bullet in bullets:
            if bullet.y >= 0:
                bullet.move(bullet.x, bullet.y - 2)
                if bullet.y < 0:
                    bullet.move(-10, -10)

        for enemy in enemies:
            for bullet in bullets:
                if (
                    bullet.x >= enemy.x
                    and bullet.x <= enemy.x + constants.SPRITE_SIZE
                    and bullet.y >= enemy.y
                    and bullet.y <= enemy.y + constants.SPRITE_SIZE
                ):
                    enemy.move(-20, -20)
                    bullet.move(-10, -10)

        game.render_sprites([ship] + bullets + enemies)
        game.tick()


if __name__ == "__main__":
    game_scene()
