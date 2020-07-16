'''
注释掉的地方是尝试记录路径，LCS  LIS都可以记录路径 基本思想都是从最后递归的往前找 DFS深搜
了解一下，具体执行代码还有一点小问题
'''
def LIS(nums):
    length = len(nums)
    if length == 0 or length == 1:
        return length
    dp = [1] * length  # dp[i]表示的是以 i 处结束时的最大上升子序列
    # path = [-1] * length
    # ans, max_pos = [], 0
    for i in range(length):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
                # path[i] = j
                # max_pos = i
    # print(dp) # 找个demo自己走一遍程序 秒懂

    # def dfs(pos):
    #     if path[pos] != -1:
    #         dfs(path[pos])
    #         ans.append(nums[pos])
    #     # else:
    #     #     ans.append(nums[pos])
    #     #     return
    #     return ans
    # print(path)
    # print(dfs(max_pos))

    return max(dp)
print(LIS([1,2,3,0,5]))