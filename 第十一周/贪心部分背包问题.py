'''
inputs：
n和p 代表物品种类数和背包容量
然后输入每种物品的数量、单价、价值
3 10
2 2 3
1 5 10
2 4 12
outputs：
背包的最大价值
27
'''
n, p = list(map(int, input().split()))
matrix = []
for i in range(n):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
# print(matrix)
def solution(matrix, p):
    # 核心语句，属于部分背包问题，按照性价比排序
    matrix.sort(key = lambda item: item[2]/item[1], reverse = True)
    # print(matrix)
    result = []
    for item in matrix:
        # 如果一个都买不起，就跳过这个物品
        if p < item[1]:
            continue
        else:
            # 否则就看看最多能买几件物品
            cnt = p // item[1]
            # 如果cnt不大于物品件数，则购买cnt件
            if cnt <= item[0]:
                result.append(item[2] * cnt)
                p -= item[1] * cnt
            else:
                # 否则，剩几件就买几件
                result.append(item[2] * item[0])
                p -= item[1] * item[0]
            # 其实上面还可以优化一下，就是 cnt = min(cnt, item[0])，知道就行了
    return sum(result)
print(solution(matrix, p))