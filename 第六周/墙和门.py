'''
You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''
'''
这道题类似一种迷宫问题，规定了 -1 表示墙，0表示门，让求每个点到门的最近的曼哈顿距离，
这其实类似于求距离场 Distance Map 的问题，那么先考虑用 DFS 来解，
思路是，搜索0的位置，每找到一个0，以其周围四个相邻点为起点，开始 DFS 遍历，并带入深度值1，
如果遇到的值大于当前深度值，将位置值赋为当前深度值，并对当前点的四个相邻点开始DFS遍历，
注意此时深度值需要加1，这样遍历完成后，所有的位置就被正确地更新了，参见代码如下：
'''
def wallAndGate(matrix):

    m, n = len(matrix), len(matrix[0])

    def dfs(matrix, i, j, val):
        # 先判断下是否越界                        # 因为val初始为0 如果碰见 -1 则不更新 因为 -1 < 0 因此墙的情况在这个条件里面已经考虑到了
        if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] < val:
            return                               # 当前位置小于深度值 所以不更新位置的值
        matrix[i][j] = val # 否则更新位置值
        dfs(matrix, i+1, j, val+1) # 下
        dfs(matrix, i-1, j, val + 1) # 上
        dfs(matrix, i, j+1, val + 1) # 右
        dfs(matrix, i, j-1, val + 1) # 左

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '.': # 找门
                dfs(matrix, i, j, 0) # 0表示距离 一开始肯定初始化为0
    return matrix # 实际上是inplace操作 不用临时副本了
# print(wallAndGate([[float('inf'), -1, 0, float('inf')],
#                    [float('inf'), float('inf'), float('inf'), -1],
#                    [float('inf'), -1, float('inf'), -1],
#                    [0, -1, float('inf'), float('inf')]]))

in_ = list(map(int, input().strip().split()))
H, W = in_[0], in_[1] # 行 列
tmp = []
matrix = []
for i in range(H):
    tmp = list(map(str, input().strip()))
    matrix.append(tmp)
print(wallAndGate(matrix))



