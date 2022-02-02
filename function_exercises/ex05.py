from turtle import st


def paper_doll(str):
    formatted = [x*3 for x in str] 
    
    return ''.join(formatted)

print(paper_doll('Mississippi'))