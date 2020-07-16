A = [[1,2,3],
     [4,5,6]]
B = [[7,3],
     [8,1],
     [2,9]]
# zipped = zip(A,B)
# for item in zip(*zipped): # 与 zip 相反，*zipped 可理解为解压 返回原来格式的元组形式
#     print(item)
row1, col1, col2 = len(A), len(A[0]), len(B[0])
res = [[0]*col2 for _ in range(row1)]

for i in range(row1): # 行
    for j in range(col2): # 列
        for k in range(col1): # 行
            res[i][j] += A[i][k] * B[k][j]
print(res)

# 对于算法优化，最广为人知的是Strassen算法，能达到 n^2.8 的时间复杂度
# 基本思想是矩阵分解分块那一部分的东西，然后再利用递归实现，了解一下就行，实现太复杂了
# 指数只减少了0.2，因此当 n 特别大的时候，Strassen算法才有一定的优势

# 默认矩阵是按行存储的，改变位置可以让内存访问变得连续，增加cache命中率
# 对于硬件优化, 调换循环顺序, 例如将原来的 ijk 顺序改成 ikj 顺序
# 实际上有 ikj > kij > jik > ijk > kji > jki (基本原理是先访问行再访问列)
res = [[0]*col2 for _ in range(row1)]
# 表达式复杂度没变 但是实际运行速度大大提升
for i in range(row1): # 行
    for k in range(col1): # 行
        for j in range(col2): # 列
            res[i][j] += A[i][k] * B[k][j]
print(res)

# 矩阵转置就很简单了 注意引入一个辅助数组 在A自身上面艹作很容易报错
tmp = [[0]*row1 for _ in range(col1)]
for i in range(row1):
    for j in range(col1):
        tmp[j][i] = A[i][j] # 核心
print(tmp)


