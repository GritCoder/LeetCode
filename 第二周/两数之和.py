# 暴力法
# def solution(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
# 索引相关问题的高效解决思路: 哈希表
def solution(nums, target):
    # Python 中的字典就是用哈希表来实现的
    dic = {}
    # 用到了两个for循环,实际上一次循环也可以
    # for i in range(len(nums)):
    #     dic[nums[i]] = i
    # for i in range(len(nums)):
    #     y = target - nums[i]
    #     if y in dic:
    #         return [i, dic[y]]
    # 一次for循环
    for i in range(len(nums)):
        y = target - nums[i]
        if y in dic:
            return sorted([i, dic[y]])
        dic[nums[i]] = i
print(solution([2, 7, 11, 15], 13))