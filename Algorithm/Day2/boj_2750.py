N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
sorted_list = sorted(list)
for i in range(N):
    print(sorted_list[i])
