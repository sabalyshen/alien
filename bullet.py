import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飛船發射子彈的類"""
    
    def __init__(self, ai_settings, screen, ship):
        #繼承父類
        super().__init__()
        self.screen = screen
        
        #在(0, 0)處創建一個代表子彈的舉行
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
        
    def update(self):
        """向上移動子彈"""
        #更新子彈的位子
        self.y -= self.speed_factor
        self.rect.y = self.y
        
        
    def draw_bullet(self):
        """在螢幕上繪製子彈"""
        pygame.draw.rect(self.screen, self.color, self.rect)