from datetime import datetime  # always put the imports at the top of the code
from calendar import monthrange

def tell_me_a_dad_joke():
    the_file = open('dad_jokes.txt', 'r')
    dad_jokes = the_file.readlines()
    the_file.close()

    today = datetime.today()
    month = monthrange(today.year, int(today.strftime('%m')))

    for i in range(month[1]):
        if i == today.day:
            print(dad_jokes[i])

