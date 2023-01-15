from game import play
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


game_percentage = 0
levels_completed = 0

levels = {
    '1': False,
    '2': False,
    '3': False,
    '4': False,
    '5': False,
    '6': False,
    '7': False
    }

cls()
work = True
print('Welcome to Wściekłe Ptaki!')
while work:
    for level in levels:
        if levels[level]:
            levels_completed += 1
    game_percentage = int(levels_completed * 100 / len(levels))
    print(f"Game completed: {game_percentage}%")
    print("Select level:")
    print("Enter 0 to exit")
    level = input()
    if level == '0':
        work = False
    elif level not in levels:
        pass
    else:
        result = play(int(level))
        if result:
            levels.update({'{level}': True})
    cls()
cls()
