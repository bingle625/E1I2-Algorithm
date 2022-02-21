
case = int(input())

name_state = {}

for i in range(case):
    name,state = input().split()
    name_state[name] = state

on = []

for name in name_state:
    if name_state[name]=="enter":
        on.append(name)

on.sort()
on = on[::-1]

for name in on:
    print(name)
