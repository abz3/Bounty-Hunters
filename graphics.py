import random
import math
import uuid
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 200, 255)
BROWN = (102, 51, 0)
PURPLE = (102, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 153, 0)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)


WINDOW_HEIGHT = 650
WINDOW_WIDTH = 650

TILE_SIZE = 3

# Constants
X_DIMENSION = 200
Y_DIMENSION = 200
TYPH_MIN = 3
TYPH_MAX = 4
NAVY_MIN = 20
NAVY_MAX = 30
ISLAND_MIN = 20
ISLAND_MAX = 30
TREASURE_QUANT = 1
PORT_MIN = 10
PORT_MAX = 20
WIND_DIRECTION = (1, 8)
WIND_SPEED = (0, 2)
LEADERSHIP_SCALE = (0, 10)
TURN_NUM = (3, 5)
obj_stats = {
    'typhoon': (7, -1),
    'navy': (1, -1),
    'island': (3, -1),
    'treasure': (1, +3),
    'port': (3, +1)
}


# Core mechanics
def crash(spot, locations):
    """
    Checks if you've crashed
    :param spot: tuple of pirate coordinates
    :param locations: dictionary; keys: type of obstacle, value: coordinate
    :return: True or False
    """
    for ID, info in locations.items():
        location = info[0]
        coord = info[1]
        if location == 'typhoon':
            if (coord[0] - (obj_stats['typhoon'][0] - 1) / 2) <= spot[0] <= \
                    (coord[0] + (obj_stats['typhoon'][0] - 1) / 2):
                if (coord[1] - (obj_stats['typhoon'][0] - 1) / 2) <= spot[1] <= \
                        (coord[0] + (obj_stats['typhoon'][0] - 1) / 2):
                    print('The Ship was swallowed up by a typhoon!')
                    return True
        if location == 'navy':
            if coord[0] == spot[0]:
                if coord[1] == spot[1]:
                    print('The Ship was apprehended by the navy!')
                    return True
        if location == 'island':
            if (coord[0] - (obj_stats['island'][0] - 1) / 2) <= spot[0] <= \
                    (coord[0] + (obj_stats['island'][0] - 1) / 2):
                if (coord[1] - (obj_stats['island'][0] - 1) / 2) <= spot[1] <= \
                        (coord[0] + (obj_stats['island'][0] - 1) / 2):
                    print('The Ship crashed into an island!')
                    return True
        if location == 'treasure':
            if coord[0] == spot[0]:
                if coord[1] == spot[1]:
                    print('The Ship found the treasure!')
                    return True
        if location == 'port':
            if (coord[0] - (obj_stats['port'][0] - 1) / 2) <= spot[0] <= \
                    (coord[0] + (obj_stats['port'][0] - 1) / 2):
                if (coord[1] - (obj_stats['port'][0] - 1) / 2) <= spot[1] <= \
                        (coord[0] + (obj_stats['port'][0] - 1) / 2):
                    print('The Ship docked at a port!')
                    return True
    return False


