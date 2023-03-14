import csv
import os
import sys

def command_line_validation():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Not enought command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith("csv") or not sys.argv[1].endswith("csv"):
        print("Files are not a CSV file")
        sys.exit(1)
    elif os.path.isfile(sys.argv[1]) == False:
        print("File does not exist")
        sys.exit(1)

def read_file():                                #Function reads data as "Name and Surname" and "House" each row
    sec_and_fir_name = []                       #and after that it appends them to correct array.
    houses = []

    with open(sys.argv[1]) as before_file:
        reader = csv.DictReader(before_file)
        for row in reader:
            sec_and_fir_name.append({"name": row["name"]})
            houses.append(row["house"])
        surnames, names = name_split(sec_and_fir_name)
        create_new_file(surnames, names, houses)

def create_new_file(surnames, names, houses):   #function creates new SCV file adding data (name, surname nad house) in correct order in each row

    with open(sys.argv[2], "w") as after:
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for i in range(len(surnames)):
            writer.writerow({"first": names[i], "last": surnames[i], "house": houses[i]})

def name_split(sec_and_fir_name):       #function splits readed names and surnames in correct arrays, used later in
    surname = []                        #function create_new_file
    name = []
    for row in sec_and_fir_name:
        full_name = row["name"]
        surname.append(full_name.split(", ")[0])
        name.append(full_name.split(", ")[1])
    return surname, name


if __name__ == "__main__":
    command_line_validation()
    read_file()
