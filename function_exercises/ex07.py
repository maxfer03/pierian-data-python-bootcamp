def summer_69(arr):
    total = 0
    stop  = False
    for i, n in enumerate(arr):
        if n == 6:
            stop = True
        elif arr[i-1] == 9:
            stop = False

        if stop:
            pass
        else:
            total+= n


    return total 


print(summer_69([6,1,1,1,9,2,6,1,1,1,9]))