# 这个题最大的变化就是，顺序不同的排列是不同的组合，之前的题目，不同排列都是同一个组合
# 回溯 + 减枝，超时
# def solution(nums, target):
#     n = len(nums)
#     nums = sorted(nums)
#     t = target
#     ans = []
#     def backtrack(target, tmp):
#         if sum(tmp) == t:
#             ans.append(tmp)
#             return
#         if sum(tmp) > t:
#             return
#         for i in range(n):
#             backtrack(target-nums[i], tmp+[nums[i]])
#     backtrack(target, [])
#     return ans

# dp解法
def solution1(nums, target):
    if not nums:
        return 0
    # dp[i]表示的是，数字 i 有几种组合方式
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            # 必须加等号，否则会结果错误
            if i >= num:
                dp[i] = dp[i] + dp[i-num]
    return dp[target]
print(solution1([3, 2, 1], 4))