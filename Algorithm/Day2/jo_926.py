first_array=[]
second_array=[]
for i in range(2):
    lst=list(map(int,input().split(' ')))
    first_array.append(lst)
for i in range(2):
    lst=list(map(int,input().split(' ')))
    second_array.append(lst)
new_list = []
for i in range(2):
    lst = []
    for j in range(4):
        lst.append(first_array[i][j]*second_array[i][j])
    new_list.append(lst)
for i in range(2):
    for j in range(4):
        print(new_list[i][j], end=' ')
    print("")