paper_count = int(input())
total_area = [[0] * 100 for j in range(100)]
count = 0
for i in range(paper_count):
    paper_x, paper_y = map(int,input().split(" "))
    for j in range(paper_x, paper_x + 10):
        for k in range(paper_y, paper_y + 10):
            total_area[j][k] = 1
for i in range(100):
    for j in range(100):
        if total_area[i][j] == 1:
            count += 1
print(count)
