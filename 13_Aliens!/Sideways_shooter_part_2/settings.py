
class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 73, 123)
        
        #Ship settings
        self.ship_speed = 0.6
        
        #Bullet settings
        self.bullet_speed = 0.2                    
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 60)
        self.bullets_allowed = 20
        
        #Alien settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 3.0
        # fleet_direction os 1 represent right; -1 represents left.
        self.fleet_direction = 1