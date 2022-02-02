def old_macdonald(str):
    arr = [x for x in str]

    
    arr[0] = arr[0].upper()
    arr[3] = arr[3].upper()  
    return ''.join(arr)

print(old_macdonald('macdonald'))