class Board:
    """
    the Board
    """

    def __init__(self, X_DIMENSION, Y_DIMENSION, qtyphoon, qnavy, qisland, qtreasure, qport, start_location):
        """
        Initializes
        :param X_DIMENSION: int
        :param Y_DIMENSION: int
        :param qtyphoon: int
        :param qnavy: int
        :param qisland: int
        :param qtreasure: int
        :param qport: int
        :param start_location: tuple of 2 ints
        """
        self._board = (X_DIMENSION, Y_DIMENSION)
        self._taken = [start_location]
        self._locations = {}
        self._typhoon = qtyphoon
        self._navy = qnavy
        self._island = qisland
        self._treasure = qtreasure
        self._port = qport
        self._last = start_location
        self._objects = {}

    def create(self):
        """
        Creates a board so that nothing is touching
        """
        print('Drawing up the map...')
        for typhoon in range(self._typhoon):
            while True:
                checks = []
                taken = False
                x_coord = random.randint(0, X_DIMENSION - 1)
                y_coord = random.randint(0, Y_DIMENSION - 1)
                checks.append((x_coord, y_coord))
                start = [x_coord - (obj_stats['typhoon'][0] - 1) / 2,
                         y_coord - (obj_stats['typhoon'][0] - 1) / 2]
                for i in range(obj_stats['typhoon'][0]):
                    start[1] += i
                    for j in range(obj_stats['typhoon'][0]):
                        start[0] += j
                        checks.append(tuple(start))
                for check in checks:
                    if check in self._taken:
                        taken = True
                        break
                if not taken:
                    for check in checks:
                        self._taken.append(check)
                        self._locations[uuid.uuid4()] = ['typhoon', (x_coord, y_coord)]
                    print('Typhoon detected at: ' + str((x_coord, y_coord)))
                    self._objects[uuid.uuid4()] = ['typhoon', (x_coord,y_coord)]
                    break
        for island in range(self._island):
            while True:
                checks = []
                taken = False
                x_coord = random.randint(0, X_DIMENSION - 1)
                y_coord = random.randint(0, Y_DIMENSION - 1)
                checks.append((x_coord, y_coord))
                start = [x_coord - (obj_stats['island'][0] - 1) / 2,
                         y_coord - (obj_stats['island'][0] - 1) / 2]
                for i in range(obj_stats['island'][0]):
                    start[1] += i
                    for j in range(obj_stats['island'][0]):
                        start[0] += j
                        checks.append(tuple(start))
                for check in checks:
                    if check in self._taken:
                        taken = True
                        break
                if not taken:
                    for check in checks:
                        self._taken.append(check)
                        self._locations[uuid.uuid4()] = ['island', (x_coord, y_coord)]
                    print('Island detected at: ' + str((x_coord, y_coord)))
                    self._objects[uuid.uuid4()] = ['island', (x_coord,y_coord)]
                    break
        for port in range(self._port):
            while True:
                checks = []
                taken = False
                x_coord = random.randint(0, X_DIMENSION - 1)
                y_coord = random.randint(0, Y_DIMENSION - 1)
                checks.append((x_coord, y_coord))
                start = [x_coord - (obj_stats['port'][0] - 1) / 2,
                         y_coord - (obj_stats['port'][0] - 1) / 2]
                for i in range(obj_stats['port'][0]):
                    start[1] += i
                    for j in range(obj_stats['port'][0]):
                        start[0] += j
                        checks.append(tuple(start))
                for check in checks:
                    if check in self._taken:
                        taken = True
                        break
                if not taken:
                    for check in checks:
                        self._taken.append(check)
                        self._locations[uuid.uuid4()] = ['port', (x_coord, y_coord)]
                    print('Port detected at: ' + str((x_coord, y_coord)))
                    self._objects[uuid.uuid4()] = ['port', (x_coord,y_coord)]
                    break
        for navy in range(self._navy):
            while True:
                taken = False
                x_coord = random.randint(0, X_DIMENSION - 1) 
                y_coord = random.randint(0, Y_DIMENSION - 1)
                if (x_coord, y_coord) not in self._taken:
                    self._taken.append((x_coord, y_coord))
                    self._locations[uuid.uuid4()] = ['navy', (x_coord, y_coord)]
                    print('Navy ship detected at: ' + str((x_coord, y_coord)))
                    self._objects[uuid.uuid4()] = ['navy', (x_coord,y_coord)]
                    break
        for treasure in range(self._treasure):
            while True:
                taken = False
                x_coord = random.randint(0, X_DIMENSION - 1)
                y_coord = random.randint(0, Y_DIMENSION - 1)
                if (x_coord, y_coord) not in self._taken and \
                        math.sqrt((x_coord - self._last[0]) ** 2 + (y_coord - self._last[1]) ** 2) > 60:
                    self._taken.append((x_coord, y_coord))
                    self._locations[uuid.uuid4()] = ['treasure', (x_coord, y_coord)]
                    print('Treasure detected at: ' + str((x_coord, y_coord)))
                    self._objects[uuid.uuid4()] = ['treasure', (x_coord,y_coord)]
                    break
        print('The map has been completed')

    def update(self, new_coord):
        """
        Changes the map for navy and for pirate ship
        :param new_coord: tuple of 2 ints of new coord of ship
        :return: updated taken list
        """
        print('The Navy is on the move...')
        self._taken.remove(self._last)
        self._last = new_coord
        #self._objects = {}
        new_locations = {}
        for ID, info in self._objects.items():
            navy = info[0]
            coord = info[1]
            if navy == 'navy':
                while True:
                    x_move = random.randint(-1, 1)
                    y_move = random.randint(-1, 1)
                    if (coord[0] + x_move, coord[1] + y_move) not in self._taken:
                        self._taken.append((coord[0] + x_move, coord[1] + y_move))
                        new_locations[ID] = ['navy', (coord[0] + x_move, coord[1] + y_move)]
                        #self._objects[uuid.uuid4()] = ['navy', (coord[0] + x_move, coord[1] + y_move)]
                        print('New Navy locations: ' + str((coord[0] + x_move, coord[1] + y_move)))
                        break
            else:
                new_locations[ID] = [navy, coord]
                #self._objects[uuid.uuid4()] = [navy, coord]
        self._locations = new_locations
        self._objects = new_locations
        print("+++++++++++++AFTER++++++++++++++++++")
        for ID, info in self._objects.items():
            print(info[0], info[1])
        self._taken.append(new_coord)
        if crash(new_coord, new_locations):
            return 'game over'

    def retrieve(self):
        """
        Just retrieves the locations mapping
        :return: dictionary of locations
        """
        return self._locations


