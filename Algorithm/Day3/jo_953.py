foul_list = input().split(' ')
dict = {}
for i in foul_list:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1
least_foul = 100000
least_list = []
for i in dict.keys():
    if dict[i] < least_foul:
        least_list = [i]
        least_foul = dict[i]
    elif dict[i] == least_foul:
        least_list.append(i)
    else:
        continue
for i in least_list:
    print(i)
print(least_foul)