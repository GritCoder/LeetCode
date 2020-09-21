# 这个版本的元素有重复的，最后需要返回不重复的排列，即要去重
# DFS实现
def permute(inputs):
    n = len(inputs)
    visit = [False] * n
    res = []
    # 排序确保重复元素在一块
    inputs.sort()
    def dfs(index, tmp):
        if index == n:
            res.append(tmp[:])
            return res
        for i in range(n):
            if visit[i] == False:  # 若没有被访问
                # 如果是重复元素，跳过
                if i > 0 and inputs[i] == inputs[i-1] and not visit[i-1]:
                    continue

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
print(permute([1, 1, 2]))