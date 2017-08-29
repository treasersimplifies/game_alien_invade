

class GameStats():
    def __init__(self, my_settings):
        self.my_settings = my_settings
        self.reset_stats()
        self.game_active = False



    def reset_stats(self):
        with open('highest_score.txt') as highest_score_file:
            highest_score = highest_score_file.read()
            self.highest_score = float(highest_score)
        self.ships_left = self.my_settings.ship_limit
        self.score = 0
        self.level = 1