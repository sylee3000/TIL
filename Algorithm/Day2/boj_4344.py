C = int(input())
for i in range(C):
    data = list(map(int, input().split(" ")))
    score_data = data[1:]
    average_data = sum(score_data)/data[0]
    above_average = len(list(filter(lambda x: x > average_data, score_data)))
    above_average_rate = above_average/data[0]*100
    print(f'{above_average_rate:.3f}%')
