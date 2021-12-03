button_pushed_image = []
button_unpushed_image = []
button_coord = []
post_pressing_effect = []
Gamemode = []

attack_image = ['images_of_battlefield/hit_on_sea.png','images_of_battlefield/hit_on_ship.png']

ships_images = ['images_buttons/Tirpitz.png', 'images_buttons/essex.png',
                'images_buttons/kirov.png', 'images_buttons/cringe_destroyer.png']

Battleship = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (2, 1),
              (3, 1), (4, 1), (4, 0), (4, -1), (3, -1), (2, -1), (1, -1), (0, -1)]
Carrier = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (2, 1),
           (3, 1), (3, 0), (3, -1), (2, -1), (1, -1), (0, -1)]
Cruiser = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1),
           (2, 1), (2, 0), (2, -1), (1, -1), (0, -1)]
Destroyer = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
             (1, 1), (1, 0), (1, -1), (0, -1)]
Ships = [Battleship, Carrier, Cruiser, Destroyer]