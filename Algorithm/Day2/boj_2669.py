area = [[0] * 100 for j in range(100)]
count = 0
for i in range(4):
    rect = list(map(int, input().split(' ')))
    for j in range(rect[0], rect[2]):
        for k in range(rect[1], rect[3]):
            area[j][k] = 1
for i in range(100):
    for j in range(100):
        if area[i][j] == 1:
            count += 1
print(count)