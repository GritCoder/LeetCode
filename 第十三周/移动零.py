# 没有借助辅助空间，先把0给删除，最后再在末尾进行添加
# 如果借助辅助空间，也比较简单，先把非0元素放进list，同时统计0的个数，最后再添加进去同样个数的0即可
def helper(nums, val):
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    # print(slow)
    return slow
def moveZeros(nums):
    p = helper(nums, 0)
    for i in range(p, len(nums)):
        nums[i] = 0
    return nums
print(moveZeros([0,1,0,3,12]))