dice_count = int(input())
last_number = 0
max_value = 0
dice_pair = [5, 3, 4, 1, 2, 0]
dice_all = []
for i in range(dice_count):
    dice = list(map(int, input().split()))
    dice_all.append(dice)

for i in range(6):
    pos = i
    value = 0
    for j in range(dice_count):
        dice_number_list = [1, 2, 3, 4, 5, 6]
        base_number = dice_all[j][pos]
        last_number = dice_all[j][dice_pair[pos]]
        dice_number_list.remove(base_number)
        dice_number_list.remove(last_number)
        side_number = dice_number_list
        value += max(side_number)
        if j < dice_count - 1:
            pos = dice_all[j + 1].index(last_number)
        else:
            max_value = value if value > max_value else max_value
print(max_value)