class Pirate:
    """
    Pirate ship you want to catch
    """
    def __init__(self, x_start, y_start, wind, leadership):
        """
        Initializes
        :param x_start: int in board
        :param y_start: int in board
        :param wind: tuple (direction (1-8), strength int)
        :param leadership: int between 0 & 10
        """
        self._location = [x_start, y_start]
        x_wind_mult = 0
        y_wind_mult = 0
        # North
        if wind[0] == 1 or 2 or 8:
            y_wind_mult = +1
        # East
        if wind[0] == 2 or 3 or 4:
            x_wind_mult = +1
        # South
        if wind[0] == 4 or 5 or 6:
            y_wind_mult = -1
        # West
        if wind[0] == 6 or 7 or 8:
            x_wind_mult = -1
        # If not cardinal direction
        if wind[0] % 2 == 0:
            x_wind_mult *= int(math.sqrt(wind[1]))
            y_wind_mult *= int(math.sqrt(wind[1]))
        # Cardinal directions
        else:
            x_wind_mult *= wind[1]
            y_wind_mult *= wind[1]
        self._wind = (x_wind_mult, y_wind_mult)
        self._leadership = int(leadership) / 10

    def move(self, locations):
        """
        Moves the ship in accordance with surrounding hazards
        :param locations: dictionary; keys: Obstacle ID, value: coordinate
        :return: the new coordinates of the ship
        """
        print('The ship has raised its sails!')
        for i in range(10):
            # Calculates the probability
            x_right = 0
            x_stay = 0
            x_left = 0
            y_up = 0
            y_stay = 0
            y_down = 0
            for ID, info in locations.items():
                location = info[0]
                coord = info[1]
                if (math.sqrt(coord[0] ** 2 + coord[1] ** 2) > 20) and \
                        (location != 'treasure'):
                    continue
                if coord[0] - (self._location[0] - 1) == 0:
                    x_left < -1
                else:
                    x_left += obj_stats[location][1] * self._leadership * \
                          X_DIMENSION / abs(coord[0] - (self._location[0] - 1))
                if x_left < 0:
                    x_left = 0
                    x_right -= x_left
                x_stay += obj_stats[location][1] * self._leadership * \
                          X_DIMENSION / abs(coord[0] - (self._location[0]))
                if x_stay < 0:
                    x_stay = 0
                if coord[0] - (self._location[0] + 1) == 0:
                    x_right = -1
                else:
                    x_right += obj_stats[location][1] * self._leadership * \
                           X_DIMENSION / abs(coord[0] - (self._location[0] + 1))
                if x_right < 0:
                    x_right = 0
                    x_left -= x_right
                if coord[1] - (self._location[1] - 1) == 0:
                    y_down = -1
                else:
                    y_down += obj_stats[location][1] * self._leadership * \
                          Y_DIMENSION / abs(coord[1] - (self._location[1] - 1))
                if y_down < 0:
                    y_down = 0
                    y_up -= y_down
                y_stay += obj_stats[location][1] * self._leadership * \
                          Y_DIMENSION / abs(coord[1] - (self._location[1]))
                if y_stay < 0:
                    y_stay = 0
                if coord[1] - (self._location[1] + 1) == 0:
                    y_up = -1
                else:
                    y_up += obj_stats[location][1] * self._leadership * \
                        Y_DIMENSION / abs(coord[1] - (self._location[1] + 1))
                if y_up < 0:
                    y_up = 0
                    y_down -= y_up
            while True:
                # Implements the move itself
                x_total = math.floor(x_left + x_stay + x_right)
                x_probs = {-1: x_left, 0: x_stay, +1: x_right}
                x_move = None
                chance = random.randint(0, x_total)
                grey_chance = 0
                for space, prob in x_probs.items():
                    grey_chance += prob
                    if grey_chance > chance:
                        x_move = space
                        break
                y_total = math.floor(y_down + y_stay + y_up)
                y_probs = {-1: y_down, 0: y_stay, +1: y_up}
                y_move = None
                chance = random.randint(0, y_total)
                grey_chance = 0
                for space, prob in y_probs.items():
                    grey_chance += prob
                    if grey_chance > chance:
                        y_move = space
                        break
                self._location[0] += x_move
                self._location[1] += y_move
                # Checks if it crashes
                if crash(self._location, locations):
                    return 'game over'
                # Makes sure it's not out of bounds
                if 0 <= self._location[0] <= 200 and 0 <= self._location[1] <= 200:
                    print('New Coords: ' + str(self._location))
                    break
        # Impmlements wind
        if self._wind[1] != 0:
            print('The wind blows...')
            if 0 <= self._location[0] + self._wind[0] <= X_DIMENSION:
                self._location[0] += self._wind[0]
            else:
                if self._wind[0] > 0:
                    self._location[0] = X_DIMENSION
                if self._wind[0] < 0:
                    self._location[0] = 0
            if 0 <= self._location[1] + self._wind[1] <= Y_DIMENSION:
                self._location[1] += self._wind[1]
            else:
                if self._wind[1] > 0:
                    self._location[1] = Y_DIMENSION
                if self._wind[1] < 0:
                    self._location[1] = 0
            if crash(self._location, locations):
                return 'game over'
        print('The ship lowers its anchor at ' + str(self._location) + ' for the night')
        return self._location

    def get_location(self):
        return self._location


