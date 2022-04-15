N = int(input())
dict = {}
for i in range(N):
    key, value = input().split(' ')
    dict[key] = value

in_data = input()
if in_data in dict.keys():
    print(dict[in_data])
else:
    print("Unknown Country")