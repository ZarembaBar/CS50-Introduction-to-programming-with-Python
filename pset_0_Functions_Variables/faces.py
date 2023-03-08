def main():
    text = input("Happy or sad?")
    text = convert(text)

    print(text)


def convert(n):
    n1 = n.replace(":)", "🙂")
    n2 = n1.replace(":(", "🙁")
    return n2


if __name__ == "__main__":
    main()
