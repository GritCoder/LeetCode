# 看正方形周围是不是水，或者在边界处，这样才能产生周长
# 暴力法 当岛屿数量比较少的时候(即 1 比较少) 这样写效率会有点低 了解一下
# def perimeterOfIslands(matrix):
#     if not matrix:
#         return 0
#     row, col = len(matrix), len(matrix[0])
#     ans = 0
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j] == 1:
#                 for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]: # 四个方向
#                     if 0 <= x < row  and 0 <= y < col and matrix[x][y] == 1: # 正常情况 周围是岛屿并且不在边界 是执行的条件 但这里恰好不执行 理解
#                         pass
#                     else:
#                         ans += 1
#     return ans
# 深搜
def perimeterOfIslands(matrix):
    def dfs(matrix, i, j, ans):
        if i < 0 or i >= row or j < 0 or j >= col: # 边界
            # ans += 1  # 不能定义个全局变量这样写递归 之前旷世面试就犯过这样的错误了 这样写程序就没有递归出口了
            return 1
        if matrix[i][j] == 0: # 水
            # ans += 1
            return 1
        if matrix[i][j] == 2: # 已访问过 return 0
            return 0
        matrix[i][j] = 2  # 标记访问
        # dfs 不用返回  因为ans这里相当于全局变量
        # ans 这个多余变量不删除了 你自己知道就行 给自己提个醒
        return dfs(matrix, i - 1, j, ans) + dfs(matrix, i + 1, j, ans) + dfs(matrix, i, j - 1, ans) + dfs(matrix, i, j + 1, ans)

    if not matrix:
        return 0
    row, col = len(matrix), len(matrix[0])
    ans = 0 # 可以多用ans变量 少用res 免得跟return有点像
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                # 题目中说了 只有一个岛屿 所以可以这样 找到后直接return就行了
                return dfs(matrix, i, j, ans)
    # return ans
print(perimeterOfIslands(
[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))