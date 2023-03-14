import sys

def command_line_validation():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif ".py" not in sys.argv[1]:
        print("Not a Python file")
        sys.exit(1)

def lines_count():
    line_count = 0
    try:
        file = open(sys.argv[1], "r")
        for line in file:
            if line.isspace():
                pass
            elif line.lstrip().startswith("#"):
                pass
            else:
                line_count += 1
        print(line_count)
    except:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":

    command_line_validation()
    lines_count()