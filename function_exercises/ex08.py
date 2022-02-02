def myfunc(string):
    char_arr = [x for x in string]
    for i, char in enumerate(char_arr):
        if (i+1) % 2 == 0:
            char_arr[i] = char.upper()
        else:
            char_arr[i] = char.lower()
    return ''.join(char_arr)


print(myfunc('Supercalifragilisticoespialidoso'))