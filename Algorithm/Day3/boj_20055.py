from collections import deque
robot_pos = []
N, K = map(int, input().split())
unload_index = N - 1
start_durability = deque(map(int, input().split()))
step = 0
count = 0

while count < K:
    #1
    change_to_load = start_durability.pop()
    start_durability.appendleft(change_to_load)
    for i in range(len(robot_pos)):
        robot_pos[i] += 1
    if robot_pos and robot_pos[0] == unload_index:
        robot_pos.pop(0)
    #2
    for i in range(len(robot_pos)):
        if start_durability[robot_pos[i] + 1] > 0 and (i == 0 or robot_pos[i - 1] != (robot_pos[i] + 1)):
            start_durability[robot_pos[i] + 1] -= 1
            if start_durability[robot_pos[i] + 1] == 0:
                count += 1
            robot_pos[i] += 1
    if robot_pos and robot_pos[0] == unload_index:
        robot_pos.pop(0)
    #3
    if start_durability[0] > 0:
        if len(robot_pos) >= 1 and robot_pos[len(robot_pos) - 1] == 0:
            pass
        else:
            robot_pos.append(0)
            start_durability[0] -= 1
            if start_durability[0] == 0:
                count += 1
    #end
    step += 1
    
print(step)
