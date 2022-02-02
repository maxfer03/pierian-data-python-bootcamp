def palindrome(s):
    s = s.lower().replace(' ', "")
    middle = int(len(s)/2)

    if len(s)%2 == 0:
        halves = [s[0:middle], s[middle:]]
    else:
        halves = [s[0:middle+1], s[middle:]]

    return halves[0] == halves[1][::-1]


print(palindrome('madam'))