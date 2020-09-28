# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 和数组中重复元素那个题目类似
def solution1(nums):
    if not nums:
        return []
    dic, ans = {}, []
    for num in nums:
        dic[num] = 1
    for num in nums:
        # 默认的是按照key来判断的
        if num not in dic:
            ans.append(num)
    return ans

def solution2(nums):
    if not nums:
        return []
    ans = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] *= -1
    for i in range(1, len(nums)+1):
        if nums[i-1] > 0:
            ans.append(i)
    return ans