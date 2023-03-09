import random


def main():
    list_x = []
    list_y = []

    generate_integer(get_level(), list_x, list_y)

    track = 0
    score = 0

    while track < 10:
        for i in range(3):
            result = list_x[track] + list_y[track]
            answer = int(input(f"{list_x[track]}" + " + " + f"{list_y[track]}" + " = "))
            if answer != result:
                print("EEE")
                i += 1
                if i == 3:
                    print(
                        f"{list_x[track]}"
                        + " + "
                        + f"{list_y[track]}"
                        + " = "
                        + f"{result}"
                    )
                    break
            elif answer == result:
                score += 1
                break
        track += 1
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                break
        except:
            continue
    return level


def generate_integer(level, list_x, list_y):
    if level == 1:
        range_level_start = 0
        range_level_end = 9
    elif level == 2:
        range_level_start = 10
        range_level_end = 99
    elif level == 3:
        range_level_start = 100
        range_level_end = 999

    for i in range(10):
        X = random.randint(range_level_start, range_level_end)
        list_x.append(X)
        Y = random.randint(range_level_start, range_level_end)
        list_y.append(Y)
    return list_x, list_y


if __name__ == "__main__":
    main()
