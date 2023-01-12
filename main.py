from game import play
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


levels = ['0', '1', '2', '3', '4', '5', '6', '7']

cls()
work = True
print('Welcome to Wściekłe Ptaki!')
while work:
    print("Select level (from 1 to 7)")
    print("Enter 0 to exit")
    level = input()
    if level == '0':
        work = False
    if level not in levels:
        pass
    elif level == '0':
        work = False
    else:
        play(int(level))
    cls()
cls()
