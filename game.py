
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
===
 a b c d e f g h
| | | | | | | | |1
| | | | | | | | |2
| | | | | | | | |3
| | | | | | | | |4
===

ZONENAME = ''
DESCRIPTION = ''
EXAMINE = ''
CHESTSOLVED = ''
UP = ''
DOWN = ''
LEFT = ''
RIGHT = ''


infomap = {
    'a1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = 'a2'
        LEFT = ''
        RIGHT = 'b1'
    }
    'b1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = 'b2'
        LEFT = 'a1'
        RIGHT = 'c1'
    }
    'c1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = 'c2'
        LEFT = 'b1'
        RIGHT = 'd1'
    }
    'd1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = 'd2'
        LEFT = 'c1'
        RIGHT = 'e1'
    }
    'e1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'f1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'g1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'h1': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'a2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'b2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'c2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'd2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'e2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'f2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'g2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'h2': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'a3': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'b3': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'c3': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'd3': {
    ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'e3': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'f3': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'g3': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'h3': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'a4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'b4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'c4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'd4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'e4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'f4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'g4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
    'h4': {
        ZONENAME = ''
        DESCRIPTION = ''
        EXAMINE = ''
        CHESTSOLVED = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
    }
}







