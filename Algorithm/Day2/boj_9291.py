Test_count = int(input())
is_correct = True
for i in range(1, Test_count + 1):
    test_case = []
    for j in range(9):
        test_case.append(list(map(int, input().split(" "))))
    test_case_T = list(map(list, zip(*test_case)))
    while is_correct:
        for a in range(9):
            for b in range(9):
                if len(test_case[i]) != len(set(test_case[i])):
                    is_correct = False
                    break
            if not is_correct:
                break
    if is_correct:
        print(f"Case {i}: CORRECT")
    else:
        print(f"Case {i}: INCORRECT")
    print("")