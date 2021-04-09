from pyrule_compendium.exceptions import *
from click import echo
from colorama import init
from termcolor import colored

init()

def handle(func):
    try:
        func()
    except Exception as err:
        echo(colored(err, "red"))