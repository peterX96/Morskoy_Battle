from init_screen import *

BLACK = (0,0,0)
def battleground( x, y, n):

    for i in range(0, n + n//10, n//10):

        line(screen, BLACK, (x+i, y), (x+i, y+n), 5)
        line(screen, BLACK, (x, y+i), (x+n, y+i), 5)

def rot_center(image, angle, x, y):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
    center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

def text( x, y, A, color, size):
    pygame.font.init()
    myfont = pygame.font.SysFont(' ', size)
    textsurface = myfont.render(A, False, color)
    screen.blit(textsurface, (x, y))

def full_sum_ships( ship_catalog):
    S = 0
    for i in range(len(ship_catalog)):
        S += ship_catalog[i]
    return S