block_pos = list(map(int, input().split(" ")))
correct_pos = [1, 2, 3, 4, 5]
while block_pos != correct_pos:
    for i in range(4):
        if block_pos[i] > block_pos[i+1]:
            block_pos[i], block_pos[i+1] = block_pos[i+1], block_pos[i]
            for i in range(5):
                print(block_pos[i], end=' ')
            print("")
