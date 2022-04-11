# 섬의 개수
# 리트코드 200번 Number of Island


def dfs(grid: list[list[str]], i: int, j: int):
    # 더이상 땅이 아닌 경우 종료
    if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
        return

    grid[i][j] = '0'

    # 동서남북 탐색
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)


def numIslands(grid: list[list[str]]) -> int:
    # 예외 처리
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1

    return count


grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]

print(numIslands(grid))
