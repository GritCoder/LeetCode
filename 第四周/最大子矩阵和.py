# 基本思路是转化为一维来做
def getMaxMatrix(matrix) :
    ans = [0]*4 # 初始结果
    N, M = len(matrix), len(matrix[0]) # 行 列
    maxsum = float('-inf') # 初始化最小值，确保第一次被更新
    r1 = c1 = 0 # 初始化左上角索引
    # i, j 就类似于双指针，控制着行的变化
    for i in range(N):
        b = [0] * M # 若换行 则每一列置0 再从头开始累加
        for j in range(i, N):
            sum = 0 # 若换行 则每一列的sum置0 再从头开始累加
            for k in range(M):
                b[k] += matrix[j][k] # 表示以k为结束的最大和
                if sum > 0:
                    sum += b[k]
                else:
                    sum = b[k]
                    r1 = i # 累加和为某个具体元素时，要更新初始索引，然后从这里继续遍历
                    c1 = k
                if sum > maxsum:
                    maxsum = sum
                    ans[0], ans[1], ans[2], ans[3] = r1, c1, j, k # j, k为右下角索引
    return ans

print(getMaxMatrix([[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]))