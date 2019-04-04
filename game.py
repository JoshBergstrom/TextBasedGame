
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 300

###Player Setup###
class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
myplayer = player()

###Title Screens###
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_screen()
    elif option.lower() == ("back"):
        title_screen()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("invalded command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_screen()
        elif option.lower() == ("back"):
            title_screen()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('cls')
    print("#######################################")
    print("#               Welcome               #")
    print("#######################################")
    print("#                -Play-               #")
    print("#                -Help-               #")
    print("#                -Quit-               #")
    print("#######################################")
    title_screen_selections()

def help_screen():
    os.system('cls')
    print("#Back##################################")
    print("#       The best help I can give      #")
    print("#       you is to play the game       #")
    print("#           and to have fun           #")
    print("#######################################")
    title_screen_selections()

###program starts###
title_screen()


###map###
# a b c d e f g h
#| | | | | | | | |1
#| | | | | | | | |2
#| | | | | | | | |3
#| | | | | | | | |4

ZONENAME: ''
DESCRIPTION = ''
EXAMINE = ''
SOLVED = False
UP = 'as'
DOWN = 'asd'
LEFT = 'as'
RIGHT = 'as'


solved_places = {

}


zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: 'fd',
        EXAMINE: 'afds',
        SOLVED: False,
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
        UP: 'e3',
        DOWN: '',
        LEFT: 'd4',
        RIGHT: 'f4',
    },-
    'f4': {
        ZONENAME: "wineceller",
        DESCRIPTION: "you are in a wood room with wine bottles stored in the walls. There is a large red stain in the carpet leading out of the room.",
        EXAMINE: "dsaf",
        SOLVED: False,
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
        UP: 'h3',
        DOWN: '',
        LEFT: 'g4',
        RIGHT: '',
    },


}







