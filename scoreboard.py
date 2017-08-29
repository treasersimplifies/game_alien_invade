
import pygame.font

class Scoreboard():

    def __init__(self, my_settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.my_settings = my_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ship_left()

    def  prep_score(self):
        score_str = "score:"+str('%.1f'%self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.my_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highest_score(self):

        highest_score_str = "highest:"+str('%.1f'%self.stats.highest_score)

        self.highest_score_image = self.font.render(highest_score_str, True, (128,128,0),
                                                    self.my_settings.bg_color)
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render('level:'+str(self.stats.level),True, (255,0,0), self.my_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship_left(self):
        self.ship_image = self.font.render('ships left:' + str(self.stats.ships_left), True, self.text_color,
                                            self.my_settings.bg_color)
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.left = 10
        self.ship_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ship_image, self.ship_rect)