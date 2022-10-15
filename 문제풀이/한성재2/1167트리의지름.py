import collections
from sys import stdin


number = int(input())
dic = collections.defaultdict(list)

for _ in range(number):
    arr = list(map(int, stdin.readline().rstrip().split()))
    for i in range((len(arr)-2)//2):
        dic[arr[0]].append((arr[i*2+1], arr[i*2+2]))

print(dic)


def travel(connected, length, node):
    if node[0] in connected:
        return length
    temp = connected

    if node[0] not in temp:
        print(temp, "hi")
        temp.append(node[0])

    result = 0

    for elem in dic[node[0]]:
        result = max(result, travel(temp, length, elem))

    return result


print(travel([], 0, (1, 0)))