class Target:
    """
    The prediction of where the pirate ship will be
    """

    def __init__(self, x_coord, y_coord):
        self._target = [x_coord, y_coord]
        self._original = (x_coord, y_coord)
        self._last = (x_coord, y_coord)

    def move(self):
        while True:
            while True:
                direction = input('Which direction do you want to move in? (Up/Down/Left/Right) ')
                if direction == 'Up' or \
                        direction == 'Down' or \
                        direction == 'Right' or \
                        direction == 'Left':
                    break
                print('Type a valid input')
            while True:
                strength = int(input('How many units would you like to move in this direction? '))
                if direction == 'Up':
                    if self._target[1] + strength <= self._last[1] + 4:
                        if self._target[1] + strength <= Y_DIMENSION:
                            self._target[1] += strength
                            break
                        else:
                            print('Input out of bounds; Try again')
                    else:
                        print('Input out of bounds; Try again')
                if direction == 'Down':
                    if self._target[1] - strength <= self._last[1] - 4:
                        if Y_DIMENSION <= self._target[1] - strength:
                            self._target[1] -= strength
                            break
                        else:
                            print('Input out of bounds; Try again')
                    else:
                        print('Input out of bounds; Try again')
                if direction == 'Left':
                    if self._target[0] - strength <= self._last[0] - 4:
                        if X_DIMENSION <= self._target[0] - strength:
                            self._target[0] -= strength
                            break
                        else:
                            print('Input out of bounds; Try again')
                    else:
                        print('Input out of bounds; Try again')
                if direction == 'Right':
                    if self._target[0] + strength <= self._last[0] + 4:
                        if self._target[0] + strength <= X_DIMENSION:
                            self._target[0] += strength
                            break
                        else:
                            print('Input out of bounds; Try again')
                    else:
                        print('Input out of bounds; Try again')
            print('New trap location: ' + str(self._target))
            cont = input('Are you satisfied with your new trap location? (Y/N) ')
            if cont == 'Y':
                break

    def score(self, pirate):
        """
        Tabulates score
        :return: Returns a score (higher is better)
        """
        # Determines based on how far you were from pirate
        print('Margin of error: ' +
              str(math.sqrt((pirate[1] - self._target[1]) ** 2 + (pirate[0] - self._target[0]) ** 2)))
        if math.sqrt((pirate[1] - self._target[1]) ** 2 + (pirate[0] - self._target[0]) ** 2) == 0:
            score = (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2))
        else:
            score = (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2)) / \
                (math.sqrt((pirate[1] - self._target[1]) ** 2 + (pirate[0] - self._target[0]) ** 2))
        print('Number of adjustments: ' +
              str(math.sqrt((self._original[1] - self._target[1]) ** 2 + (self._original[0] - self._target[0]) ** 2)))
        if math.sqrt((self._original[1] - self._target[1]) ** 2 + (self._original[0] - self._target[0]) ** 2) == 0:
            score += (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2))
        else:
            score += (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2)) / \
                 (math.sqrt((self._original[1] - self._target[1]) ** 2 + (self._original[0] - self._target[0]) ** 2))
        print('FINAL SCORE: ' + str(score))
        return score
    def getScores(self, pirate):
        """
        Tabulates score
        :return: Returns margin of error, number of adjustments, and score (higher is better)
        """
        # Determines based on how far you were from pirate
        
        margin_of_error = math.sqrt((pirate[1] - self._target[1]) ** 2 + (pirate[0] - self._target[0]) ** 2)
        if math.sqrt((pirate[1] - self._target[1]) ** 2 + (pirate[0] - self._target[0]) ** 2) == 0:
            score = (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2))
        else:
            score = (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2)) / \
                (math.sqrt((pirate[1] - self._target[1]) ** 2 + (pirate[0] - self._target[0]) ** 2))
        num_adjustments = math.sqrt((self._original[1] - self._target[1]) ** 2 + (self._original[0] - self._target[0]) ** 2)
        if math.sqrt((self._original[1] - self._target[1]) ** 2 + (self._original[0] - self._target[0]) ** 2) == 0:
            score += (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2))
        else:
            score += (math.sqrt(X_DIMENSION ** 2 + Y_DIMENSION ** 2)) / \
                 (math.sqrt((self._original[1] - self._target[1]) ** 2 + (self._original[0] - self._target[0]) ** 2))
        return margin_of_error, num_adjustments, score


    def get_target(self):
        """
        Gets the guess
        :return: The last guess you made
        """
        return self._target


