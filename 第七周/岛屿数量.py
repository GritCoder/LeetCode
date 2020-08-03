# 深搜 注意做标记和递归结束条件
def numOfIslands(matrix):
    def dfs(matrix, i, j):
        if i < 0 or i >= row or j < 0 or j >= col:
            return 0
        if matrix[i][j] == 1: # 是岛的话就 +1 并去递归的搜索相邻的四个方向
            matrix[i][j] = 0 # 标记已访问
            return dfs(matrix, i, j-1) + dfs(matrix, i-1, j) + dfs(matrix, i+1, j) + dfs(matrix, i, j+1) + 1 # 去递归的搜索4个方向 上下左右
        else:
            return 0

    if not matrix:
        return 0
    row, col = len(matrix), len(matrix[0])
    num = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                if dfs(matrix, i, j) >= 1: # 说明是岛
                    num += 1
    return num
# 广搜 队列为空即搜索结束，是很多广搜的trick
# from collections import deque
# def numOfIslands(matrix):
#     if not matrix:
#         return 0
#     row, col = len(matrix), len(matrix[0])
#     num = 0
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j] == 1:
#                 num += 1
#                 matrix[i][j] = 0
#                 # 这样初始化的话 必须加列表符号 否则不是可迭代对象 报错
#                 q = deque([(i, j)]) # 注意入队的是坐标，入队节点在这里没啥意义
#                 while q:
#                     row1, col1 = q.popleft()
#                     for x, y in [(row1+1,col1), (row1-1,col1), (row1,col1+1),(row1,col1-1)]:
#                         if 0 <= x < row and 0 <= y < col and matrix[x][y] == 1:
#                             q.append((x, y)) # 这里append就不用加列表符号了 因为上面初始化做了 否则也会报错 注意！！！
#                             matrix[x][y] = 0
#     return num

matrix = []
tmp = []
for i in range(6):
    tmp = list(map(str, input().strip()))
    matrix.append(tmp)
print(numOfIslands(matrix))