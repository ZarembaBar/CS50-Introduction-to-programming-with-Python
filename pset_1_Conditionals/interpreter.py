def main():
    expression = input("Expression: ").strip()

    x = expression.split()[0]
    y = expression.split()[1]
    z = expression.split()[2]

    if y == "+":
        print(float(x) + float(z))

    elif y == "-":
        print(float(x) - float(z))

    elif y == "*":
        print(float(x) * float(z))

    elif y == "/":
        print(float(x) / float(z))


if __name__ == "__main__":
    main()
