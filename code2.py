#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: July 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create bullets list (example with 5 bullets)
    bullets = []
    for i in range(5):
        bullet = stage.Sprite(image_bank_sprites, 6, -10, -10)  # start off-screen
        bullets.append(bullet)

    # create enemies list (example with 3 enemies)
    enemies = []
    for i in range(3):
        enemy = stage.Sprite(image_bank_sprites, 1, 20 + i * 30, 20)  # spread out
        enemies.append(enemy)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites; items show up in order
    # note: ship should be above the background, bullets above enemies
    game.layers = [ship] + bullets + enemies + [background]

    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
        
        # example: shoot bullet if A button pressed
        if keys & ugame.K_X:
            for bullet in bullets:
                if bullet.y < 0:  # bullet is off-screen
                    bullet.move(ship.x, ship.y - 10)
                    break

        # update game logic
        for bullet in bullets:
            if bullet.y >= 0:
                bullet.move(bullet.x, bullet.y - 2)  # move bullet up
                if bullet.y < 0:
                    bullet.move(-10, -10)  # hide off-screen

        # simple collision detection
        for enemy in enemies:
            for bullet in bullets:
                if bullet.x >= enemy.x and bullet.x <= enemy.x + 15 and \
                   bullet.y >= enemy.y and bullet.y <= enemy.y + 15:
                    print("Enemy hit!")
                    enemy.move(-20, -20)  # hide enemy off-screen
                    bullet.move(-10, -10)  # hide bullet off-screen

        # redraw sprite
        game.render_sprites([ship] + bullets + enemies)
        game.tick()  # wait until the next frame


if __name__ == "__main__":
    game_scene()
