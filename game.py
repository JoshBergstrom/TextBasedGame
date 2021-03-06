
import cmd
import textwrap
import sys
import os
import time
import random
import emoji
from termcolor import colored, cprint

screen_width = 500
###Player Setup###
class player:
    def __init__(self):
        self.name = ''
        self.hp = 000
        self.mp = 000
        self.type = ''
        self.location = 'e4'
        self.gameOver = False
        self.atk = 0
myplayer = player()

class enemy:
    def __init__(self):
        self.hp
        self.atk
        self.name

###Title Screens###
def title_screen_selections():
    option = raw_input("> ")
    if option.lower() == ('play'):
        setup_game()
    elif option.lower() == ('help'):
        help_screen()
    elif option.lower() == ('back'):
        title_screen()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'back', 'quit']:
        print("invalded command")
        option = raw_input("> ")
        if option.lower() == ('play'):
            setup_game()
        elif option.lower() == ('help'):
            help_screen()
        elif option.lower() == ('back'):
            title_screen()
        elif option.lower() == ('quit'):
            sys.exit()
def title_screen():
    os.system('clear')
    print("-----------------------------------------------------------")
    print("-                         Welcome                         -")
    print("-----------------------------------------------------------")
    print("-                          -Play-                         -")
    print("-                          -Help-                         -")
    print("-                          -Quit-                         -")
    print("-----------------------------------------------------------")
    title_screen_selections()
def help_screen():
    os.system('clear')
    print("-Back-------------------------------------------------------")
    print("-                  The best help I can give                -")
    print("-                  you is to play the game                 -")
    print("-                      and to have fun                     -")
    print("------------------------------------------------------------")
    title_screen_selections()
def setup_game():
    os.system('clear')
    print_slow('------------------------------------------------------------')
    print_slow('-                     Well hello there.                    -')
    print_slow('-                    What is your name?                    -')
    print_slow('------------------------------------------------------------')
    myplayer.name = raw_input("> ")
    myplayer.hp = 100
    myplayer.mp = 100
    print_slow('-'*60)
    print_slow('-            Great name, now choose your class?            -')
    print('-                        '),
    print colored('-Knight-', 'cyan'),
    print_slow('                         -')
    print('-                         '),
    print colored('-Mage-', 'magenta'),
    print_slow('                          -')
    print_slow('-'*60)
    classType = raw_input("> ")
    if classType.lower() == ('knight'):
        myplayer.type = 'knight'
        game_starts()
    elif classType.lower() == ('mage'):
        myplayer.type = 'mage'
        game_starts()
    while classType.lower() not in ['knight', 'mage']:
        print('Not a class, select one.')
        classType = raw_input("> ")
        if classType.lower() == ('knight'):
            myplayer.type = 'knight'
            game_starts()
        elif classType.lower() == ('mage'):
            myplayer.type = 'mage'
            game_starts()
def game_starts():
    os.system('clear')
    main_game_loop()
###HELPER FUNCTIONS###
def print_game_status():
    #os.system('clear')
    print('-'),
    print colored('HP%d ' % myplayer.hp, 'red'),
    sys.stdout.write('-')
    sys.stdout.flush()
    print colored('LOCATION', 'green', attrs=['underline']),
    print_slow('-'*43)
    print('-'),
    print colored('MP%d' % myplayer.mp, 'cyan'),
    print('---'),
    print colored(myplayer.location.upper(), 'green'),
    print_slow(' ' + '-'*45)
    print('-'+' '*21),
    print colored('Where are you?', attrs=['underline','bold']),
    print(' '*21 + '-')
    print_slow(zonemap[myplayer.location][DESCRIPTION])
def print_slow(str):
    for letter in str +'\n':
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)
def movementHandler(destanation):
    print('You moved to ' + destanation + '.')
    time.sleep(0.5)
    myplayer.location = destanation
def print_location():
    print(('#' * (4 + len(myplayer.location))))
    print("# " + myplayer.location.upper() + ' #')
    print(('#' * (4 + len(myplayer.location))))
