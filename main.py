from week0 import pattern
from week0 import tree
from week1 import infodb
from week1 import fibonacci
from week2 import factorial
from week2 import math
from time import sleep
import sys 
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
menu_list = [
  #  ["Pattern", pattern.ship],
   # ["Tree", tree.treefunc],
   # ["Loopy", None],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Tree", tree.treefunc],
    ["Pattern", pattern.ship],
]

math_sub_menu = [
    ["Movie Dictionary", infodb.tester],
    ["Fibonacci", fibonacci.tester],
    ["Factorial", factorial.tester],
    ["Math Function", math.gcd],
]
banner_words = "Please Select An Option"
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.25)
# Menu banner is typically defined by menu owner

def _banner_(): 
  print(f"\n{border}")
  delay_print(banner_words)
  print(f"\n{border}")
border = "=" * 25
banner = f"\n{_banner_()}\n"
# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    # menu_list = main_menu.copy()
    menu_list.append(["Patterns", submenu])
    menu_list.append(["Math", math_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def math_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, math_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options) 
  # recursion, start menu over again


if __name__ == "__main__":
    menu()