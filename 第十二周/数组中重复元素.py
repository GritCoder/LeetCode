# 数组长度为n,且元素范围为1-n,有些元素只出现一次，有些出现两次，求出所有出现两次的元素
# 常规方法就是用哈希，求出每个元素出现的次数，然后遍历即可
# 这个方法空间复杂度为O(1)，具体看题目要求
def solution(nums):
    if not nums:
        return []
    n = len(nums)
    ans = []
    for i in range(n):
        # 因为有可能被取反过，所以这里取个绝对值
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            ans.append(index + 1)
        nums[index] = -nums[index]
    return ans
print(solution([4,3,2,7,8,2,3,1]))