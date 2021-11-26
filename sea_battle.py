import pygame
from pygame.draw import *
from random import choice

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

Battleship = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(2,1),(3,1),(4,1),(4,0),(4,-1),(3,-1),(2,-1),(1,-1),(0,-1)]
Carrier = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(2,1),(3,1),(3,0),(3,-1),(2,-1),(1,-1),(0,-1)]
Cruiser = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(2,1),(2,0),(2,-1),(1,-1),(0,-1)]
Destroyer = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

class Button:
    def _init(self, n):

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

class Ship_Buttons:

    def _init(self,event,n):
        self.image = pygame.image.load(button_unpushed_image[screen_id][n])
        self.image,self.image_rect = s_f.rot_center(self.image, 0, event.pos[0],event.pos[1])
        self.size = button_coord[screen_id][n][1]
        self.angle_flag = 0

    def examination_of_button(self,event):
        if (self.angle_flag == 0):
            a,b = self.size[0] / 2 , self.size[1] / 2
        else:
            print('*')
            b,a = self.size[0] / 2 , self.size[1] / 2
        x, y = event.pos[0] - 100 - a, event.pos[1] - 100 - b
        delta = abs(self.size[1])
        X,Y = int(x//delta), int(y//delta) 
        print(' ')
        if ( 0 <= x and x + 2 * a <= 600 and 0 <= y and y + 2 * a <= 650 ):
            battlefield[X+1][Y] = int(self.size[0]//50)
        for row in battlefield:
            print(' '.join([str(elem) for elem in row]))

    def rotation(self,event):

        self.image, self.image_rect = s_f.rot_center(self.image,90, event.pos[0],event.pos[1])
        if (self.angle_flag == 1): self.angle_flag = 0
        else: self.angle_flag = 1
        screen.blit(self.image, self.image_rect)

    def _draw(self,event):
        self.image_rect = self.image.get_rect(center = (event.pos[0],event.pos[1]))
        screen.blit(self.image, self.image_rect)

def static_background(flag):

    _x = pygame.image.load(background_image[flag])
    x_rect = _x.get_rect(bottomleft=(0, 900))
    screen.blit(_x, x_rect)
    if screen_id == 2 :
        for i in range(0,400,100):
            s_f.text(950,170 + i, str(ship_catalog[i//100]),BLACK,64)
        s_f.battleground(100,100,500)

def dinamic_background(level_background, event):
    a, b, c = 0, level_background, 0
    for i in range(len(button_pushed_image[level_background])):
        
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

class additional_background():

    def _init_battlefield(self):

        self.battlefield = [[[0] * 12 for i in range(12)],[[0] * 12 for i in range(12)]]

    def _init_ship(self, motion_button):
        self.ship = Ship_Buttons()
        self.ship._init(event,motion_button- 1)
        ship_catalog[motion_button-1] -= 1

    def operator_on_ships_button(self,_ship, event):

        motion_button = _ship + 1
        if event.type == pygame.MOUSEMOTION:
            self.ship._draw(event)

        elif (event.type == pygame.MOUSEBUTTONDOWN):

            if (event.button == 3):
                self.ship.rotation(event)

            elif (event.button == 2):
                ship_catalog[_ship] += 1
                motion_button = 0

            elif (event.button == 1):
                self.ship.examination_of_button(event)

            self.ship._draw(event)

        return motion_button
      
    def auto_set_ship(self,n):
        size_ship = [3,2,1,0]
        battlefield_ = [[0] * 12 for i in range(12)]
        for n in ship_catalog:
            for m in range(n):
                flag_angle = choice([0,1])
                A = []
                m,k = 11,11 - size_ship[n-1]
                
                if (flag_angle == 1): m,k = k,m

                for i in range(1,m):
                    for j in range(1,k):
                        if ((flag_angle ==0 and battlefield_[i][j] == 0 and battlefield_[i][j + size_ship[n-1]] == 0) or (flag_angle == 1 and battlefield_[i][j] == 0 and battlefield_[i + size_ship[n-1]][j] == 0)):
                                A.append((i,j))

                coord = choice(A)
                for i in range(0,size_ship[n-1] + 1):
                    if (flag_angle == 0):
                        battlefield_[coord[0]][coord[1] + i] = size_ship[n-1] + 2
                    else:
                        battlefield_[coord[0]+i][coord[1]] = size_ship[n-1] + 2

                if (n == 1) : B = Battleship
                elif (n == 2) : B = Carrier
                elif (n == 3) : B = Cruiser
                else: B = Destroyer

                for i in range(len(B)):
                    if (flag_angle == 0):
                        battlefield_[int(coord[0] + B[i][1])][int(coord[1] + B[i][0])] = 1
                    else:
                        battlefield_[int(coord[0] + B[i][0])][int(coord[1] + B[i][1])] = 1
                        
        self.battlefield[n] = battlefield_
        return [0,0,0,0]
      
class Servise_Function:
    def battleground(self,x,y,n):

        for i in range(0,n + n//10,n//10):

            line(screen,BLACK,(x+i,y),(x+i,y+n),5)
            line(screen,BLACK,(x,y+i),(x+n,y+i),5)

    def rot_center(self,image, angle, x, y):
        
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

        return rotated_image, new_rect

    def text(self,x, y, A, color, size):
        pygame.font.init()
        myfont = pygame.font.SysFont(' ', size)
        textsurface = myfont.render(A, False, color)
        screen.blit(textsurface, (x, y))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


screen_id = 0
flag_quit = 0
gamemode = 0
motion_button = 0
ship_catalog = [1, 2, 3, 4]

s_f = Servise_Function()
b_n = Button()
static_background(screen_id)

static_background(level_background)
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or flag_quit == 1:
            finished = True
        elif screen_id != 2:
            flag_quit, screen_id, motion_button = dinamic_background(screen_id, event)
            if screen_id != 0:
                static_background(screen_id)
        elif screen_id == 2:  # SET YOUR SHIPS
            static_background(screen_id)

            if (motion_button == 0):
                flag_quit, screen_id, motion_button = dinamic_background(
                    screen_id, event)
                add_bd = additional_background()
                fl = 1
            else:
                if (fl == 1):
                    add_bd._init_ship(motion_button)
                    fl = 0

                motion_button = add_bd.operator_on_ships_button(motion_button - 1,event)


    pygame.display.update()
pygame.quit()

