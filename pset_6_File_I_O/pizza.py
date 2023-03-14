import sys
import csv
from tabulate import tabulate

def command_line_validation():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
    elif len(sys.argv) < 2:
        print("Not enought command-line arguments")
    elif ".csv" not in sys.argv[1]:
        print("Not a SCV file")

def menu_display():
    table = []
    with open(sys.argv[1]) as menu:
        reader = csv.reader(menu)
        for row in reader:
            table.append({"Pizza": row[0], "Small": row[1], "Large": row[2]})

    print(tabulate(table, headers = "firstrow", tablefmt="grid"))


if __name__ == "__main__":

    command_line_validation()
    menu_display()
