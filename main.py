import pygame
from settings import Settings

from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():

    #  初始化
    pygame.init()
    pygame.display.set_caption("alien invasion!")

    #  定义的数据结构
    screen = pygame.display.set_mode((1200,700))
    my_settings=Settings()
    bg_color = my_settings.bg_color
    ship = Ship(my_settings,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(my_settings)
    sb = Scoreboard(my_settings, screen, stats)
    play_button = Button(my_settings, screen, "pLAy")

    gf.creat_fleet(my_settings, screen, ship, aliens)

    #  游戏程序的主循环
    while True:

        gf.check_events(my_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(my_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(my_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(my_settings, screen, stats, sb, ship, bullets, aliens, play_button)



run_game()