def main():
    greeting = input("Greeting: ").strip()
    value(greeting)

def value(greeting):
    if greeting[0:5].lower() == "hello":
        print("$0")
    elif greeting.lower()[0] == "h" and greeting.lower()[0:4] != "hello":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
