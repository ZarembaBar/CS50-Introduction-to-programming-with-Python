def main():
    phrase = input("Input: ")

    vowels = ["a", "e", "i", "o", "u"]

    output = ""

    for letter in phrase:

        if letter.lower() in vowels:
            letter = ""
        output += letter

    print(f"Output: {output}")


if __name__ == "__main__":
    main()
