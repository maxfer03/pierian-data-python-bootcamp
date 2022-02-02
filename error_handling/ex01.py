for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("Cant operate on a string/character!")