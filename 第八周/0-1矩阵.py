# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。 两个相邻元素间的距离为 1
'''
引入超级0 我们可以把这些 0 看成一个整体好了 任意一个 1 到它最近的 0 的距离，会等于这个 1 到「超级零」的距离减去一
在广度优先搜索的过程中，我们每遇到一个 1，就得到了它到「超级零」的距离减去一，也就是 这个 1 到最近的 0 的距离
熟悉「最短路」的读者应该知道，我们所说的「超级零」实际上就是一个「超级源点」。在最短路问题中，如果我们要求多个源点出发的最短路时
一般我们都会建立一个「超级源点」连向所有的源点，用「超级源点」到终点的最短路等价多个源点到终点的最短路。
[ 多源点最短路径问题也可以用佛洛依德算法 ]
'''
from collections import deque
def solution(matrix):
    if not matrix:
        return
    row, col = len(matrix), len(matrix[0])
    dist = [[0] * col for _ in range(row)]
    zeros_pos = [(i, j) for i in range(row) for j in range(col) if matrix[i][j] == '.']
    q = deque(zeros_pos)
    seen = set(zeros_pos) # 养成一个好的思维习惯 只要跟深搜广搜相关的 一般都少不了标记数组
    while q:
        i, j = q.popleft()
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
              # seen数组也是可以省去的，每次找的时候，可以通过判断dist[ni][nj] == 0 and matrix[ni][nj] == 1来筛选没有访问过的节点。
            if 0 <= ni < row and 0 <= nj < col and (ni, nj) not in seen:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
                seen.add((ni, nj))
    return sum(max(dist))
# 动态规划
'''
对于矩阵中的任意一个 1 以及一个 0，我们如何从这个 1 到达 0 并且距离最短呢？
只有 水平向左移动 和 竖直向上移动
只有 水平向左移动 和 竖直向下移动
只有 水平向右移动 和 竖直向上移动
只有 水平向右移动 和 竖直向下移动
'''
# def solution(matrix):
#     if not matrix:
#         return
#     row, col = len(matrix), len(matrix[0])
#     dist = [[10**9] * col for _ in range(row)] # 初始化一个较大值 确保矩阵会被更新
#     # 找0的位置
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j] == 0:
#                 dist[i][j] = 0 # 0到0本身的距离为0
#     # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
#     for i in range(row): # 如果索引朝着下降的方向走 则正常遍历 先取小索引 可能这样考虑是优先利用边界条件吧
#         for j in range(col):
#             if i - 1 >= 0:
#                 dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
#             if j - 1 >= 0:
#                 dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
#     # 优化一下 只保留左上和右下即可 证明略
#     # # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
#     # for i in range(row-1, -1, -1):
#     #     for j in range(col):
#     #         if i + 1 < row:
#     #             dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
#     #         if j - 1 >= 0:
#     #             dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
#     # # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
#     # for i in range(row):
#     #     for j in range(col-1, -1, -1):
#     #         if i - 1 >= 0:
#     #             dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
#     #         if j + 1 < col:
#     #             dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
#     # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
#     for i in range(row-1, -1, -1):  # 如果索引朝着增加的方向走 则逆序遍历 先取大索引 可能这样考虑是优先利用边界条件吧
#         for j in range(col-1, -1, -1):
#             if i + 1 < row:
#                 dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
#             if j + 1 < col:
#                 dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
#     return dist
in_ = list(map(int, input().strip().split()))
H, W = in_[0], in_[1] # 行 列
tmp = []
matrix = []
for i in range(H):
    tmp = list(map(str, input().strip()))
    matrix.append(tmp)
print(solution(matrix))
