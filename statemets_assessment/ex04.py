st = 'Print every word in this sentence that has an even number of letters'
st = st.split(' ')

isEven = [x for x in st if len(x) % 2 == 0]

print(isEven)