'''
A group of two or more people wants to meet and minimize the total travel distance.
You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
Example:
Input:
1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
Output: 6
Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.
'''
# 详细解题过程可以参考 https://baihuqian.github.io/2018-08-01-best-meeting-point/
# The meeting point is medium of all 1s
# def solution(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#     if rows == 0 or cols == 0:
#         return 0
#     tmp = [] # 保存people的位置
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 1:
#                 tmp.append((i, j))
#     if len(tmp) == 0:
#         return 0
#     x = sorted([p[0] for p in tmp])
#     y = sorted([p[1] for p in tmp])
#     # 经过证明 在中间会晤距离最短 因此要找到中间位置 因此要讨论一下奇偶
#     if len(tmp) % 2 == 1: # 奇数直接取中间那个位置
#         X, Y = x[len(tmp) // 2], y[len(tmp) // 2]
#     else: # 偶数的话就取中间两个数的平均值 注意索引要比长度少1
#         X = (x[len(tmp) // 2 - 1] + x[len(tmp) // 2]) / 2
#         Y = (y[len(tmp) // 2 - 1] + y[len(tmp) // 2]) / 2
#     distance = sum([abs(X - p[0]) + abs(Y - p[1]) for p in tmp])
#     return distance

# 由于排序的存在 多引入了一些时间复杂度 可以不用排序也可以解决此题
def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    if rows == 0 or cols == 0:
        return 0
    x = []
    for i in range(rows): # 从左到右和从上到下的遍历已经保证 x y 都是递增的了 矩阵必然是这样的
        for j in range(cols):
            if matrix[i][j] == 1:
                x.append(i)
    if len(x) == 0:
        return 0
    y = []
    for i in range(rows): # 从左到右和从上到下的遍历已经保证 x y 都是递增的了 矩阵必然是这样的
        for j in range(cols):
            if matrix[i][j] == 1:
                y.append(j)
    # y 也可以不用判断 因为 x y肯定是对应相等的 因为坐标嘛~
    if len(y) == 0:
        return 0
    if len(x) % 2 == 1: # 奇数
        X, Y = x[len(x) // 2], y[len(y) // 2]
    else:
        X = (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        Y = (y[len(y) // 2 - 1] + y[len(y) // 2]) / 2
    distance = sum([abs(X - p) for p in x]) + sum([abs(Y - p) for p in y])
    return distance


