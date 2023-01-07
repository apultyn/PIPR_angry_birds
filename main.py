from game import play


work = True
while work:
    print("Select level (from 1 to 2)")
    level = int(input())
    if level == 0:
        work = False
    else:
        play(level)
