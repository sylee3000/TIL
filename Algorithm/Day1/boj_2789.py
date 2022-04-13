word=input()
ban="CAMBRIDGE"
for i in ban:
    while word.find(i)>=0:
        pos=word.find(i)
        word=word[:pos]+word[pos+1:]
print(word)