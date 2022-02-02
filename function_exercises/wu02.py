def animal_crackers(str):
    str_arr = str.upper().split(' ')
    if len(str_arr) != 2:
        return 'string must have 2 words only'
    
    return str_arr[0][0] == str_arr [1][0]


print(animal_crackers('World word'))