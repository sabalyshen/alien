import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示外星人的類"""
    
    def __init__(self, ai_settings, screen):
        """初始化外星人並設置其位子"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #載入外星人圖像
        self.image = pygame.image.load('/Users/chenwenyu/Desktop/python/alien/images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #每個外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #儲存外星人準確位子
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)