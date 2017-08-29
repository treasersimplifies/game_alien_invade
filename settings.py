

class Settings():

    def __init__(self):
        self.screen_width =1299
        self.screen_height = 800

        self.bg_color=(88,88,88)


        self.ship_limit = 5



        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = [230, 230, 230]


        self.speeded_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 10

        self.bullets_allowed = 5
        self.alien_points = 1
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 20

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speeded_scale
        self.bullet_speed_factor *= self.speeded_scale
        self.alien_speed_factor *= self.speeded_scale
        self.fleet_drop_speed *= self.speeded_scale
        self.alien_points *= self.speeded_scale
        self.bullets_allowed  *= self.speeded_scale