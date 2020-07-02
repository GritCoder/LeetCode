# 全排列涉及知识点 深搜 广搜 回溯 标记数组

'''
回溯法 从深层结点回到浅层结点的过程中所做的操作就叫 回溯
这种解法不需要创建标记数组，程序动态维护，但输出不是字典序，若要求字典序输出
请用标记数组或者尝试其他方法
'''
# def permute(inputs):
#     n = len(inputs)
#     res = [] # 结果数组
#     def backtrack(first=0):
#         if first == n: # 递归程序出口 若不加return，会重复很多遍历 尽管结果正确
#             res.append(inputs[:])
#             return res
#         for i in range(first, n): # first表示要填的第几个位置
#             # 本质上这里也是结果的复制(交换/填充)
#             inputs[first], inputs[i] = inputs[i], inputs[first] # 动态维护数组
#             backtrack(first+1) # 继续填充下一个
#             inputs[first], inputs[i] = inputs[i], inputs[first] # 撤销操作
#     backtrack()
#     return res
# DFS实现
def permute(inputs):
    length = len(inputs)
    visit = [False] * length
    res, tmp = [], [0] * length
    def dfs(position):
        if position == length:
            res.append(tmp[:])
            return res
        for i in range(length):
            if visit[i] == False: # 若没有被访问
                tmp[position] = inputs[i]
                visit[i] = True # 访问
                dfs(position + 1) # 全排列只跟位置有关 因为结果长度都是一样的 所以此处为position
                visit[i] = False # 回溯至未访问
    dfs(0)
    return res
print(permute([1,2,3]))
