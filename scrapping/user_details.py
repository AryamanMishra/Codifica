import requests
import json
import matplotlib.pyplot as plt 

URL = 'https://codeforces.com/api/user.status?handle='

Rating = 'https://codeforces.com/api/user.rating?handle='

user_name = input()

URL += user_name

Rating += user_name

problems_solved = []

link = requests.get(URL)

parsed = json.loads(link.text)

rate = requests.get(Rating)

rateparsed = json.loads(rate.text)

json.dumps(parsed, indent=4)

json.dumps(rateparsed, indent=4)


def giverating():
    if rateparsed['status'] == 'FAILED':
        print("Oops!! we could not find that username")
    elif len(rateparsed['result']) == 0:
        print("You are unrated on codeforces")
    else:
        print("Your Codeforces rating is: " + str(rateparsed['result'][len(rateparsed['result']) - 1]['newRating']))
        

def latestproblem():
    if parsed['status'] == 'OK':
        if (len(parsed['result']) != 0):
            print("Hmmm it seems like the latest problem you solved was " + str(parsed['result'][0]['problem']['name']) )
        else:
            print("Looks like you have not solved a problem recently")
    else:
        print("Oops!! we could not find that username")

def no_of_submissions():
    if parsed['status'] == 'OK':
        if (len(parsed['result']) == 1): 
            print("You have given " + str(len(parsed['result']))  + " submission on Codeforces")
        else:
            print("You have given " + str(len(parsed['result']))  + " submissions on Codeforces")
    else:
        print("Oops!! we could not find that username")

def tags():
    if parsed['status'] == 'OK':
        greedy = 0
        math = 0
        implementation = 0
        dp = 0
        data_structures = 0
        brute_force = 0
        constructive_algorithms = 0
        graphs = 0
        sortings = 0
        binary_search = 0
        dfs_and_similar = 0
        trees = 0
        strings = 0
        number_theory = 0
        combinatorics = 0
        geometry = 0
        bitmasks = 0
        two_pointers = 0
        dsu = 0
        shortest_paths = 0
        probabilities = 0
        divide_and_conquer = 0
        hashing = 0
        games = 0
        flows = 0
        interactive = 0
        matrices = 0
        string_suffix_structures = 0 
        fft = 0
        graph_matchings = 0
        ternary_search = 0
        expression_parsing = 0 
        meet_in_the_middle = 0
        _2_sat = 0
        chinese_remainder_theorem = 0
        schedules = 0

        for res in parsed['result']:
            lis = res['problem']['tags']
            for l in lis:
                if l == 'greedy':
                    greedy += 1
                elif l == 'math':
                    math += 1
                elif l == 'implementation':
                    implementation += 1
                elif l == 'dp':
                    dp += 1
                elif l == 'data structures':
                    data_structures += 1
                elif l == 'brute force':
                    brute_force += 1
                elif l == 'constructive algorithms':
                    constructive_algorithms += 1
                elif l == 'graphs':
                    graphs += 1
                elif l == 'sortings':
                    sortings += 1
                elif l == 'binary search':
                    binary_search += 1
                # elif l == 'dfs and similar':
                #     dfs_and_similar += 1
                # elif l == 'trees':
                #     trees += 1
                # elif l == 'strings':
                #     strings += 1
                # elif l == 'number theory':
                #     number_theory += 1
                # elif l == 'combinatorics':
                #     combinatorics += 1
                # elif l == 'geometry':
                #     geometry += 1
                # elif l == 'bitmasks':
                #     bitmasks += 1
                # elif l == 'two pointers':
                #     two_pointers += 1
                # elif l == 'dsu':
                #     dsu  += 1
                # elif l == 'shortest paths':
                #     shortest_paths += 1
                # elif l == 'probabilities':
                #     probabilities += 1
                # elif l == 'divide and conquer':
                #     divide_and_conquer += 1
                # elif l == 'hashing':
                #     hashing += 1
                # elif l == 'games':
                #     games += 1
                # elif l == 'flows':
                #     flows += 1
                # elif l == 'interactive':
                #     interactive += 1
                # elif l == 'matrices':
                #     matrices += 1
                # elif l == 'string suffix structures':
                #     string_suffix_structures += 1
                # elif l == 'fft':
                #     fft += 1
                # elif l == 'graph matchings':
                #     graph_matchings += 1
                # elif l == 'ternary search ':
                #     ternary_search  += 1
                # elif l == 'expression parsing':
                #     expression_parsing += 1
                # elif l == 'meet-in-the-middle':
                #     meet_in_the_middle += 1
                # elif l == '2-sat':
                #     _2_sat  += 1
                # elif l == 'chinese remainder theorem':
                #     chinese_remainder_theorem += 1
                # elif l == 'schedules':
                #     schedules  += 1
        left = []   
        for i in range(1,11):
            left.append(i)
        height = [greedy, 
        math,
        implementation,
        dp,
        data_structures,
        brute_force,
        constructive_algorithms,
        graphs,
        sortings,
        binary_search
        # dfs_and_similar,
        # trees,
        # strings,
        # number_theory,
        # combinatorics,
        # geometry,
        # bitmasks,
        # two_pointers,
        # dsu,
        # shortest_paths,
        # probabilities,
        # divide_and_conquer,
        # hashing,
        # games,
        # flows,
        # interactive,
        # matrices,
        # string_suffix_structures, 
        # fft,
        # graph_matchings,
        # ternary_search,
        # expression_parsing,
        # meet_in_the_middle,
        # _2_sat,
        # chinese_remainder_theorem,
        # schedules
        ]
        tag_label = ['greedy',
        'math',
        'implementation',
        'dp',
        'data structures',
        'brute force',
        'constr algorithms',
        'graphs',
        'sortings',
        'binary search',
        # 'dfs and similar', 
        # 'trees',
        # 'strings',
        # 'number theory'
        # 'combinatorics',
        # 'geometry',
        # 'bitmasks',
        # 'two pointers',
        # 'dsu',
        # 'shortest paths',
        # 'probabilities',
        # 'divide and conquer',
        # 'hashing',
        # 'games',
        # 'flows',
        # 'interactive',
        # 'matrices',
        # 'string suffix structures', 
        # 'fft', 
        # 'graph matchings',
        # 'ternary search',
        # 'expression parsing',
        # 'meet-in-the-middle',
        # '2-sat',
        # 'chinese remainder theorem',
        # 'schedules'
        ]
        plt.bar(left, height, tick_label = tag_label, 
            width = 0.8, color = ['red', 'green'])
        plt.ylabel('Number Of submissions')
        plt.xlabel('Tags')     
        plt.show()       
        
giverating()
latestproblem()
no_of_submissions()
tags()

