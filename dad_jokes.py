from datetime import datetime  # always put the imports at the top of the code
from calendar import monthrange
import csv
import random


def read_dad_joke_tsv_file():
    with open('dad_jokes.tsv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        our_tsv_data = list(reader)
    return our_tsv_data

def tell_me_a_dad_joke():
    dad_jokes = read_dad_joke_tsv_file()

    today_as_day_of_year = datetime.now().timetuple().tm_yday
    return dad_jokes[today_as_day_of_year][1]

def tell_me_a_random_dad_joke():
    read_dad_joke = read_dad_joke_tsv_file()
    return random.choice(read_dad_joke)[1]

print("====================\n"
      "DAD JOKE OF THE DAY!\n"
      "====================")
joke = tell_me_a_dad_joke()
print("*" * len(joke))
print(joke)
print("*" * len(joke))

print()
print("========================================================\n"
      "LUCKY YOU! HERE'S ANOTHER RANDOM DAD JOKE, JUST FOR YOU!\n"
      "========================================================")
random_joke = tell_me_a_random_dad_joke()
print("*" * len(random_joke))
print(random_joke)
print("*" * len(random_joke))

    # today = datetime.now()
    # month = monthrange(today.year, int(today.strftime('%m')))
    #
    # for i in range(month[1]):
    #     if i == today.day:
    #         print(dad_jokes[i])