###GAME INTERACTIRTY###
def prompt():
    print_game_status()
    print_slow('------------------------------------------------------------')
    print('-                     '),
    print colored('What do you do?', attrs=['underline', 'bold'] ),
    print_slow('                     -')
    sys.stdout.write('-  [1]')
    sys.stdout.flush()
    print colored('Walk', 'yellow'),
    print_slow('                                                 -')
    sys.stdout.write('-  [2]')
    sys.stdout.flush()
    print colored('Search', 'yellow'),
    print_slow('                                               -')
    sys.stdout.write('-  [3]')
    sys.stdout.flush()
    print colored('Inventory', 'yellow'),
    print_slow('                                            -')
    sys.stdout.write('-  [4]')
    sys.stdout.flush()
    print colored('Quit', 'yellow'),
    print_slow('                                                 -')
    print_slow('------------------------------------------------------------')
    action = raw_input('> ')
    acceptable_actions = ['walk', 'search', 'inventory', 'quit']
    if action.lower() == 'walk':
        player_move(action.lower())
    elif action.lower() == 'search':
        print(zonemap[myplayer.location][EXAMINE])
        if zonemap[myplayer.location][ITEMNUMBER] != 'itemnumber':
            time.sleep(0.5)
            items[zonemap[myplayer.location][ITEMNUMBER]] = True
        else:
            return
    elif action.lower() == 'inventory':
        inventory()
    elif action.lower() == 'quit':
        sys.exit()
    while action.lower() not in acceptable_actions:
        print('Unknow action, try again.\n')
        action = raw_input('> ')
        if action.lower() == 'walk':
            player_move(action.lower())
        elif action.lower() == 'search':
            print(zonemap[myplayer.location][EXAMINE])
        elif action.lower() == 'inventory':
            inventory()
        elif action.lower() == 'quit':
            sys.exit()
def player_move(myAction):
    ask = 'Where do you move? Up, Down, Right, left.\n> '
    dest = raw_input(ask)
    if dest.lower() == 'up':
        movingTo = zonemap[myplayer.location][UP]
        if movingTo != '':
            if myplayer.location == 'e4':
                if items['item1'] == True:
                    movementHandler(movingTo)
                else:
                    print('You do not have the key for this door.')
            else:
                movementHandler(movingTo)
        else:
            print('cant move that way')
    elif dest.lower() == 'down':
        movingTo = zonemap[myplayer.location][DOWN]
        if movingTo != '':
            if myplayer.location == 'e2':
                if items['item1'] == True:
                    movementHandler(moveingTo)
                else:
                    print('You dont have the key for this door.')
            movementHandler(movingTo)
        else:
            print('cant move that way')
    elif dest.lower() == 'left':
        movingTo = zonemap[myplayer.location][LEFT]
        if movingTo != '':
            if myplayer.location == 'd3':
                if items['item1'] == True:
                    movementHandler(movingTo)
                else:
                    print('You dont have the key for this door.')
            movementHandler(movingTo)
        else:
            print('cant move that way')
    elif dest.lower() == 'right':
        movingTo = zonemap[myplayer.location][RIGHT]
        if movingTo != '':
            movementHandler(movingTo)
        else:
            print('cant move that way')
    else:
        print('invald command, try using up down left righrt.')
        player_move(myAction)
def inventory():
    count = 0
    count2 = 0
    inventory_descriptions = {

    }
    for item_number in items:
        if items[item_number] == True:
            count += 1
            item1 = player_inventory[item_number][ITEMNAME]
            inventory_descriptions['item'+str(count)] = player_inventory[item_number][ITEMDESCRIPTION]
            print('['+str(count)+']'+item1)
    if count != 0:
        print('Choose an item by its number to learn about it.')
        chosen_item = raw_input('> ')
        posible_items = [count]
        for each_item in range(count):
            count2+= 1
            if chosen_item == str(count2):
                print(inventory_descriptions['item'+chosen_item])
                time.sleep(0.5)
