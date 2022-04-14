total_score = []
for i in range(5):
    score = map(int, input().split(" "))
    total_score.append(sum(score))
print(total_score.index(max(total_score))+1, max(total_score))