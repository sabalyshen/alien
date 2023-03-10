import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        #創建一顆子彈
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(ai_settings, screen, ship, bullets):
    """響應案件和鼠標事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()         
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)         
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的圖像，並切換到新屏幕"""
    #每次循環時都重繪螢幕
    screen.fill(ai_settings.bg_color)
    #在飛船及外星人後面崇祟所有子彈
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    #讓最近繪製的屏幕可見
    pygame.display.flip()
    
    
def update_bullets(bullets):
    """更新子彈位子，刪除已消失子彈"""
    #更新子彈位子
    bullets.update()
    #刪除消失的子彈
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
            
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果還沒超過限制就發射子彈"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """計算每行可容納幾個外星人"""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    """創建外星人並放在當前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    """創建一群外星人"""
    #創建一個外星人並計算可以容納多少外星人
    #外星人間距為外星人寬度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    
    #創建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)