def run(players):
    """
    Plays the fucking game no shit
    :param players: int of number of players (1 - 4)
    :return: a game (we do need a map tho)
    """
    # Sets up the board\
    global qtyphoon, qnavy, qisland, qtreasure, qport, wind, leadership, turns, enemy, map
    qtyphoon = random.randint(TYPH_MIN, TYPH_MAX)
    qnavy = random.randint(NAVY_MIN, NAVY_MAX)
    qisland = random.randint(ISLAND_MIN, ISLAND_MAX)
    qtreasure = TREASURE_QUANT
    qport = random.randint(PORT_MIN, PORT_MAX)
    wind = (random.randint(WIND_DIRECTION[0], WIND_DIRECTION[1]), random.randint(WIND_SPEED[0], WIND_SPEED[1]))
    leadership = random.randint(LEADERSHIP_SCALE[0], LEADERSHIP_SCALE[1])
    turns = random.randint(TURN_NUM[0], TURN_NUM[1])
    start_location = (random.randint(0, X_DIMENSION - 1), random.randint(0, Y_DIMENSION - 1))
    enemy = Pirate(start_location[0], start_location[1], wind, leadership)
    map = Board(X_DIMENSION, Y_DIMENSION, qtyphoon, qnavy, qisland, qtreasure, qport, start_location)
    
    print('==== BOUNTY INFORMATION ====')
    print('Target: Pirates')
    print('Last seen: ' + str(start_location))
    print('Leadership: ' + str(leadership) + '/10')
    print('')
    print("Here's a map to get you started")
    map.create()
    # create pygame 
    drawBoard(start_location, players, turns)

    # if wind[1] != 0:
    #     if wind[0] == 1:
    #         print('The winds are blowing North at ' + str(wind[1]) + ' units/day')
    #     if wind[0] == 2:
    #         print('The winds are blowing Northeast at ' + str(wind[1]) + ' units/day')
    #     if wind[0] == 3:
    #         print('The winds are blowing East at ' + str(wind[1]) + ' units/day')
    #     if wind[0] == 4:
    #         print('The winds are blowing Southeast at ' + str(wind[1]) + ' units/day')
    #     if wind[0] == 5:
    #         print('The winds are blowing South at ' + str(wind[1]) + ' units/day')
    #     if wind[0] == 6:
    #         print('The winds are blowing Southwest at ' + str(wind[1]) + ' units/day')
    #     if wind[0] == 7:
    #         print('The winds are blowing West at ' + str(wind[1]) + ' units/day')
    #     if wind[0] == 8:
    #         print('The winds are blowing Northwest at ' + str(wind[1]) + ' units/day')
    
       
