import random
import math
import uuid

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

    def create(self):
        """
        Creates a board so that nothing is touching
        """
        print('Drawing up the map...')
        for typhoon in range(self._typhoon):
            while True:
                checks = []
                taken = False
                x_coord = random.randint(0, X_DIMENSION)
                y_coord = random.randint(0, Y_DIMENSION)
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
                    break
        for island in range(self._island):
            while True:
                checks = []
                taken = False
                x_coord = random.randint(0, X_DIMENSION)
                y_coord = random.randint(0, Y_DIMENSION)
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
                    break
        for port in range(self._port):
            while True:
                checks = []
                taken = False
                x_coord = random.randint(0, X_DIMENSION)
                y_coord = random.randint(0, Y_DIMENSION)
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
                    break
        for navy in range(self._navy):
            while True:
                taken = False
                x_coord = random.randint(0, X_DIMENSION)
                y_coord = random.randint(0, Y_DIMENSION)
                if (x_coord, y_coord) not in self._taken:
                    self._taken.append((x_coord, y_coord))
                    self._locations[uuid.uuid4()] = ['navy', (x_coord, y_coord)]
                    print('Navy ship detected at: ' + str((x_coord, y_coord)))
                    break
        for treasure in range(self._treasure):
            while True:
                taken = False
                x_coord = random.randint(0, X_DIMENSION)
                y_coord = random.randint(0, Y_DIMENSION)
                if (x_coord, y_coord) not in self._taken and \
                        math.sqrt((x_coord - self._last[0]) ** 2 + (y_coord - self._last[1]) ** 2) > 60:
                    self._taken.append((x_coord, y_coord))
                    self._locations[uuid.uuid4()] = ['treasure', (x_coord, y_coord)]
                    print('Treasure detected at: ' + str((x_coord, y_coord)))
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
        new_locations = {}
        for ID, info in self._locations.items():
            navy = info[0]
            coord = info[1]
            if navy == 'navy':
                while True:
                    x_move = random.randint(-1, 1)
                    y_move = random.randint(-1, 1)
                    if (coord[0] + x_move, coord[1] + y_move) not in self._taken:
                        self._taken.append((coord[0] + x_move, coord[1] + y_move))
                        new_locations[ID] = ['navy', (coord[0] + x_move, coord[1] + y_move)]
                        print('New Navy locations: ' + str((coord[0] + x_move, coord[1] + y_move)))
                        break
            else:
                new_locations[ID] = [navy, coord]
        self._locations = new_locations
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
    # Sets up the board
    qtyphoon = random.randint(TYPH_MIN, TYPH_MAX)
    qnavy = random.randint(NAVY_MIN, NAVY_MAX)
    qisland = random.randint(ISLAND_MIN, ISLAND_MAX)
    qtreasure = TREASURE_QUANT
    qport = random.randint(PORT_MIN, PORT_MAX)
    wind = (random.randint(WIND_DIRECTION[0], WIND_DIRECTION[1]), random.randint(WIND_SPEED[0], WIND_SPEED[1]))
    leadership = random.randint(LEADERSHIP_SCALE[0], LEADERSHIP_SCALE[1])
    turns = random.randint(TURN_NUM[0], TURN_NUM[1])
    start_location = (random.randint(0, X_DIMENSION), random.randint(0, Y_DIMENSION))
    enemy = Pirate(start_location[0], start_location[1], wind, leadership)
    map = Board(X_DIMENSION, Y_DIMENSION, qtyphoon, qnavy, qisland, qtreasure, qport, start_location)
    print('==== BOUNTY INFORMATION ====')
    print('Target: Pirates')
    print('Last seen: ' + str(start_location))
    print('Leadership: ' + str(leadership) + '/10')
    print('')
    print("Here's a map to get you started")
    map.create()
    if wind[1] != 0:
        if wind[0] == 1:
            print('The winds are blowing North at ' + str(wind[1]) + ' units/day')
        if wind[0] == 2:
            print('The winds are blowing Northeast at ' + str(wind[1]) + ' units/day')
        if wind[0] == 3:
            print('The winds are blowing East at ' + str(wind[1]) + ' units/day')
        if wind[0] == 4:
            print('The winds are blowing Southeast at ' + str(wind[1]) + ' units/day')
        if wind[0] == 5:
            print('The winds are blowing South at ' + str(wind[1]) + ' units/day')
        if wind[0] == 6:
            print('The winds are blowing Southwest at ' + str(wind[1]) + ' units/day')
        if wind[0] == 7:
            print('The winds are blowing West at ' + str(wind[1]) + ' units/day')
        if wind[0] == 8:
            print('The winds are blowing Northwest at ' + str(wind[1]) + ' units/day')

    for player in range(players):
        print('')
        print('It is player ' + str(player + 1) + "'s turn!")
        choice = []
        choice.append(int(input('Choose an x coordinate: ')))
        choice.append(int(input('Choose a y coordinate: ')))
        if player == 0:
            player1 = Target(choice[0], choice[1])
        if player == 1:
            player2 = Target(choice[0], choice[1])
        if player == 2:
            player3 = Target(choice[0], choice[1])
        if player == 3:
            player4 = Target(choice[0], choice[1])

    for day in range(1, turns + 2):
        print('===')
        if day < turns + 2:
            print('Day: ' + str(day))
        else:
            print('The Ship sails one last time!')
        new_spot = enemy.move(map.retrieve())
        print('')
        if new_spot == 'game over':
            print('=====')
            print('Game Over!')
            break
        map.update(new_spot)
        if map.update(new_spot) == 'game over':
            print('=====')
            print('Game Over!')
            break
        if day == turns + 2:
            print('=====')
            print('Game Over!')
            break
        if day < (turns + 2):
            for player in range(players):
                print('')
                print('It is player ' + str(player + 1) + "'s turn!")
                choice = input('Adjust your prediction? (Y/N) ')
                if choice == 'N':
                    continue
                if player == 0:
                    player1.move()
                if player == 1:
                    player2.move()
                if player == 2:
                    player3.move()
                if player == 3:
                    player4.move()
    print('')
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

run(1)