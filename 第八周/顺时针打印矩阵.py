# 这个代码写的太 6 了 ！
# def printMatrix(matrix):
#     res = []
#     while matrix:
#         res += matrix.pop(0)
#         matrix = list(zip(*matrix))[::-1]
#         # print(matrix)
#     return res
# 常规解法
''' # 注意 "边界"这两个字是相对打印方向来说的
打印方向    根据边界打印          边界收缩         是否打印完毕
从左向右    左边界l 右边界 r      上边界 t 加 1    是否 t > b
从上向下    上边界 t 下边界b      右边界 r 减 1    是否 r < l
从右向左    右边界 r 左边界l      下边界 b 减 1    是否 b < t
从下向上    下边界 b 上边界t      左边界 l 加 1    是否 l > r
'''
# def printMatrix(matrix):
#     if not matrix:
#         return []
#     l, r, t, b, res = 0, len(matrix[0])-1, 0, len(matrix)-1, []
#     while True:
#         for i in range(l, r+1):
#             res.append(matrix[t][i])
#         t += 1
#         if t > b: break
#         for i in range(t, b+1):
#             res.append(matrix[i][r])
#         r -= 1
#         if r < l: break
#         for i in range(r, l-1, -1):
#             res.append(matrix[b][i])
#         b -= 1
#         if t > b: break
#         for i in range(b, t-1, -1):
#             res.append(matrix[l][i])
#         l += 1
#         if l > r: break
#     return res

# 延伸一下 逆时针打印 根据那个表格可以类似的推导出来
def printMatrix(matrix):
    if not matrix:
        return []
    l, r, t, b, res = 0, len(matrix[0])-1, 0, len(matrix)-1, []
    while True:
        for i in range(t, b+1):
            res.append(matrix[i][l])
        l += 1
        if l > r: break

        for i in range(l, r+1):
            res.append(matrix[b][i])
        b -= 1
        if b < t: break

        for i in range(b, t-1, -1):
            res.append(matrix[i][r])
        r -= 1
        if r < l: break

        for i in range(r, l-1, -1):
            res.append(matrix[t][i])
        t += 1
        if t > b: break

    return res
print(printMatrix([[1,2,3],
                   [4,5,6],
                   [7,8,9]]))