def drawBoard(start_location, players, turns):
    global SCREEN, CLOCK, GRID
    global targets
    global player1, player2, player3, player4
    player1 = 0
    player2 = 0
    player3 = 0
    player4 = 0
    targets = [player1, player2, player3, player4]
    GRID = []
    GRID = createGrid(start_location)
    numRow = 200
    
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLUE)

    pirateShip = pygame.Surface((TILE_SIZE, TILE_SIZE))
    pirateShip.fill(RED)
    
    
    drawGrid()
    

    pirateShipStartX, pirateShipStartY = start_location
    print(start_location)
    current_location = ""
    SCREEN.blit(pirateShip, (0,0) )

    player_target_selection = [0] * players
    player_target_selection[0] = 1
    currentPlayer = 0
    playingPlayer = 0
    target_selection_stage = True
    new_spot = 0
    new_spot_created = False
    day = 1 # day increments when players decide on adjustments 
    maxDays = turns + 2
    game_over = False
    day_stage = False # will become true when target select stage is done, will become false again after days are over ( days == maxDays)
    make_adjustments = "" # will player make adjustments, changes when button is pressed 
    finished_adjusting = False
    adjustmentStage = False
    while True:
        CLOCK.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if target_selection_stage:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (TILE_SIZE)
                    row = pos[1] // (TILE_SIZE)
                    # Set that location to one
                    GRID[row][column] = "targeted"
                    # if current_location == "":
                    #     current_location = (column, row)
                    # else:
                    #     oldR, oldC = current_location
                    #     GRID[oldR][oldC] = 0
                    #     current_location = (column, row)
                    choice = []
                    x_selection, y_selection = convertToXY((row, column))
                    choice.append(x_selection)
                    choice.append(y_selection)
                    if currentPlayer == 0:
                        player1 = Target(choice[0], choice[1])
                        targets[0] = player1
                        currentPlayer+=1
                    elif currentPlayer == 1:
                        player2 = Target(choice[0], choice[1])
                        targets[1] = player2
                        currentPlayer+=1
                    elif currentPlayer == 2:
                        player3 = Target(choice[0], choice[1])
                        targets[2] = player3
                        currentPlayer+=1
                    elif currentPlayer == 3:
                        player4 = Target(choice[0], choice[1])
                        targets[3] = player4
                        currentPlayer+=1
                    if currentPlayer >= players:
                        target_selection_stage = False
                        day_stage = True
                    print("Click ", pos, "Grid coordinates: ", row, column, "Cardinal: ", x_selection, y_selection)
                if day_stage and adjustmentStage == False:
                    pos = pygame.mouse.get_pos()
                    if 450 + 50 > pos[0] > 450  and 600 + 50 > pos[1] > 600:
                        make_adjustments = True
                    if 525 + 50 > pos[0] > 525  and 600 + 50 > pos[1] > 600:
                        make_adjustments = False 
                if adjustmentStage == True:
                    pos = pygame.mouse.get_pos()
                    if 450 + 50 > pos[0] > 450  and 600 + 50 > pos[1] > 600:
                        finished_adjusting = True
            elif event.type == pygame.KEYDOWN:
                if adjustmentStage:
                    direction = ""
                    targetToMove = ""
                    current_location = enemy.get_location()
                    x = current_location[0]
                    y = current_location[1]
                    if playingPlayer == 0:
                        targetToMove = player1
                    elif playingPlayer == 1:
                        targetToMove = player2
                    elif playingPlayer == 2:
                        targetToMove = player3
                    elif playingPlayer == 3:
                        targetToMove = player4
                    if event.key == pygame.K_LEFT:
                        print("left")
                        direction = "Left"
                        newTarget = moveShip(targetToMove, "Left")
                        targets[playingPlayer] = newTarget
                        GRID = createGrid((x, y))
                        drawGrid()
                    if event.key == pygame.K_RIGHT:
                        print("right")
                        direction = "Right"
                        newTarget = moveShip(targetToMove, "Right")
                        targets[playingPlayer] = newTarget
                        GRID = createGrid((x, y))
                        drawGrid()
                    if event.key == pygame.K_UP:
                        print("up")
                        direction = "Up"
                        newTarget = moveShip(targetToMove, "Up")
                        targets[playingPlayer] = newTarget
                        GRID = createGrid((x, y))
                        drawGrid()
                    if event.key == pygame.K_DOWN:
                        print("down")
                        direction = "Down"
                        newTarget = moveShip(targetToMove, "Down")
                        targets[playingPlayer] = newTarget
                        GRID = createGrid((x, y))
                        drawGrid()
                    # make adjustments   
        # players are selecting their initial targets 
        if target_selection_stage: 
            setText('It is player ' + str(currentPlayer + 1) + "'s turn! Choose a target location.")
            drawGrid()
        elif day_stage: # day stage 
            if day < turns + 2:
                setText("Day " + str(day))
                drawGrid()
            else:
                setText("The Ship sails one last time!")
                drawGrid()
            if new_spot_created == False: # get new spot of pirate ship 
                new_spot = enemy.move(map.retrieve())
                print(new_spot)
               
                new_spot_created = True
                if new_spot == "game over":
                    day_stage = False
                    setText("Game Over!")
                    drawGrid()
                    continue
                map.update(new_spot)
                GRID = createGrid(new_spot) # PROBLEM: This overrides the target locations 
                drawGrid() #redraw new navy locations 
                print("===================== Redraw ======================")
                # if map.update(new_spot) == "game over": # this does update twice 
                #     day_stage = False
                #     setText("Game Over!")
                #     drawGrid()
                #     continue
            if day == turns + 1: # days have ended, day stage is done 
                day_stage = False
                continue
            if day < turns + 1:
                setText('Day ' + str(day) + ': It is player ' + str(playingPlayer + 1) + "'s turn! Make adjustments?")
                drawGrid()
                drawButtons() # draw adjustment buttons (Y/N)
                if make_adjustments != "":
                    if make_adjustments == False:
                        #day += 1
                        make_adjustments = ""
                        adjustmentStage = False
                        playingPlayer+=1
                        #continue
                    elif make_adjustments:
                        adjustmentStage = True
                    if playingPlayer >= players: # NOTE: might be better to move this method after if m_a != "", then uncomment continue 
                        day+=1
                        make_adjustments = ""
                        new_spot_created = False
                        playingPlayer = 0
                        print(new_spot_created, "+===============================================")
                        continue
                    if make_adjustments and playingPlayer == 0: # prompt players to make adjustments 
                        adjustLocation(player1)
                        
                        if finished_adjusting:
                            playingPlayer+=1
                            finished_adjusting = False
                        #player1.move()
                    elif make_adjustments and playingPlayer == 1:
                        adjustLocation(player2)
                        
                        if finished_adjusting:
                            playingPlayer+=1
                            finished_adjusting = False
                        #player2.move()
                    elif make_adjustments and playingPlayer == 2:
                        adjustLocation(player3)
                        
                        if finished_adjusting:
                            playingPlayer+=1
                            finished_adjusting = False
                        #player3.move()
                    elif make_adjustments and playingPlayer == 3:
                        adjustLocation(player4)
                        
                        if finished_adjusting:
                            playingPlayer+=1
                            finished_adjusting = False
                        #player4.move()
                elif make_adjustments == "":
                    adjustmentStage = False
        else:
            setText("Game Done")
            drawGrid()
            print("The Pirate's final location: " + str(enemy.get_location()))
            print('=== SCORE BOARD ===')
            for player in range(players):
                if player == 0:
                    print('PLAYER 1')
                    print('Final target location: ' + str(player1.get_target()))
                    player1.score(enemy.get_location())
                    print('')
                if player == 1:
                    print('PLAYER 2')
                    print('Final target location: ' + str(player2.get_target()))
                    player2.score(enemy.get_location())
                    print('')
                if player == 2:
                    print('PLAYER 3')
                    print('Final target location: ' + str(player3.get_target()))
                    player3.score(enemy.get_location())
                    print('')
                if player == 3:
                    print('PLAYER 4')
                    print('Final target location: ' + str(player4.get_target()))
                    player4.score(enemy.get_location())
                    print('')
            break
        CLOCK.tick(30)
        #print(CLOCK.get_fps())
        pygame.display.update()

    # display end game screen
    SCREEN.fill(BLUE)
    center = 200
    while True:
        CLOCK.tick(60)
        SCREEN.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        font = pygame.font.SysFont(None, 25)
        img = font.render("Game Done", True, BLACK)
        SCREEN.blit(img, (center, 10))
        text1 = "The Pirate's final location: " + str(enemy.get_location())
        text2 = "=== SCORE BOARD ==="
        img2 = font.render(text1, True, BLACK)
        img3 = font.render(text2, True, BLACK)
        SCREEN.blit(img2, (center, 30))
        SCREEN.blit(img3, (center, 50))
        start = 80
        for player in range(players):
            margin_of_error = 0
            num_adjustments = 0
            score = 0
            player_text = ""
            target_text = ""

            if player == 0:
                player_text = "PLAYER 1"
                target_text = 'Final target location: ' + str(player1.get_target())
                margin_of_error, num_adjustments, score = player1.getScores(enemy.get_location())        
            if player == 1:
                player_text = "PLAYER 2"
                target_text = 'Final target location: ' + str(player2.get_target())
                margin_of_error, num_adjustments, score = player2.getScores(enemy.get_location())        
            if player == 2:
                player_text = "PLAYER 3"
                target_text = 'Final target location: ' + str(player3.get_target())
                margin_of_error, num_adjustments, score = player3.getScores(enemy.get_location())              
            if player == 3:
                player_text = "PLAYER 4"
                target_text = 'Final target location: ' + str(player4.get_target())
                margin_of_error, num_adjustments, score = player4.getScores(enemy.get_location())
            # Display text for each player
            t1 = font.render(player_text, True, BLACK)
            t2 = font.render(target_text, True, BLACK)
            t3 = font.render('Margin of Error: ' + str(margin_of_error), True, BLACK)
            t4 = font.render('Number of Adjustments: ' + str(num_adjustments), True, BLACK)
            t5 = font.render('Final Score: ' + str(score), True, BLACK)
            text_list = [t1, t2, t3, t4, t5]
            for t in text_list:
                SCREEN.blit(t, (center, start))
                start+=30
        #SCREEN.fill(BLUE)
        pygame.display.update()

    
