# 对于每个 0，我们将它暂时变成 1，然后统计这个连通块的大小。
# 对于每个 0，将它变成 1，然后做一次深度优先搜索计算出连通块的大小。答案就是找到的最大连通块。
# 当然，如果没有 0，那么答案就是整个网格的大小。
# 本质上是递归+回溯+队列
from collections import deque
def maxAreaIsland(matrix):
    def dfs(matrix, i, j):
        seen = {(i, j)} # 是1的话则加进去 有点类似于标记数组的味道
        q = deque([(i, j)])
        while q:
            row_, col_ = q.popleft()
            for x, y in [(row_+1, col_), (row_-1, col_), (row_, col_+1), (row_, col_-1)]:
                if (x, y) not in seen and 0 <= x < row and 0 <= y < col and matrix[x][y] == 1:
                    seen.add((x, y))
                    q.append((x, y))
        return len(seen) # 1的个数即为面积

    if not matrix:
        return 0
    row, col = len(matrix), len(matrix[0])
    has_zero = False
    area = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                has_zero = True
                matrix[i][j] = 1
                area = max(area, dfs(matrix, i, j))
                matrix[i][j] = 0 # 回溯
    return area if has_zero else row * col