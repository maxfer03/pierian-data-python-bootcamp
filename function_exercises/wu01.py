def lesser(x, y):
    if x%2 == 0 and y%2 == 0:
        if x < y:   return x
        else:       return y
    else:
        if x > y:   return x
        else:       return y


print(lesser(1,10))