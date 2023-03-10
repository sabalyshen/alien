class Settings():
    """儲存所有設置的class"""
    
    
    def __init__(self):
        """初始化所有設置"""
        #屏幕設置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        
        #子彈設置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3