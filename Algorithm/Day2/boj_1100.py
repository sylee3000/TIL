count = 0
for i in range(8):
    line_status = input()
    for j in range(8):
        if line_status[j]=='F' and (i + j) % 2 == 0:
            count += 1
print(count)
