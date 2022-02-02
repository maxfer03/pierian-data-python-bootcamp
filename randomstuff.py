st = 'Print only the words that start with s in this sentence'
st = st.split(' ')

for word in st:
    if word[0] == 's':
        print(word)
