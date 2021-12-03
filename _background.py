from init_screen import *
from _buttons_ import *

background_image = []

with open("background.json") as buttons_json_file:
    buttons_list = json.load(buttons_json_file)
for i in range(len(buttons_list)):
    background_image.append(buttons_list[i]["image"])

def static_background(flag):

    _x = pygame.image.load(background_image[flag])
    x_rect = _x.get_rect(bottomleft=(0, 900))
    screen.blit(_x, x_rect)