
class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 73, 123)
        
        #Ship settings
        self.ship_speed = 3
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed = 3                    
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 60)
        self.bullets_allowed = 1
        self.bullets_qty = 10
        self.bullets_left = 10
        
        #Target settings
        self.target_color = (255, 255, 100)
        self.target_width = 20
        self.target_height = 60
        self.target_speed = 0.2
        self.target_direction = 1
        
        self.asserts = 0
        self.increase = 4
        
    def initialize_settings(self):
        """ """
        self.target_speed = 0.2
        self.bullets_left = 10
        self.asserts = 0
        self.increase = 4        
        
        