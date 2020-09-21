# # 全排列涉及知识点 深搜 广搜 回溯 标记数组
#
# '''
# 回溯法 从深层结点回到浅层结点的过程中所做的操作就叫 回溯
# 这种解法不需要创建标记数组，程序动态维护，但输出不是字典序，若要求字典序输出
# 请用标记数组或者尝试其他方法
# '''
# def permute(inputs):
#     n = len(inputs)
#     res = [] # 结果数组
#     def backtrack(index):
#         if index == n: # 递归程序出口 若不加return，会重复很多遍历 尽管结果正确
#             res.append(inputs[:])
#             return res
#         for i in range(index, n): # first表示要填的第几个位置
#             # 本质上这里也是结果的复制(交换/填充)
#             inputs[index], inputs[i] = inputs[i], inputs[index] # 动态维护数组
#             backtrack(index+1) # 继续填充下一个
#             inputs[index], inputs[i] = inputs[i], inputs[index] # 撤销操作
#     backtrack(0)
#     return res

# DFS实现
def permute(inputs):
    n = len(inputs)
    visit = [False] * n
    res = []
    def dfs(index, tmp):
        if index == n:
            res.append(tmp[:])
            return res
        for i in range(n):
            if visit[i] == False: # 若没有被访问
                visit[i] = True  # 访问
                tmp.append(inputs[i])
                dfs(index + 1, tmp)
                # 回溯至未访问
                visit[i] = False
                tmp.pop()

    dfs(0, [])
    return res  # 正常返回结果
    # tmp = []
    # for item in res:
    #     item = [str(x) for x in item]
    #     print(item)
    #     tmp.append(''.join(item))
    # return list(set(tmp))   # 若有重复字符，并且题目要求去重，则返回此结果
print(permute([1,1,2]))
# 背包问题 临时的
# money = int(input().strip())
# n = int(input().strip())
# prices = []
# values = []
# for x in range(n):
#     tmp = list(map(int, input().strip().split()))
#     prices.append(tmp[0])
#     values.append(tmp[1])
# dp = [[0] * (money+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, money+1):
#         if j < prices[i-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-prices[i-1]] + values[i-1])
# print(dp[n][money])