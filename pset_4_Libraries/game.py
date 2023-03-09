import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

game_num = random.randint(1, int(level))
while True:
    try:
        guess_num = int(input("Guess: "))
        if guess_num > 0:
            if guess_num < game_num:
                print("Too small!")
            elif guess_num > game_num:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass
