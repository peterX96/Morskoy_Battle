import pygame
from pygame.draw import *

pygame.init()

FPS = 100
screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Sea Battle")

ship_catalog = [1, 2, 3, 4 ]
button_pushed_image = ['images_buttons/exit_pushed_button.png','images_buttons/button_pushed_play.png','images_buttons/button_pushed_settings.png']
button_unpushed_image = [ 'images_buttons/exit_unpushed_button.png','images_buttons/button_unpushed_play.png','images_buttons/button_unpushed_settings.png' ]
button_coord = [[(902, 105),(100, -100)],[(432,522),(137,-143)],[(902,205),(100,-100)]]

background_image = ['images_static_battleground/menu_game.png','images_static_battleground/question_about_gamemode.png','images_static_battleground/selection_of_ships.png']
coordinates_of_buttons_on_a_slide = [(0,1,2),(0,1)]
post_pressing_effect = [[(1,0,0),(0,1,0),(0,8,0)]]

class Button:
    def _init(self,n):

        self.push_im = button_pushed_image[n]
        self.unpush_im = button_unpushed_image[n]
        self.coord_bottomleft = button_coord[n][0]
        self.size_button = button_coord[n][1]

    def pressure_test(self,event):
        return (int(event.pos[0] >= self.coord_bottomleft[0] and event.pos[0] <= self.coord_bottomleft[0] + self.size_button[0] and event.pos[1] <= self.coord_bottomleft[1] and event.pos[1] >= self.coord_bottomleft[1] + self.size_button[1]))

    def pushed_button_draw(self):
        _x = pygame.image.load(self.push_im)
        x_rect = _x.get_rect(bottomleft = self.coord_bottomleft)
        screen.blit(_x,x_rect)

    def unpushed_button_draw(self):
        _x = pygame.image.load(self.unpush_im)
        x_rect = _x.get_rect(bottomleft = self.coord_bottomleft)
        screen.blit(_x,x_rect)

def static_background(flag):

    _x = pygame.image.load(background_image[flag])
    x_rect = _x.get_rect(bottomleft = (0,900))
    screen.blit(_x,x_rect)

def dinamic_background(level_background,event):
    a , b, c  = 0 , level_background, 0
    for i in coordinates_of_buttons_on_a_slide[level_background]:
        b_n = Button()
        b_n._init(i)
        if event.type == pygame.MOUSEMOTION:
            if (b_n.pressure_test(event)):
                b_n.pushed_button_draw()
            else:
                b_n.unpushed_button_draw()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (b_n.pressure_test(event)):
                a,b,c = post_pressing_effect[level_background][i]
                
    return a,b,c

class Servise_Functions:

    def text(self,x, y, A, color, size):
        pygame.font.init()
        myfont = pygame.font.SysFont(' ', size)
        textsurface = myfont.render(A, False, color)
        screen.blit(textsurface, (x, y))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

flag_language = 0
level_background = 0
flag_quit = 0

ship_catalog = [1,2,3,4]

static_background(level_background)

s_f = Servise_Functions()
b_n = Button()

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or flag_quit == 1:
            finished = True
        elif (level_background == 0):
            flag_quit,level_background, gamemode = dinamic_background(level_background,event)
            if (level_background != 0): static_background(level_background)
        
        
        
    pygame.display.update()
    print(level_background)
pygame.quit()