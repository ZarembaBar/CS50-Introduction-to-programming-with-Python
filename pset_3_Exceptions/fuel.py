while True:
    tank = input("Fraction: ")
    try:
        fractions = tank.split("/")
        level = round(int(fractions[0]) / int(fractions[1]), 2)
        if level <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

fuel_level = int(level * 100)

if fuel_level >= 99:
    print("F")
elif fuel_level <= 1:
    print("E")
else:
    print(f"{fuel_level}%")
