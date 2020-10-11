# 给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 深搜超时
# def solution(nums):
#     ans = []
#     nums=sorted(nums)
#     def dfs(nums, index,tmp):
#         if len(tmp) == 3 and sum(tmp) == 0:
#             if sorted(tmp) not in ans:
#                 ans.append(tmp)
#         if len(tmp) > 3 and sum(tmp) > 0:
#             return
#         for i in range(index,len(nums)):
#             dfs(nums,i+1, tmp + [nums[i]])
#     dfs(nums,0,[])
#     return ans
# print(solution( [1,-1,-1,0]))

# 排序+双指针
pass # 已提交LeetCode，具体不写了   