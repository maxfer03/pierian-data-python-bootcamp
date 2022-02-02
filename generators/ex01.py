def gensquares(n):
    for x in range(n):
        yield x**2



for x in gensquares(10):
    print(x)


