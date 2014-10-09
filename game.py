import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
import random


#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 8
GAME_HEIGHT = 8

#### Put class definitions here ####
class Gem(GameElement):
    SOLID = False

    def interact(self, zelda):
        zelda.inventory.append(self)
        GAME_BOARD.draw_msg("You rich bitch! You so fancy. You have %d status symbols" % len(zelda.inventory))

    def __init__(self, position, gem_color="BlueGem"):
        self.IMAGE = gem_color
        GAME_BOARD.register(self)
        self.position = position
        x_coord, y_coord = position
        GAME_BOARD.set_el(x_coord,y_coord,self)

class OrangeGem(Gem):
    IMAGE = "OrangeGem"
    SOLID = True

    def interact(self, zelda):
        for piece in starting_board_pieces:
            reset_piece_to_start(piece)
        random_rock_not_solid()
        zelda.inventory = []
        GAME_BOARD.draw_msg("Whoever said orange is the new pink" +
            " was seriously disturbed! Back to start with no status symbols.")

    def __init__(self, position):
        return super(OrangeGem, self).__init__(position, self.IMAGE)

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True  

    def interact(self, zelda):
        self.board.draw_msg("You got rock blocked")    

    def __init__(self, position):
        self.position = position
        x_coord, y_coord = position
        GAME_BOARD.register(self)
        GAME_BOARD.set_el(x_coord, y_coord, self)


class Character(GameElement):
    IMAGE = "Princess"
    position = (2,2)
    inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

    def update_pos(self, next_x, next_y):
        self.board.del_el(self.x, self.y)
        self.board.set_el(next_x, next_y, self)

    def keyboard_handler(self, symbol, modifier):
        direction = None
        direction_message = "I'm a Princess!"

        if symbol == key.UP:
            direction_message = "Upsee dwaynzee"
            direction = "up"
        elif symbol == key.DOWN:
            direction_message = "we goin down we yellin timberrrr"
            direction = "down"
        elif symbol == key.LEFT:
            direction_message = "to the left to the left"
            direction = "left"
        elif symbol == key.RIGHT:
            direction_message = "you spin me right round baby rigghhhht round"
            direction = "right"
        elif symbol == key.SPACE:
            self.board.erase_msg()

        self.board.draw_msg('%s says: "%s"' % (self.IMAGE, direction_message))

        if direction:
            next_location = self.next_pos(direction)

            if next_location:
                next_x, next_y = next_location
                try:
                    existing_el = self.board.get_el(next_x, next_y)
                    if existing_el:
                        existing_el.interact(self) 

                    if existing_el is None or not existing_el.SOLID:
                        self.update_pos(next_x, next_y)
                except IndexError:
                    self.board.draw_msg("Where do you think you're going fool?")


    def __init__(self):
        GameElement.__init__(self)

####   End class definitions    ####

def reset_piece_to_start(self):
    self.board.del_el(self.x, self.y)
    x_coord, y_coord = self.position
    GAME_BOARD.set_el(x_coord, y_coord, self)

def random_rock_not_solid():
    for dwayne in dwayne_johnsons:
        dwayne.SOLID = True
    random.choice(dwayne_johnsons).SOLID = False

def initialize():
    """Put game initialization code here"""
    global starting_board_pieces
    starting_board_pieces = []

    global current_board_pieces
    current_board_pieces = {}

        current_board_pieces[self.position] = self


    dwayne_johnson_positions = [
        (2,1),
        (1,2),
        (3,2),
        (2,3)
        ]
    
    global dwayne_johnsons
    dwayne_johnsons = []

    for pos in dwayne_johnson_positions:
        dwayne = Rock(pos)
        dwayne_johnsons.append(dwayne)
        starting_board_pieces.append(dwayne)

    random_rock_not_solid()

    zelda = Character()
    GAME_BOARD.register(zelda)
    GAME_BOARD.set_el(2,2, zelda)
    starting_board_pieces.append(zelda)

    blue_gem = Gem((3,1))
    green_gem = Gem((4,4), "GreenGem")
    orange_gem = OrangeGem((0,0))
    starting_board_pieces.extend([blue_gem, green_gem, orange_gem])