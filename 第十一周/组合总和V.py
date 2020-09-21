'''面试题：找到和为target的连续子数组：
题意：1.连续，2.所有的
'''
nums = [1,3,-2,5]
target = 6
res = []
def backtrack(i, target, path):
    if target == 0:
        res.append(path)
        return
    if i > len(nums)-1: return # 边界问题
    if target-nums[i] < 0: return # 剪枝
    backtrack(i + 1,target - nums[i],path + [nums[i]])
# 注意这里，连续，所以循环写在这里哦！因为之前那几个版本，都是从0位置开始找的，没啥特殊要求，这里要求连续，从0如果找不到，就换个位置找，注意区别
for i in range(len(nums)-1):
    backtrack(i, target, [])
print(res)