# 1874번

# 스택수열

last_one = 0
last_max = 0
output = []
result = []

num = int(input())

for i in range(num):
    present_one = int(input())
    # 1. present_one이 last_one 보다 작은 경우
    # 1.1 1작은 경우 => okay
    # 1.2.1 1보다 더 작은 경우 => 그 수까지 도달하는 수가 모두 output에 있는 경우 => okay
    # 1.2.2 1보다 더 작은경우 => 그 수까지 도달하는 수가 모두 output에 있지 않은 경우 => No
    # 2. present_one이 last_one보다 큰 경우 => okay
    if present_one < last_one:
        if last_one-present_one == 1:
            output.append(present_one)
            result.append("-")
            last_one = present_one
        else:
            for k in range(present_one+1, last_one):
                if k in output:
                    continue
                else:
                    result.append("NO")

            output.append(present_one)
            result.append("-")
            last_one = present_one
    else:
        output.append(present_one)

        for _ in range(last_max, present_one):
            result.append("+")
        result.append("-")
        last_one = present_one

    if present_one > last_max:
        last_max = present_one

if "NO" in result:
    print("NO")
else:
    for res in result:
        print(res)
