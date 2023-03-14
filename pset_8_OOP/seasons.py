from datetime import date
import inflect
import re
import sys

p = inflect.engine()

def main():
    birth_date = input("Your birth date (YYYY-MM-DD): ")
    birth_date_prompt(birth_date)

def birth_date_prompt(birth_date: str) -> int:

    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        days_count = count_days_between_b_date_and_today(birth_date)
        minutes_count = count_minutes_in_days(days_count)
        words = p.number_to_words(minutes_count, andword = "")
        print(f"{words.capitalize()} minutes")
    else:
        sys.exit(1)

def cut_date_on_three_parts(date: str) -> int:
    date_parts = date.split("-")
    years = int(date_parts[0])
    months = int(date_parts[1])
    days = int(date_parts[2])
    return years, months, days

def count_days_between_b_date_and_today(b_date: str) -> int:
    birth_years, birth_months, birth_days = cut_date_on_three_parts(b_date)
    present_years, present_months, present_days = cut_date_on_three_parts(str(date.today()))
    return (date(present_years, present_months, present_days) - date(birth_years, birth_months, birth_days)).days

def count_minutes_in_days(days: int) -> int:
    minutes = days * 1440
    return minutes



if __name__ == "__main__":
    main()
