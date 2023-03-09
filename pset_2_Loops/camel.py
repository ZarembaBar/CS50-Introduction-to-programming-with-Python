def main():
    camelName = input("camelCase: ")

    snake_case = ""

    for letter in range(len(camelName)):
        if camelName[letter].isupper():
            snake_case = snake_case + "_" + camelName[letter].lower()
        else:
            snake_case += camelName[letter]

    print("snake_case: ", snake_case)


if __name__ == "__main__":
    main()
