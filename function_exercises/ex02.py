def master_yoda(str):
    reversed_str = str.lower().split(' ')[::-1]
    return ' '.join(reversed_str)



print(master_yoda("I will win today"))