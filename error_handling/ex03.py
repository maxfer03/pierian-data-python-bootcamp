

def ask():
    while True:
        num = input('Get the square root of: ')
        try:
            num = int(num)
            print(num**(1/2))
            return num**(1/2)
        except ValueError:
            print("Only numbers allowed!")
    
    


ask()