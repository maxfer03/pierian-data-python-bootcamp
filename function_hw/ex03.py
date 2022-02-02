def up_low(str):
    lows= 0
    highs= 0

    for char in str:
        if char.isupper():
            highs+=1
        elif char.islower():
            lows+=1
    return f'upper: {highs}, lower: {lows}'



string = 'Hello Mr. Rogers, how are you this fine Tuesday?'

print(up_low(string))