###map###
# a b c d e f g h
#| | | | | | | | |1
#| | | | | | | | |2
#| | | | | | | | |3
#| | | | | | | | |4

solved_places = { 'a1': False, 'a2': False, 'a3': False, 'a4': False, 'b1': False,
 'b2': False, 'b3': False, 'b4': False, 'c1': False, 'c2': False, 'c3': False,
 'c4': False, 'd1': False, 'd2': False, 'd3': False, 'd4': False, 'f1': False, 'f2': False, 'f3': False, 'f4':
 False, 'g1': False, 'g2': False, 'g3': False, 'g4': False, 'h1': False, 'h2': False, 'h3': False, 'h4': False,
}

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINE = 'examine'
SOLVED = False
ENEMYPRESENT = False
ITEMNUMBER = 'itemnumber'
UP = 'up',
DOWN = 'down',
LEFT = 'left',
RIGHT = 'right',

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: 'fd',
        EXAMINE: 'afds',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'a2',
        LEFT: '',
        RIGHT: 'b1',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'adf',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'c1',
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'ffd',
        EXAMINE: 'adfda',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'd1',
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: 'af',
        EXAMINE: 'dfa',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'e1',
    },
    'e1': {
        ZONENAME: "",
        DESCRIPTION: 'afd',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: 'f1',
    },
    'f1': {
        ZONENAME: "",
        DESCRIPTION: 'adf',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'f2',
        LEFT: 'e1',
        RIGHT: 'g1',
    },
    'g1': {
        ZONENAME: "",
        DESCRIPTION: 'adf',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'g2',
        LEFT: 'f1',
        RIGHT: 'h1',
    },
    'h1': {
        ZONENAME: "",
        DESCRIPTION: 'adsf',
        EXAMINE: 'adsf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: '',
        DOWN: 'h2',
        LEFT: 'g1',
        RIGHT: '',
    },
    'a2': {
        ZONENAME: "",
        DESCRIPTION: 'fd',
        EXAMINE: 'dasf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'a1',
        DOWN: 'a3',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "",
        DESCRIPTION: 'afds',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'b1',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'dfs',
        EXAMINE: 'dfafds',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'c1',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'dfs',
        EXAMINE: 'fds',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'd1',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'e2',
    },
    'e2': {
        ZONENAME: "",
        DESCRIPTION: 'dfa',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'e1',
        DOWN: 'e3',
        LEFT: 'd2',
        RIGHT: 'f2',
    },
    'f2': {
        ZONENAME: "",
        DESCRIPTION: 'fads',
        EXAMINE: 'afdf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'f1',
        DOWN: 'f3',
        LEFT: 'e2',
        RIGHT: 'g2',
    },
    'g2': {
        ZONENAME: "",
        DESCRIPTION: 'afd',
        EXAMINE: 'afd',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'g1',
        DOWN: 'g3',
        LEFT: 'f2',
        RIGHT: 'h2',
    },
    'h2': {
        ZONENAME: "",
        DESCRIPTION: 'fasd',
        EXAMINE: 'asf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'h1',
        DOWN: 'h3',
        LEFT: 'g2',
        RIGHT: '',
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION: 'afd',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'a2',
        DOWN: 'a4',
        LEFT: '',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'afsd',
        EXAMINE: 'fasf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'b2',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'afsd',
        EXAMINE: 'adfas',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'c2',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'fadf',
        EXAMINE: 'adfa',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'd2',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'e3',
    },
    'e3': {
        ZONENAME: "",
        DESCRIPTION: 'afda',
        EXAMINE: 'afsa',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'e2',
        DOWN: 'e4',
        LEFT: 'd3',
        RIGHT: 'f3',
    },
    'f3': {
        ZONENAME: "",
        DESCRIPTION: 'afdsa',
        EXAMINE: 'fadsf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'f2',
        DOWN: 'f4',
        LEFT: 'e3',
        RIGHT: 'g3',
    },
    'g3': {
        ZONENAME: "",
        DESCRIPTION: 'afasf',
        EXAMINE: 'afdsaf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'g2',
        DOWN: 'g4',
        LEFT: 'f3',
        RIGHT: 'h3',
    },
    'h3': {
        ZONENAME: "",
        DESCRIPTION: 'afsdf',
        EXAMINE: 'adf',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'h2',
        DOWN: 'h4',
        LEFT: 'g3',
        RIGHT: '',
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION: 'afda',
        EXAMINE: 'afda',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'a3',
        DOWN: '',
        LEFT: '',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'fdsf',
        EXAMINE: 'afds',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'b3',
        DOWN: '',
        LEFT: 'a4',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'adfsa',
        EXAMINE: 'adfas',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'c3',
        DOWN: '',
        LEFT: 'b4',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "libary",
        DESCRIPTION: "you are in a room with a large round wood table in the center of the room, there are book shelf's on all the walls. There is also a skeleton in the corner with an iron sword in his hand",
        EXAMINE: "you find a spell book in one of the shelf's",
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'item2',
        UP: 'd3',
        DOWN: '',
        LEFT: 'c4',
        RIGHT: 'e4',
    },
    'e4': {
        ZONENAME: "start",
        DESCRIPTION: "you are at the entrance to the castle with a door in front to the left and to the right of you",
        EXAMINE: "you see the door in front is locked",
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: "e3",
        DOWN: "",
        LEFT: "d4",
        RIGHT: "f4",
    },
    'f4': {
        ZONENAME: "wineceller",
        DESCRIPTION: "you are in a wood room with wine bottles stored in the walls. There is a large red stain in the carpet leading out of the room.",
        EXAMINE: "dsaf",
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'f3',
        DOWN: '',
        LEFT: 'e4',
        RIGHT: 'g4',
    },
    'g4': {
        ZONENAME: "",
        DESCRIPTION: 'dsfa',
        EXAMINE: 'adfa',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'g3',
        DOWN: '',
        LEFT: 'f4',
        RIGHT: 'h4',
    },
    'h4': {
        ZONENAME: "",
        DESCRIPTION: 'dasff',
        EXAMINE: 'adfsa',
        SOLVED: False,
        ENEMYPRESENT: False,
        ITEMNUMBER: 'itemnumber',
        UP: 'h3',
        DOWN: '',
        LEFT: 'g4',
        RIGHT: '',
    },


}

