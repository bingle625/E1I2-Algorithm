class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        stack = [(sr, sc)]
        target_color = image[sr][sc]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while stack:
            e = stack.pop()
            x, y = e[0], e[1]
            if visited[x][y] == False and image[x][y] == target_color:
                image[x][y] = color
                visited[x][y] = True
                for i in range(4):
                    if 0<=x+dx[i]<len(image) and 0<=y+dy[i]<len(image[0]):
                        stack.append((x+dx[i], y+dy[i]))
        return image