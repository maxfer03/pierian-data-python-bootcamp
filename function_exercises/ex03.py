def almost_there(x):
    minus_100 = x - 100
    minus_200 = x - 200

    return -10 <= minus_100 <= 10 or -10 <= minus_200 <= 10

print(almost_there(194))