import enum


def has_33(arr):
    
    for idx, num in enumerate(arr):
        if num == 3 and idx+1 != len(arr) and arr[idx+1] == 3:
            return True
    return False




print(has_33([1, 2, 3]))