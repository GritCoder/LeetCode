# 借助辅助数组
def rotate(matrix):
    n = len(matrix[0])
    # 初始化 若不是方阵，输入跟初始化也很好变化对应
    matrix_new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 找旋转前后位置变化的规律
              # new_row = old_col
              # new_col = n-old_row-1
            matrix_new[j][n-i-1] = matrix[i][j]
    # python里面这三种写法都对
    matrix = matrix_new
    # matrix[:] = matrix_new
    # matrix = matrix_new.copy()
    return matrix
# 就地旋转，没有额外空间
# def rotate(matrix):
#     n = len(matrix[0])
#     # matrix_new = [[0]*n for _ in range(n)]
#     # 讨论奇偶 确定遍历空间，不要都遍历 反而会报错
#     for i in range(int(n/2)):
#         for j in range(int((n+1)/2)):
#             # 引入一个临时变量即可 发现规律
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[n-j-1][i]
#             matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
#             matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
#             matrix[j][n-i-1] = temp
#     return matrix

n = input()
matrix = []
for i in range(int(n)):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
print(rotate(matrix))