def moveShip(self, direction): # changes location of target in grid, will not change if out of bounds 
    strength = 1
    if direction == 'Up':
        if self._target[1] + strength <= self._last[1] + 4:
            if self._target[1] + strength <= Y_DIMENSION:
                self._target[1] += strength
                
            else:
                print('Input out of bounds; Try again')
        else:
            print('Input out of bounds; Try again')
    if direction == 'Down':
        if self._target[1] - strength <= self._last[1] - 4:
            if Y_DIMENSION <= self._target[1] - strength:
                self._target[1] -= strength
                
            else:
                print('Input out of bounds; Try again')
        else:
            print('Input out of bounds; Try again')
    if direction == 'Left':
        if self._target[0] - strength <= self._last[0] - 4:
            if X_DIMENSION <= self._target[0] - strength:
                self._target[0] -= strength
                
            else:
                print('Input out of bounds; Try again')
        else:
            print('Input out of bounds; Try again')
    if direction == 'Right':
        if self._target[0] + strength <= self._last[0] + 4:
            if self._target[0] + strength <= X_DIMENSION:
                self._target[0] += strength
                
            else:
                print('Input out of bounds; Try again')
        else:
            print('Input out of bounds; Try again')
    newLocation = self.get_target()
    print(newLocation)
    return self

