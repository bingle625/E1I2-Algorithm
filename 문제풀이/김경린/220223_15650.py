
result = []

end,num = map(int,input().split())


def dfs(elements,start,num):
    if num==0:
        result.append(elements[:])
        
    else:
        for i in range(start,end+1):
            elements.append(i)
            dfs(elements,i+1,num-1)
            elements.pop()

    
    return result

result_list = dfs([],1,num)

for element in result_list:
    print(*element)


