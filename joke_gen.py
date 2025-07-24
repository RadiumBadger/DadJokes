# Step 1: grab the website with dad jokes that is an API
import requests
import time
import math
# Step 2: create a variable that is a dictionary
# but now, why is this dictionary this way? This is
# because it is standardised by the elders of the internet
# as a way for clients to talk to servers.
# Here, accept the requested format which is plain text
# For more information, check the following links
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers#content_negotiation
# https://www.iana.org/assignments/media-types/media-types.xhtml#text
header = {'Accept': 'application/json'}
res = requests.get(url='https://icanhazdadjoke.com/search', headers=header)
# print(res.json()['results'])
# print(res.json()['results'][0]['joke'])
number_of_jokes = 700
number_of_jokes_per_page = res.json()['limit']
amnt_pages_to_fetch = number_of_jokes/number_of_jokes_per_page
the_file = open('dad_jokes.csv', 'w', encoding='utf-8')

for i in range(math.ceil(amnt_pages_to_fetch)): # math.ceil is rounding up
    # the number of (in this instant pages)
    current_page = requests.get(url='https://icanhazdadjoke.com/search?page=' + str(i), headers=header)

    for joke_number in range(number_of_jokes_per_page):
        the_file.write(current_page.json()['results'][joke_number]['joke'])
        the_file.write('\n')
        print(current_page.json()['results'][joke_number]['joke'])

the_file.close()

# Step 3: Now we are going to request to get the
# data from the required URL (website)

# for i in range(365):
#     res = requests.get(url='https://icanhazdadjoke.com/', headers=header)
#     if res.status_code == 200:
#         print(res.text)
#     else:
#         print('Taking a piss for 60 seconds...')
#         time.sleep(60)



