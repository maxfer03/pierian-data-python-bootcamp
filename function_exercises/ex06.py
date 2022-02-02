def blackjack(x, y, z):
    eleven = x == 11 or y == 11 or z == 11
    sum = x+z+y
    if sum <= 21:
        return sum
    elif sum > 21 and eleven:
        sum-=10
        if sum > 21:
            return 'BUST'
        else:
            return sum
    else: return 'BUST'



print(blackjack(11,11,11))