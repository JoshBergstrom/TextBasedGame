
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#########player setup##########
class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp =0
myplayer = player()


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in [play , quit]:
        print("invalded command")
    option = imput(">")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("quit"):
        sys.exit()

## title screen ##
def title_screen():
    os.system('clear')
    print("#################")
    print("#####welcome#####")
    print("##are you ready##")
    print("     -Play-      ")
    print("     -Quit-      ")
    print("#################")
    title_screen_selections()



title_screen()

