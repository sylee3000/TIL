N = int(input())
num = int(input())
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
table = [[0] * N for j in range(N)]
value = 1
x = N // 2
y = N // 2
table[x][y] = value
tick = 0
dir_pos = 0
is_full = 0
index_x = -1
index_y = -1
for i in range(1, N + 1):
    while not is_full:
        for j in range(i):
            x_move = direction[dir_pos][0]
            y_move = direction[dir_pos][1]
            value = value + 1
            x = x + x_move
            y = y + y_move
            table[x][y] = value
            if x == 0 and y == 0:
                is_full = 1
                break
        dir_pos = (dir_pos + 1) % 4
        if tick == 1:
            tick = 0
            break
        else:
            tick += 1
for i in range(N):
    for j in range(N):
        print(table[i][j], end = ' ')
        if table[i][j] == num:
            index_x = i + 1
            index_y = j + 1
    print('')
print(index_x, index_y)