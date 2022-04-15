total_rain_amount = 0

world_h, world_w = map(int, input().split(' '))
height = list(map(int, input().split(' ')))
rain_amount = [0] * world_h

left_side = height[0]
last_height = height[0]
for i in range(1, world_w):
    if height[i] <= left_side:
        for j in range(height[i], left_side):
            rain_amount[j] += 1
        if height[i] > last_height:
            for k in range(last_height, height[i]):
                total_rain_amount += rain_amount[k]
                rain_amount[k] = 0
    else:
        for j in range(last_height, height[i]):
            total_rain_amount += rain_amount[j]
            rain_amount[j] = 0
        left_side = height[i]
    last_height = height[i]
print(total_rain_amount)