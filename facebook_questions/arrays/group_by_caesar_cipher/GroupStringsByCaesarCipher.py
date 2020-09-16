from collections import defaultdict
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Idea
# 1) find the base 'anagram' for each string
# 2) put in dictionary[anagram] = string
# 3) return the values in the dictionary, where value is a list
def group_caesar(los):
    dict = defaultdict(list)

    # i is index base 0
    # str is the value of string in 'los' list of string
    for i, str in enumerate(los):
        # for each char 'c' in 'str', find their index where char 'a' is 0
        # and create a array index
        # Example: str = "dac", then pos = [3, 0, 2]
        #          str = "ebd", then pos = [4, 1, 3]
        pos = [alphabet.index(c) for c in str]

        minPos = min(pos)
        # pos = [3, 0, 2], minPos = 0
        # pos = [4, 1, 3], minPos = 1

        pos = [num - minPos for num in pos]
        # pos = [3, 0, 2], minPos = 0, pos = [3, 0, 2]
        # pos = [4, 1, 3], minPos = 1, pos = [3, 0, 2]

        # there for "dac" and "ebd" have the same anagram
        # and group them together
        dict[tuple(pos)].append(str)
    return dict.values()

print(group_caesar(["dac", "ebd", "abc", "bcd", "acd", "dfg", "ace", "bdf", "random"]))