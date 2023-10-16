import pygame as pg
import classes as cl


pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("lol dodge game")
icon = pg.image.load("assets/game_icon.png")
pg.display.set_icon(icon)
clock = pg.time.Clock()
delta_time = 0

running = True

while running:
    player = cl.PLayer()
    player_x = 0
    player_y = 0
    player.set_position(player_x, player_y)
    mouse_x = 0
    mouse_y = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    mouse = pg.mouse.get_pressed()

    pg.display.flip()
    delta_time = clock.tick(60) / 1000

pg.quit()
