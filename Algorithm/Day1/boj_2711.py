T=int(input())
for i in range(T):
    pos,word=input().split()
    mod_word=word[:int(pos)-1]+word[int(pos):]
    print(mod_word)