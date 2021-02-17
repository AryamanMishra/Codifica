import requests    # Necessary Headers
import json

URL = 'https://codeforces.com/api/user.status?handle=' # Status API

user_name = input()  # Taking Username input

URL += user_name

input_problem = input()  # The input problem

problems_solved = []   # List of solved problems containg a string concatenated by contest ID and Question Key

link = requests.get(URL)  # API request

Bool = False

parsed = json.loads(link.text)  

json.dumps(parsed, indent=4) # Parsing API


if parsed['status'] == 'OK':      # Fetching all the solved problems
    for i in range(len(parsed['result'])):
        if (str(parsed['result'][i]['verdict']) == 'OK'):
            problems_solved.append(str(parsed['result'][i]['problem']['contestId']) + str(parsed['result'][i]['problem']['index']))

    for problem in problems_solved:
        if (problem == input_problem):   # Checking if input problem is solved by the user
            print("Bravo!! you have solved this problem")
            Bool = True
            break
        
    if Bool == False:
        print("You have not solved this problem so you cannot write editorial for it")
else:
    print("Invalid username")

