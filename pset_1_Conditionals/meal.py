def main():
    mealTime = input("what time is it?: ").strip()

    timeFloat = convert(mealTime)

    if timeFloat >= 7 and timeFloat <= 8:
        print("breakfast time")

    elif timeFloat >= 12 and timeFloat <= 13:
        print("lunch time")

    elif timeFloat >= 18 and timeFloat <= 19:
        print("dinner time")


def convert(time):
    hours = int(time.split(":")[0])
    minutes = int(time.split(":")[1][0:1])
    hourFormat = time.split()
    # Example with time format
    if "p.m." in hourFormat and hours >= 1 and hours < 12:
        hours = hours + 12
    # Change 12 a.m. on 00:00 hour
    elif "a.m." in hourFormat and hours == 12:
        hours = hours - 12

    minutesPart = minutes / 60

    finalMealTime = hours + minutesPart

    return finalMealTime


if __name__ == "__main__":
    main()
