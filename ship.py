import pygame 

class Ship():
       
    def __init__(self, ai_settings, screen):
        """初始化並設定ship初始位子"""
        self.screen = screen
        self.ai_settings = ai_settings  
        #加載飛船圖像
        self.image = pygame.image.load('/Users/chenwenyu/Desktop/python/alien/images/ship.bmp')
        #飛船位子的實參
        self.rect = self.image.get_rect()
        #讀取螢幕的大小
        self.screen_rect = screen.get_rect()
        
        
        #將飛船放在中間
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #在飛船的屬性center加入小數點
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #預設飛船是靜止
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        
    def update(self):
        """根據移動標誌調整飛船的位子"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
             
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
            
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        
             
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery   
            
    def blitme(self):
        """在指定位子繪製飛船"""
        self.screen.blit(self.image, self.rect)