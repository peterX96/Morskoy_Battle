import pygame
from pygame.draw import *
from _constans import *
from _buttons_ import *
from init_screen import *

class Button:
    def _init(self, n, screen_id):

        self.push_im = button_pushed_image[screen_id][n]
        self.unpush_im = button_unpushed_image[screen_id][n]

        self.coord_bottomleft = button_coord[screen_id][n][0]
        self.size_button = button_coord[screen_id][n][1]

    def pressure_test(self, event):
        return (int(event.pos[0] >= self.coord_bottomleft[0] and event.pos[0] <= self.coord_bottomleft[0] + self.size_button[0] and event.pos[1] <= self.coord_bottomleft[1] and event.pos[1] >= self.coord_bottomleft[1] + self.size_button[1]))

    def pushed_button_draw(self):
        _x = pygame.image.load(self.push_im)
        x_rect = _x.get_rect(bottomleft=self.coord_bottomleft)
        screen.blit(_x, x_rect)

    def unpushed_button_draw(self):
        _x = pygame.image.load(self.unpush_im)
        x_rect = _x.get_rect(bottomleft=self.coord_bottomleft)
        screen.blit(_x, x_rect)