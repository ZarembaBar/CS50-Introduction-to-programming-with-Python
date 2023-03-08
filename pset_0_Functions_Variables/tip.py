def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    return float(d[1:])


def percent_to_float(p: str) -> float:  # 15% - 0,15, 20% - 0,20 itd.
    return float(p[:-1]) / 100


if __name__ == "__main__":
    main()
