from game import play
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


levels = [0, 1, 2, 3, 4]

cls()
work = True
print('Welcome to Wściekłe Ptaki!')
while work:
    print("Select level (from 1 to 2)")
    print("Enter 0 to exit")
    level = int(input())
    if level == 0:
        work = False
    if level not in levels:
        print('Wrong input')
    elif level == 0:
        work = False
    else:
        play(level)
    cls()
cls()
