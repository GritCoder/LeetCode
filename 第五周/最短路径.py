# 注意，Dijkstra算法求的是单源点到其他结点的最短路径，且路径里面不能出现负值(否则算法会不正确)
# 本质是贪心 + 广搜(BFS)  只能计算无向图
# def dijkstra(start, matrix): # matrix肯定是方阵 索引值代表结点值
#     passed = [start] # 已访问
#     nopass = [x for x in range(len(matrix)) if x != start] # 未访问
#     distance = matrix[start] # 起始点到其他结点的距离
#     while len(nopass): # 当还有未访问结点时
#         idx = nopass[0]
#         for i in nopass: # 选择一个距离起始点最近的结点(贪心)
#             if distance[i] < distance[idx]: # distance[i] 表示的是起始结点到 i 结点的距离
#                 idx = i
#         # 更新标记数组
#         nopass.remove(idx)
#         passed.append(idx)
#         # 通过最近结点来更新起始点到其他结点的距离(即直接到达与踩着最近点间接到达的比较)
#         for i in nopass:
#             if distance[idx] + matrix[idx][i] < distance[i]:
#                 distance[i] = distance[idx] + matrix[idx][i]
#     return distance
# 佛洛依德算法 本质动态规划思想 可以计算无向图或有向图 任意两点间的距离 算法复杂度O(n^3)
# 核心是 Dis(i,k) + Dis(k,j) < Dis(i,j) 这个公式  可以用数学归纳法证明
def floyd(n, matrix):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    # path[i][j] = k # 这里可以记录路径 知道就行了
    return matrix
n, m = map(int, input().split()) # 其实极大多数情况m n是相等的 即表示图结点个数(这个时候不能理解为矩阵的宽高了)
# matrix = [[float('inf')] * m for _ in range(n)]
# print(matrix)
# for i in range(n):
#     for j in range(m):
        # matrix[i][j] = float(input()) # 这种写法一行只能输入一个数  然后换行
matrix = []
for i in range(n):
    lis = list(map(float, input().split())) #
    matrix.append(lis)
# print(dijkstra(0, matrix))
print(floyd(n, matrix))
