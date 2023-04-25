
class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10,73, 123)
        
        #Ship settings
        self.ship_speed = 3

       #Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 224, 78)
        self.bullets_allowed = 10
        