def adjustLocation(player): # player is a target object, shows adjust location gui
    setText("Use arrow keys to adjust target location")
    pygame.draw.rect(SCREEN, BLUE, (450, 600, 50, 50))
    pygame.draw.rect(SCREEN, BLUE, (450, 600, 50, 50))
    pos = pygame.mouse.get_pos()
    if 450 + 50 > pos[0] > 450  and 600 + 50 > pos[1] > 600:
        pygame.draw.rect(SCREEN, BRIGHT_GREEN, (450, 600, 50, 50))
    else:
        pygame.draw.rect(SCREEN, GREEN, (450, 600, 50, 50))
    drawGrid()

def drawButtons():
    pos = pygame.mouse.get_pos()
    if 450 + 50 > pos[0] > 450  and 600 + 50 > pos[1] > 600:
        pygame.draw.rect(SCREEN, BRIGHT_GREEN, (450, 600, 50, 50))
    else:
        pygame.draw.rect(SCREEN, GREEN, (450, 600, 50, 50))
    if 525 + 50 > pos[0] > 525  and 600 + 50 > pos[1] > 600:
        pygame.draw.rect(SCREEN, BRIGHT_RED, (525, 600, 50, 50))
    else:
        pygame.draw.rect(SCREEN, RED, (525, 600, 50, 50))

def setText(text):
    SCREEN.fill(BLUE)
    font = pygame.font.SysFont(None, 25)
    img = font.render(text, True, BLACK)
    SCREEN.blit(img, (10, 620))

def drawText():
    font = pygame.font.SysFont(None, 30)
    img = font.render('Choose a location', True, BLACK)
    SCREEN.blit(img, (20, 620)) 

def drawGrid():
    blockSize = TILE_SIZE #Set the size of the grid block
    num = 0
    # draw initial board 
    for row in range(Y_DIMENSION):
        for col in range(X_DIMENSION):
            color = WHITE
            rect = pygame.Rect(row*blockSize, col*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, color, rect, 1)
    # blit objects onto grid
    size = TILE_SIZE
    for row in range(Y_DIMENSION):
        for col in range(X_DIMENSION):
            if(GRID[row][col] == "pirate"):
                color = RED
            elif(GRID[row][col] == "typhoon"):
                color = PURPLE
            elif(GRID[row][col] == "island"):
                color = GREEN
            elif(GRID[row][col] == "port"):
                color = BLACK
            elif(GRID[row][col] == "navy"):
                #print("+++++++++++++++++++", row, col)
                color = BLUE
            elif(GRID[row][col] == "treasure"):
                color = YELLOW
            elif(GRID[row][col] == "targeted"):
                #print("+++++++++++++++++++", row, col)
                color = ORANGE
            else:
                continue
            thing = pygame.Surface((size, size))
            thing.fill(color)
            x, y = convertToXY((row, col))
            SCREEN.blit(thing, (col* TILE_SIZE, row* TILE_SIZE)) # PROBLEM HERE, NOT DISPLAYING IN THE RIGHT PLACE


def drawIslands():
    numIslands = 25
    for i in range(numIslands):
        randX = random.randint(0, WINDOW_WIDTH)
        randY = random.randint(0, WINDOW_HEIGHT)
        island = pygame.Surface((50, 50))
        island.fill(GREEN)
        SCREEN.blit(island, (randX, randY))
# createGrid should take in a targets location array as a parameter
def createGrid(start_location): # converts board into a 2d array called GRID
    # still need to identify each player's targets 
    GRID = [[0 for x in range(X_DIMENSION)] for y in range(Y_DIMENSION)]
    start_x, start_y = convertCords(start_location)
    GRID[start_x][start_y] = "pirate"
    objects = map._objects
    for key in map._objects:
        thing = map._objects[key]
        name = thing[0]
        r, c = convertCords(thing[1])
        print(name, thing[1], "--->", r, c)
        GRID[r][c] = name
    for target in targets:
        if target != 0:
            location = target.get_target()
            print(location)
            x = location[0]
            y = location[1]
            r, c = convertCords((x,y))
            GRID[r][c] = "targeted"
            print("yes ---------------------------------------------",r,c)

    return GRID

def convertCords(location):
    x, y = location
    col = x 
    row = 200 - y - 1
    #print(x, y, "-->",row,col)
    #ERROR if (x,y) = (200,  31), coords are from 0 - 200 while array indexes are from 0 - 199
    return row, col

def convertToXY(location):
    row, col = location
    x = col
    y = 199 - row
    return x, y



run(1)
