import pygame
from pygame.draw import *

pygame.init()

FPS = 100
screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Sea Battle")

BLACK = (0, 0, 0)

button_pushed_image = [('images_buttons/exit_pushed_button.png', 'images_buttons/button_pushed_play.png',
                        'images_buttons/button_pushed_settings.png'), ('images_buttons/AI_gamemode_pushed.png', 'images_buttons/pushed_pass_next.png'), ('images_buttons/Tirpitz_pushed_button.png', 'images_buttons/essex_pushed_button.png', 'images_buttons/kirov_pushed_button.png', 'images_buttons/destroyer_pushed_button.png', 'images_buttons/exit_pushed_button.png'),
                       ('images_buttons/return_in_game_pushed_button.png', 'images_buttons/return_in_the_menu_pushed_button.png', 'images_buttons/return_in_quit_pushed_button.png')]
button_unpushed_image = [('images_buttons/exit_unpushed_button.png', 'images_buttons/button_unpushed_play.png',
                          'images_buttons/button_unpushed_settings.png'), ('images_buttons/Al_gamemode_unpushed.png', 'images_buttons/unpushed_pass_next.png'), ('images_buttons/Tirpitz.png', 'images_buttons/essex.png', 'images_buttons/kirov.png', 'images_buttons/cringe_destroyer.png', 'images_buttons/exit_unpushed_button.png'),
                         ('images_buttons/return_in_game_unpushed_button.png', 'images_buttons/return_in_the_menu_unpushed_button.png', 'images_buttons/return_in_quit_unpushed_button.png')]
button_coord = [[[(902, 105), (100, -100)], [(432, 522), (137, -143)], [(902, 205), (100, -100)]], [[(321, 438), (362, -98)],
                                                                                                    [(321, 558), (362, -100)]], [[(720, 224), (200, -50)], [(720, 322), (150, -50)], [(720, 421), (100, -50)], [(721, 520), (50, -50)], [(900, 105), (100, -100)]],
                [[(229, 477), (543, -63)], [(229, 544), (544, -62)], [(229, 610), (544, -62)]]]

background_image = ['images_static_battleground/menu_game.png',
                    'images_static_battleground/question_about_gamemode.png',
                    'images_static_battleground/selection_of_ships.png',
                    'images_static_battleground/question_quit.png']
post_pressing_effect = [[(1, 0, 0), (0, 1, 0), (0, 8, 0)], [
    (0, 2, 0), (0, 5, 0)], [(0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 3, 0)], [(0, 2, 0), (0, 0, 0), (1, 0, 0)]]

Map = [(100,100),(500,500)]
class Button:
    def _init(self, n):

        self.push_im = button_pushed_image[level_background][n]
        self.unpush_im = button_unpushed_image[level_background][n]

        self.coord_bottomleft = button_coord[level_background][n][0]
        self.size_button = button_coord[level_background][n][1]

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

class Motion_Buttons:

    def _init(self,event,n):
        self.image = pygame.image.load(button_unpushed_image[level_background][n])
        self.image,self.image_rect = rot_center(self.image, 0, event.pos[0],event.pos[1])
        self.size = button_coord[level_background][n][1]
        self.angle = 0

    def examination_of_button(self,event):
        if (self.angle % 90 == 0):
            a ,b= self.size[0] / 2, self.size[1] / 2
        else:
            b ,a= self.size[0] / 2, self.size[1] / 2
        delta = abs(self.size[1])
        x = event.pos[0] - Map[0][0] - a 
        y = event.pos[1] - Map[0][1] - b
        if (x >= 0 and x + 2*a <= Map[1][0] and y >= 0 and y + 2*b <= Map[1][1]):
            p = int(x//delta)+1
            h = int(y//delta)+1
            print(x,y)
            if (self.angle % 90 == 0):
                print(p,h,self.size[0]//delta)
                battlefield[h][p] = self.size[0]//delta
        for row in battlefield:
            print(' '.join([str(elem) for elem in row]))
    def rotation(self,event):

        self.image, self.image_rect = rot_center(self.image,90, event.pos[0],event.pos[1])
        self.angle += 90
        screen.blit(self.image, self.image_rect)

    def _draw(self,event):
        self.image_rect = self.image.get_rect(center = (event.pos[0],event.pos[1]))
        screen.blit(self.image, self.image_rect)

def static_background(flag):

    _x = pygame.image.load(background_image[flag])
    x_rect = _x.get_rect(bottomleft=(0, 900))
    screen.blit(_x, x_rect)
    if level_background == 2 :
        for i in range(0,400,100):
            text(950,170 + i, str(ship_catalog[i//100]),BLACK,64)
        battleground(Map[0][0],Map[0][1],Map[1][1])



def dinamic_background(level_background, event):
    a, b, c = 0, level_background, 0
    for i in range(len(button_pushed_image[level_background])):
        b_n = Button()
        b_n._init(i)
        if event.type == pygame.MOUSEMOTION:
            if (b_n.pressure_test(event)):
                b_n.pushed_button_draw()
            else:
                b_n.unpushed_button_draw()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (b_n.pressure_test(event)):
                a, b, c = post_pressing_effect[level_background][i]

    return a, b, c

def dinamic_background_for_motion_buttons(ship, event):
    motion_button = ship + 1
    if event.type == pygame.MOUSEMOTION:
        m_b_n._draw(event)
    elif (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 3):
            m_b_n.rotation(event)
        elif (event.button == 2):
            ship_catalog[ship] += 1
            motion_button = 0
        elif (event.button == 1):
            m_b_n.examination_of_button(event)
        m_b_n._draw(event)

    return motion_button

def battleground(x,y,n):

    for i in range(0,n + n//10,n//10):

        line(screen,BLACK,(x+i,y),(x+i,y+n),5)
        line(screen,BLACK,(x,y+i),(x+n,y+i),5)
def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect
def text(x, y, A, color, size):
    pygame.font.init()
    myfont = pygame.font.SysFont(' ', size)
    textsurface = myfont.render(A, False, color)
    screen.blit(textsurface, (x, y))
pygame.display.update()
clock = pygame.time.Clock()
finished = False


level_background = 0
flag_quit = 0
gamemode = 0
motion_button = 0
ship_catalog = [1, 2, 3, 4]
battlefield = [[0] * 12] * 12

static_background(level_background)

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or flag_quit == 1:
            finished = True
        elif (level_background == 0):

            flag_quit, level_background, motion_button = dinamic_background(
                level_background, event)
            if (level_background != 0):
                static_background(level_background)

        elif (level_background == 1):

            flag_quit, level_background, motion_button = dinamic_background(
                level_background, event)
            if (level_background != 1):
                static_background(level_background)

        elif (level_background == 2):  # SET YOUR SHIPS
            static_background(level_background)

            if (motion_button == 0):
                flag_quit, level_background, motion_button = dinamic_background(
                    level_background, event)
                fl = 1
            if (motion_button !=0 ):
                if (fl == 1):
                    m_b_n = Motion_Buttons()
                    m_b_n._init(event,motion_button- 1)
                    ship_catalog[motion_button-1] -= 1
                    fl = 0
                motion_button = dinamic_background_for_motion_buttons(motion_button - 1,event)

        elif (level_background == 3):
            static_background(level_background)
            flag_quit, level_background, gamemode = dinamic_background(
                level_background, event)
            if (level_background != 3):
                static_background(level_background)

    pygame.display.update()
pygame.quit()

