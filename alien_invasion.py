import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #初始化遊戲並創建一個屏幕對象
    pygame.init()
    ai_settings = Settings()
    screen  = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #創建飛船
    ship = Ship(ai_settings, screen)
    #創建存放子彈的地方
    bullets = Group()
    #創建一個放外星人的地方
    aliens = Group()
    #創建一個外星人
    alien = Alien(ai_settings, screen)
    #創建一個外星人群
    gf.create_fleet(ai_settings, screen, aliens)
    
    #開始遊戲的主循環
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()    