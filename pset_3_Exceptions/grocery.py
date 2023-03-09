list = {}


def user_list_input():
    while True:
        try:
            item = input("")
            if item in list.keys():
                list[item] += 1
            else:
                list[item] = 1
        except EOFError:
            print("\n")
            for item in sorted(list):
                print(f"{list[item]} {item.upper()}")
            break


user_list_input()
