def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Checking lenght of string (between 2 and 6).
    if len(s) < 2 or len(s) > 6:
        return False
        # Checking if first two signs are only letters
    if not s[:2].isalpha():
        return False
        # Checking if there are only letters and digits in string.
    if not s.isalnum():
        return False

    for sign in s:
        if sign == "0":
            return False
        if sign.isdigit():
            break

    digit_flag = False
    for sign in s:
        if sign.isdigit():
            digit_flag = True
            continue
        if sign.isalpha() and digit_flag == True:
            return False
    else:
        return True


if __name__ == "__main__":
    main()