ITEMNAME = ''
ITEMDESCRIPTION = 'description'
PLAYERHAS = False
ISKEY = False
ISWEAPON = False
ISSPELL = False

items = { 'item1': False, 'item2': False, 'item3': False, 'item4': False
}

player_inventory = {
    'item1':{
        ITEMNAME: 'KEY',
        ITEMDESCRIPTION: 'Key to e4 door.',
        PLAYERHAS: True,
        ISKEY: True,
        ISWEAPON: False,
        ISSPELL: False,
    },
    'item2':{
        ITEMNAME: 'Flamethrower Spell book',
        ITEMDESCRIPTION: 'Spell book found in D4. Grants player flamethrower spell.',
        PLAYERHAS: False,
        ISKEY: False,
        ISWEAPON: False,
        ISSPELL: True,
    },
    'item3':{
        ITEMNAME: 'Iron sword',
        ITEMDESCRIPTION: 'An Iron sword. The classic weapon of all knights.',
        PLAYERHAS: False,
        ISKEY: False,
        ISWEAPON: True,
        ISSPELL: False,
    },
    'item4':{
        ITEMNAME: 'Spark spell book',
        ITEMDESCRIPTION: 'Spell book of the mage class. Grants player spark spell.',
        PLAYERHAS: False,
        ISKEY: False,
        ISWEAPON: False,
        ISSPELL: True,
    }
}
###program starts###
def main_game_loop():
    while myplayer.gameOver is False:
        prompt()

title_screen()
