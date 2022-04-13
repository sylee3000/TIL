A,B=input().split()
save=False
for i in A:
    for j in B:
        if i==j:
            index_A=A.index(i)
            index_B=B.index(j)
            save=True
            break
    if save:
        break
crossword=[]
for i in range(len(B)):
    line=[]
    for j in range(len(A)):
        line.append('.')
    crossword.append(line)

for i in range(len(A)):
    crossword[index_B][i]=A[i]
for i in range(len(B)):
    crossword[i][index_A]=B[i]

for i in range(len(B)):
    for j in range(len(A)):
        print(crossword[i][j],end='')
    print('')